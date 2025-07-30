# Search Delegation Pattern - Architecture Assistant

## Problem Solved

The Google ADK (Agent Development Kit) has a constraint where Gemini only supports one built-in tool (like `google_search`) at a time across the entire agent system. When multiple agents have the `google_search` tool, it causes:

```
400 INVALID_ARGUMENT: Tool use with function calling is unsupported
```

## Solution: Centralized Search Agent

We implement a dedicated `search_agent` that is the ONLY agent in the system with the `google_search` tool. All other agents delegate search requests to this central service.

## Implementation

### 1. Search Agent (The Only Agent with google_search)

```python
search_agent = Agent(
    model="gemini-2.0-flash",
    name="search_agent",
    description="Performs web searches for all other agents in the system",
    instruction=SEARCH_AGENT_PROMPT,
    tools=[google_search]  # ONLY agent with google_search tool
)
```

### 2. Other Agents Request Searches

All other agents have `tools=[]` and use natural language to request searches:

```python
# In agent prompts:
When you need to research information about:
- Similar businesses and their challenges
- Market size and growth potential
- Common failure points to avoid

Say: "I need to research [specific topic]. Let me get that information."
The system will provide search results for your analysis.
```

### 3. Root Orchestrator Handles Delegation

The root agent includes search_agent in its sub_agents and handles delegation:

```python
# In root agent prompt:
When any agent says they need to research something:
- Immediately delegate to search_agent with the specific query
- Example: If requirements_discovery_agent says "I need to research market size"
- You respond: "I'll have the search_agent look that up" and delegate
```

## Architecture Overview

```
root_agent (NO TOOLS - orchestrator only)
├── search_agent (ONLY agent with google_search tool)
├── requirements_discovery_agent (no tools - requests searches)
├── project_reality_check_agent (no tools - requests searches)
├── education_loop_agent (LoopAgent - no tools)
│   ├── tradeoff_educator_agent (has exit_loop tool only)
│   └── clarification_agent (has exit_loop tool only)
├── architecture_loop_agent (LoopAgent - no tools)
│   ├── analyze_requirements_agent (no tools - requests searches)
│   └── double_check_agent (has exit_loop tool only)
└── implementation_roadmap_agent (no tools - requests searches)
```

## Example Flow

1. User asks: "I want to build a dog walking app"
2. Root delegates to requirements_discovery_agent
3. Requirements agent says: "I need to research the market size for pet services"
4. Root sees this and delegates to search_agent
5. Search agent performs the search and returns results
6. Requirements agent continues with the information

## Key Benefits

1. **Avoids Function Calling Error**: Only one agent has google_search
2. **Centralized Search**: All searches go through one agent
3. **Natural Delegation**: Uses natural language, not function calls
4. **Maintainable**: Easy to update search behavior in one place
5. **Clear Separation**: Search functionality is isolated

## Important Notes

- The search_agent should be listed FIRST in the root agent's sub_agents
- All agent prompts must be updated to request searches, not perform them
- The root orchestrator must be trained to recognize search requests
- This pattern follows ADK's constraint that agents can have tools OR sub_agents, not both

## Testing

To verify this pattern works:
1. Run `adk web` and select the architecture_assistant
2. Ask questions that require research
3. Observe that agents request searches and get results
4. No "Tool use with function calling" errors should occur