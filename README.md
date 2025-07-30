# Architecture Assistant - Multi-Agent System

A sophisticated software architecture assistant built using Google ADK (Agent Development Kit) with Gemini 2.0 Flash. This system helps developers make informed architecture decisions through intelligent multi-agent collaboration.

## 🎯 Key Features

- **Intelligent Architecture Analysis**: Researches and proposes optimal solutions based on your requirements
- **Iterative Refinement**: Validates and improves proposals through multi-agent collaboration
- **Current Best Practices**: Uses Google Search to find up-to-date patterns and recommendations
- **Practical Focus**: Balances ideal solutions with real-world constraints

## 🏗️ Architecture Pattern

This implementation uses a **hierarchical multi-agent pattern** that avoids common pitfalls:

```
root_agent (NO TOOLS - only sub_agents)
└── architecture_loop_agent (LoopAgent)
    ├── analyze_requirements_agent (has google_search tool)
    └── double_check_agent (has exit_loop tool)
```

### Critical Design Decision

The root agent has **NO TOOLS** to avoid the "Tool use with function calling is unsupported" error. It only delegates to sub-agents through natural language in its instructions.

## 🚀 Getting Started

1. **Set up environment**:
   ```bash
   # Create .env file with your Google API key
   echo "GOOGLE_API_KEY=your-key-here" > .env
   ```

2. **Install dependencies**:
   ```bash
   pip install google-genai-developer
   ```

3. **Run the assistant**:
   ```bash
   # From the parent directory
   adk web
   # Select 'architecture_assistant' when prompted
   ```

## 💬 Example Queries

- "I need to design a web app that will serve 50,000 daily active users"
- "Help me choose between microservices and monolith for a startup with 3 developers"
- "What's the best architecture for a real-time chat application?"
- "I have a 6-month timeline and need to build an e-commerce platform"

## 🔄 How It Works

1. **User provides requirements** → Root agent gathers key information
2. **Root agent delegates** → Mentions `architecture_loop_agent` in natural language
3. **Loop agent coordinates**:
   - `analyze_requirements_agent` researches and proposes solutions
   - `double_check_agent` validates the proposal
   - Iterates up to 3 times for refinement
4. **Final architecture** → Presented to user with clear reasoning

## 📁 Project Structure

```
architecture_assistant/
├── agent.py           # Main implementation (all agents defined here)
├── __init__.py        # Package initialization
├── README.md          # This file
└── .env              # Your Google API key (create this)
```

## 🚧 Roadmap

### Phase 1: Core Foundation ✅
- Basic multi-agent architecture
- Requirements analysis and validation
- Iterative refinement loop

### Phase 2: Enhanced Analysis (Coming Soon)
- Security architecture analysis
- Scalability evaluation
- Cost optimization recommendations

### Phase 3: Pattern Library
- Microservices patterns
- Event-driven architectures
- Data architecture patterns

### Phase 4: Technology Recommendations
- Framework selection based on requirements
- Database technology recommendations
- Infrastructure choices

### Phase 5: Documentation Generation
- Architecture Decision Records (ADRs)
- System design diagrams
- Technology comparison matrices

## 🛠️ Technical Notes

- **Framework**: Google ADK with Gemini 2.0 Flash
- **Pattern**: Hierarchical multi-agent with natural language delegation
- **Key Constraint**: Agents cannot have both tools AND sub_agents
- **Delegation**: Through mentioning agent names in instructions

## 🤝 Contributing

This project demonstrates proper multi-agent patterns with Google ADK. Feel free to explore and extend the architecture following these principles:

1. Keep root agents tool-free when using sub_agents
2. Use natural language for delegation
3. Test incrementally to avoid breaking the pattern
4. Document your architectural decisions

## 📝 License

Copyright 2025 - See individual files for details