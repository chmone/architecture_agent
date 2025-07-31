# Copyright 2025
# Architecture Assistant - Search Agent Module
#
# CRITICAL: Only ONE agent in the entire system can have google_search tool
# This module provides the centralized search service for all other agents

from google.adk import Agent
from google.adk.tools import google_search, AgentTool

# ===== SHARED SEARCH AGENT =====
# CRITICAL: Only ONE agent in the system can have google_search tool
# All other agents must request searches through this agent

SEARCH_AGENT_PROMPT = """You are a research assistant that performs web searches for other agents.

When asked to search for information:
1. Use Google Search to find relevant, current information
2. Focus on the specific query requested
3. Summarize key findings clearly
4. Provide sources when relevant

Return concise, factual results that directly answer the search request.
"""

search_agent = Agent(
    model="gemini-2.0-flash",
    name="search_agent",
    description="Performs web searches for all other agents in the system",
    instruction=SEARCH_AGENT_PROMPT,
    tools=[google_search]  # ONLY agent with google_search tool
)

# Create AgentTool from search_agent for other agents to use
search_agent_tool = AgentTool(agent=search_agent)

__all__ = ['search_agent', 'search_agent_tool']