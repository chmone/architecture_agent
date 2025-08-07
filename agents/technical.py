# Architecture Assistant - Technical Design Agents
#
# These agents handle technical architecture design and validation

from google.adk import Agent
from google.adk.agents import LoopAgent
from google.adk.tools import exit_loop
from .search import search_agent_tool

# ===== TECHNICAL DESIGN AGENTS (keeping existing capability) =====

# Core Architecture Analyzer (simplified from original)
ARCHITECTURE_ANALYZER_PROMPT = """You are an architecture expert who translates business requirements into technical designs.

## YOUR ONLY JOB
Create a technical architecture design based on requirements. Nothing more.

## CRITICAL BOUNDARIES - YOU MUST NEVER:
- Start implementing or coding the solution
- Create detailed technical specifications
- Write actual code snippets
- Begin building components
- Take over development work
- Continue after architecture is defined
- Move into execution phase

## YOUR APPROACH
When given requirements:
1. Use the search_agent tool to research current best practices and patterns
2. Propose architecture that balances simplicity with scalability
3. Focus on what can actually be built by the team
4. Explain technical choices in business terms

## OUTPUT SHOULD INCLUDE
- Recommended architecture pattern
- Technology stack with justifications  
- Key design decisions
- Implementation approach

Keep explanations clear and avoid overwhelming technical detail.

## COMPLETION CRITERIA - YOU ARE DONE WHEN:
1. You've delivered the architecture design
2. The double_check_agent will validate your work
3. Focus on completing the design, not continuing conversation

## EXIT BEHAVIOR
Complete your architecture proposal and wait for validation. Do not continue beyond your architectural recommendations.

CRITICAL: Stay within the bounds of architecture design. Do not venture into implementation.
"""

analyze_requirements_agent = Agent(
    model="gemini-2.0-flash",
    name="analyze_requirements_agent",
    description="Translates requirements into technical architecture",
    instruction=ARCHITECTURE_ANALYZER_PROMPT,
    tools=[search_agent_tool]  # Can use search_agent via AgentTool
)

# Architecture Validator
ARCHITECTURE_VALIDATOR_PROMPT = """You validate proposed architectures for practicality and fit.

Review the architecture for:
- Does it meet the business requirements?
- Is it buildable by the team?
- Is it appropriately complex?
- Are there critical gaps?

If appropriate, call exit_loop() to approve.
If not, provide specific, actionable feedback.
"""

double_check_agent = Agent(
    model="gemini-2.0-flash",
    name="double_check_agent",
    description="Validates architecture proposals",
    instruction=ARCHITECTURE_VALIDATOR_PROMPT,
    tools=[exit_loop]
)

# Technical Architecture Loop (kept for users who need it)
architecture_loop_agent = LoopAgent(
    name="architecture_loop_agent",
    description="Develops technical architecture through iteration",
    sub_agents=[
        analyze_requirements_agent,
        double_check_agent
    ],
    max_iterations=3
)

__all__ = ['architecture_loop_agent', 'analyze_requirements_agent', 'double_check_agent']