# Copyright 2025
# Architecture Assistant - User-Centric Multi-Agent System
# 
# This implementation focuses on education and empowerment for non-technical users
# turning their ideas into actionable technical plans through conversation and learning.
#
# CRITICAL ADK CONSTRAINTS:
# 1. Agents can have either 'tools' OR 'sub_agents', NEVER both
# 2. Root orchestrator: Has sub_agents only (no tools property)
# 3. Worker agents: Have tools only (no sub_agents property)
# 4. Delegation happens through natural language mentions, not function calls
# 5. Keep delegation phrases simple: "Let's use X" not "I'll have X do Y"
#
# This architecture prevents "Tool use with function calling is unsupported" error

from dotenv import load_dotenv
from google.adk import Agent

# Import all agents from the modular architecture
# When ADK loads this module, it sets up the import path correctly
from .agents import (
      requirements_discovery_agent,
      project_reality_check_agent,
      education_loop_agent,        architecture_loop_agent,
      implementation_roadmap_agent
    )
from .agents.orchestrator import USER_CENTRIC_ORCHESTRATOR_PROMPT

# Load environment variables
load_dotenv()

# Create root agent - CRITICAL: NO TOOLS!
root_agent = Agent(
    model="gemini-2.0-flash",
    name="architecture_assistant",
    description="Helps non-technical users turn ideas into actionable technical plans",
    instruction=USER_CENTRIC_ORCHESTRATOR_PROMPT,
    sub_agents=[
        # Note: search_agent removed - now available via AgentTool to sub-agents
        requirements_discovery_agent,
        project_reality_check_agent,
        education_loop_agent,
        architecture_loop_agent,
        implementation_roadmap_agent
    ]
)

# Export for ADK
__all__ = ['root_agent']