# Debugging "Tool use with function calling is unsupported" Error

## Issue
Getting `google.genai.errors.ClientError: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'Tool use with function calling is unsupported'}}`

## Attempts

### 1. Initial Approach (Failed)
- Used `AgentTool` to wrap sub-agents
- This is incorrect pattern per ADK docs

### 2. Redesign with sub_agents (Failed)
- Used proper `sub_agents` parameter
- But still had `format_requirements_tool` on main agent
- Any FunctionTool seems to trigger the error

### 3. Simplified Approach (Current)
- Removed ALL tools from main agent
- Only sub-agents have tools
- Main agent delegates through natural language

## Key Learnings

1. **Don't use AgentTool for sub-agents** - Use `sub_agents` parameter
2. **Avoid FunctionTool on agents with sub_agents** - Seems to cause conflicts
3. **Keep main orchestrator agent tool-free** - Let sub-agents handle tools
4. **Delegation through instructions** - Natural language mentions of sub-agent names

## Testing

If simplified approach still fails, consider:
- Different model versions (gemini-1.5-flash?)
- Removing all tools and testing pure delegation
- Checking if it's an API key limitation