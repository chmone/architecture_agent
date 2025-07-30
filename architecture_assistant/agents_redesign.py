# Copyright 2025
# Redesigned Architecture Assistant with Proper Multi-Agent Pattern

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
    description="Researches and proposes optimal architecture solutions based on project requirements",
    instruction="""You are an architecture analysis expert who researches and proposes solutions.

When called, you should:

1. **Parse the Requirements** from what you're given:
   - Project type and domain
   - Scale expectations  
   - Team size and expertise
   - Timeline and constraints
   - Any existing systems

2. **Research Current Best Practices** using Google Search:
   - Search for current architectural patterns for the project type
   - Look up latest framework recommendations
   - Find real-world case studies and benchmarks
   - Research common pitfalls and solutions

3. **Propose an Architecture** with:
   - Recommended architectural pattern (monolith, microservices, serverless, etc.)
   - Specific technology stack with versions
   - Infrastructure recommendations
   - Key design decisions and trade-offs
   - Clear reasoning for each choice

Format your response clearly with sections for:
- Requirements Understanding
- Research Findings  
- Proposed Architecture
- Reasoning and Trade-offs

Be specific and practical in your recommendations.""",
    tools=[google_search]
)

# Sub-agent 2: Double Check Agent
double_check_agent = Agent(
    model="gemini-2.0-flash",
    name="double_check_agent",
    description="Validates proposed architectures against requirements and provides feedback",
    instruction="""You are an architecture validation expert who ensures proposals meet requirements.

When called, you should:

1. **Review the Original Requirements** from the conversation
2. **Analyze the Proposed Architecture** for:
   - Does it meet all stated requirements?
   - Is it appropriate for the team size and timeline?
   - Does it respect constraints (budget, existing systems)?
   - Is it over-engineered or under-engineered?

3. **Make a Decision**:
   - If the architecture is appropriate and well-reasoned, call exit_loop() to approve it
   - If improvements are needed, provide specific feedback:
     * What issues did you find?
     * What specific improvements are needed?
     * What should be reconsidered?

Be thorough but practical. The goal is a working architecture for THIS team and project.""",
    tools=[exit_loop]
)

# Loop Agent: Orchestrates the iterative refinement
architecture_loop_agent = LoopAgent(
    name="architecture_loop_agent",
    description="Iteratively refines architecture through research and validation",
    sub_agents=[
        analyze_requirements_agent,
        double_check_agent
    ],
    max_iterations=3
)

# Note: Removed format_requirements function and tool to avoid function calling issues
# The main agent will format requirements directly in conversation

# Main Architecture Assistant Agent
root_agent = Agent(
    model="gemini-2.0-flash",
    name="architecture_assistant",
    description="Helps developers design software architectures through intelligent analysis",
    instruction="""You are a software architecture assistant that helps developers make informed architecture decisions.

## Your Capabilities

You have access to:
1. **Google Search** - For quick lookups and general information
2. **architecture_loop_agent** - An intelligent sub-agent that researches and refines architecture proposals

## How to Help Users

When a user needs architecture help:

1. **First, gather information** by asking about:
   - What type of application (web, mobile, API, etc.)
   - Expected scale and users
   - Team size and experience
   - Timeline and budget
   - Any constraints or existing systems

2. **For architecture design requests**:
   - Format the requirements clearly as:
     * Project Type: [type]
     * Expected Scale: [scale]
     * Team Size: [number] developers
     * Timeline: [months] months
     * Constraints: [list any constraints]
     * Additional Context: [any other relevant info]
   - Then delegate to architecture_loop_agent by saying:
     "I'll have the architecture_loop_agent analyze these requirements and propose a solution"
   - The loop agent will research, propose, validate, and refine the architecture
   - Present the final validated architecture to the user

3. **For quick questions** (not full architecture design):
   - Use Google Search for current information
   - Answer directly without delegating

## Important Guidelines

- Always delegate substantial architecture design to architecture_loop_agent
- Be conversational and helpful
- Ask clarifying questions when needed
- Present results clearly and explain the reasoning

Remember: Good architecture balances ideal solutions with practical constraints.""",
    tools=[google_search],
    sub_agents=[architecture_loop_agent]  # Key: sub-agent defined here, not as a tool
)