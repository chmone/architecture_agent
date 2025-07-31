# Agent Exit Criteria Quick Reference

## Requirements Discovery Agent
**Job**: Discover requirements ONLY  
**Done When**: User says "That's exactly right" / "Perfect" / "You've got it"  
**Never**: Design solutions, recommend tech, estimate costs  
**Handoff**: "Your vision is now clearly documented. Let me hand you back..."

## Project Reality Check Agent  
**Job**: Assess feasibility ONLY  
**Done When**: User says "I understand" / "Makes sense" / "Got it"  
**Never**: Start implementing, write code, design architecture  
**Handoff**: "You now have a realistic understanding. Let me hand you back..."

## Trade-off Educator Agent
**Job**: Explain concepts ONLY  
**Done When**: User says "I understand now" / "Clear" / "Thanks"  
**Never**: Make decisions, implement, write code  
**Exit**: Calls exit_loop() when user understands

## Implementation Roadmap Agent
**Job**: Create roadmap ONLY  
**Done When**: User says "Looks good" / "Perfect plan" / "I can work with this"  
**Never**: Start implementing, write code, execute plan  
**Handoff**: "You now have a clear, phased plan. Let me hand you back..."

## Architecture Analyzer Agent  
**Job**: Design architecture ONLY  
**Done When**: Design complete for validation  
**Never**: Implement code, write specs, build components  
**Note**: Works within loop, waits for validation

## Orchestrator Rules

### When Delegating
Always say: "They'll ONLY [specific job], then hand back to me."

### When Agent Completes
1. Recognize handoff message (contains "hand you back")
2. Take control immediately  
3. Thank agent and summarize
4. Ask user for feedback
5. Offer next steps

### Example Delegation
"I'll have the reality check agent assess feasibility. They'll ONLY analyze challenges, not start building."

### Example Handoff Response
Agent: "[Handoff message]"  
You: "Thank you! [Summary]. [User], does this work for you? Would you like to [next step]?"