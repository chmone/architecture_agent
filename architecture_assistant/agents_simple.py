# Copyright 2025
# Simplified Architecture Assistant - Minimal Multi-Agent Pattern

from dotenv import load_dotenv
from google.adk import Agent
from google.adk.agents import LoopAgent
from google.adk.tools import google_search, exit_loop

# Load environment variables
load_dotenv()

# Sub-agent 1: Analyze Requirements Agent
analyze_requirements_agent = Agent(
    model="gemini-2.0-flash",
    name="analyze_requirements_agent",
    description="Researches and proposes optimal architecture solutions",
    instruction="""You research and propose architecture solutions.

When given requirements:
1. Use Google Search to research current best practices
2. Propose an architecture with:
   - Pattern (monolith, microservices, etc.)
   - Technology stack
   - Infrastructure
   - Key trade-offs

Be specific and practical.""",
    tools=[google_search]
)

# Sub-agent 2: Double Check Agent  
double_check_agent = Agent(
    model="gemini-2.0-flash",
    name="double_check_agent",
    description="Validates proposed architectures",
    instruction="""You validate architecture proposals.

Review the proposed architecture:
- Does it meet the requirements?
- Is it appropriate for the team size and timeline?
- Is it over/under-engineered?

If appropriate, call exit_loop() to approve.
If not, provide specific feedback for improvement.""",
    tools=[exit_loop]
)

# Loop Agent
architecture_loop_agent = LoopAgent(
    name="architecture_loop_agent",
    description="Iteratively refines architecture proposals",
    sub_agents=[
        analyze_requirements_agent,
        double_check_agent
    ],
    max_iterations=3
)

# Main Agent - NO TOOLS to avoid function calling issues
root_agent = Agent(
    model="gemini-2.0-flash",
    name="architecture_assistant",
    description="Helps with software architecture decisions",
    instruction="""You help developers design software architectures.

When users need architecture help:
1. Ask about their project type, scale, team size, timeline, and constraints
2. Once you have the information, say: "I'll have the architecture_loop_agent analyze your requirements"
3. The architecture_loop_agent will research and refine a solution
4. Present the final architecture recommendation

For simple questions not needing full analysis, just answer directly.

You delegate to architecture_loop_agent for any substantial architecture design work.""",
    # NO TOOLS HERE - avoiding function calling issues
    sub_agents=[architecture_loop_agent]
)