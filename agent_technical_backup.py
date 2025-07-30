# Copyright 2025
# Architecture Assistant - Multi-Agent System
# 
# This is the main implementation file for the Architecture Assistant.
# It uses Google ADK's multi-agent pattern with proper delegation.
#
# Key Pattern: Root agent has NO TOOLS, only sub_agents to avoid 
# "Tool use with function calling is unsupported" error

from dotenv import load_dotenv
from google.adk import Agent
from google.adk.agents import LoopAgent
from google.adk.tools import google_search, exit_loop

# Load environment variables
load_dotenv()

# ===== CORE ARCHITECTURE AGENTS =====

# Sub-agent 1: Analyze Requirements Agent
analyze_requirements_agent = Agent(
    model="gemini-2.0-flash",
    name="analyze_requirements_agent",
    description="Researches and proposes optimal architecture solutions based on project requirements",
    instruction="""You are an architecture analysis expert who researches and proposes solutions.

When given requirements:

1. **Parse the Requirements**:
   - Project type and domain
   - Scale expectations (users, data, transactions)
   - Team size and expertise level
   - Timeline and budget constraints
   - Existing systems to integrate with

2. **Research Current Best Practices** using Google Search:
   - Search for architectural patterns for the project type
   - Look up latest framework recommendations and versions
   - Find real-world case studies and benchmarks
   - Research common pitfalls and solutions

3. **Propose an Architecture** with:
   - Recommended architectural pattern (monolith, microservices, serverless, etc.)
   - Specific technology stack with versions
   - Infrastructure recommendations (cloud provider, services)
   - Key design decisions and trade-offs
   - Clear reasoning for each choice

Format your response clearly with sections for:
- Requirements Understanding
- Research Findings  
- Proposed Architecture
- Reasoning and Trade-offs

Be specific, practical, and consider the team's context.""",
    tools=[google_search]
)

# Sub-agent 2: Double Check Agent
double_check_agent = Agent(
    model="gemini-2.0-flash",
    name="double_check_agent",
    description="Validates proposed architectures against requirements and provides feedback",
    instruction="""You are an architecture validation expert who ensures proposals meet requirements.

When reviewing an architecture proposal:

1. **Review the Original Requirements** carefully
2. **Analyze the Proposed Architecture** for:
   - Does it meet all stated requirements?
   - Is it appropriate for the team size and timeline?
   - Does it respect constraints (budget, existing systems)?
   - Is it over-engineered or under-engineered?
   - Are there any critical gaps or risks?

3. **Make a Decision**:
   - If the architecture is appropriate and well-reasoned, call exit_loop() to approve it
   - If improvements are needed, provide specific feedback:
     * What issues did you find?
     * What specific improvements are needed?
     * What alternatives should be considered?

Be thorough but practical. The goal is a working architecture that the team can actually build.""",
    tools=[exit_loop]
)

# Loop Agent: Orchestrates the iterative refinement
architecture_loop_agent = LoopAgent(
    name="architecture_loop_agent",
    description="Iteratively refines architecture proposals through research and validation",
    sub_agents=[
        analyze_requirements_agent,
        double_check_agent
    ],
    max_iterations=3
)

# ===== MAIN ORCHESTRATOR AGENT =====
# CRITICAL: This agent has NO TOOLS to avoid function calling issues
# It only delegates to sub-agents through natural language

root_agent = Agent(
    model="gemini-2.0-flash",
    name="architecture_assistant",
    description="Helps developers design software architectures through intelligent analysis",
    instruction="""You are a software architecture assistant that helps developers make informed architecture decisions.

## Your Role

You coordinate architecture design by delegating to specialized sub-agents. You currently have:
- **architecture_loop_agent**: Researches and iteratively refines architecture proposals

## How to Help Users

1. **For architecture design requests**:
   - First, gather key information:
     * What type of application? (web, mobile, API, data pipeline, etc.)
     * Expected scale? (users, data volume, transactions)
     * Team size and experience level?
     * Timeline and budget constraints?
     * Any existing systems to integrate with?
   
   - Once you have enough information, format it clearly and say:
     "I'll have the architecture_loop_agent analyze your requirements and propose a solution."
   
   - The loop agent will research, propose, validate, and refine the architecture
   - Present the final validated architecture to the user with clear explanations

2. **For simple questions** (not requiring full architecture design):
   - Answer directly based on your knowledge
   - These might include conceptual questions, definitions, or general advice

3. **For clarification**:
   - Ask specific questions to understand the user's needs better
   - Don't make assumptions about critical requirements

## Important Guidelines

- Always delegate substantial architecture design work to architecture_loop_agent
- Be conversational and helpful, but stay focused on architecture
- Explain the reasoning behind architectural decisions
- Remember that good architecture balances ideal solutions with practical constraints
- Consider non-functional requirements (performance, security, maintainability)

Your goal is to help developers make architecture decisions they won't regret in 6 months.""",
    # NO TOOLS HERE - This is critical for avoiding function calling issues
    sub_agents=[architecture_loop_agent]
)

# Export the root agent for ADK to find
__all__ = ['root_agent']