# Software Architecture Assistant Agent

A simple, focused AI agent built with Google ADK that helps developers think through software architecture decisions. The agent asks clarifying questions, researches frameworks and APIs, and provides thoughtful recommendations based on your specific needs.

## Design Philosophy

This agent follows the 12-factor agents principles:
- **Small & Focused** (Factor 10): Only handles architecture decisions, not implementation
- **Natural Language to Tools** (Factor 1): Conversational interface with structured tool outputs
- **Own Your Prompts** (Factor 2): Clear, versioned instructions for consistent behavior
- **Stateless Operations** (Factor 12): Each conversation is independent

## Features

### Phase 1 (Completed)
- ✅ Interactive architecture discussions
- ✅ Asks clarifying questions about your project
- ✅ Provides thoughtful recommendations
- ✅ Considers trade-offs and constraints

### Phase 2 (Completed)
- ✅ Web search for framework/API research
- ✅ Researches current best practices and technologies
- ✅ Verifies up-to-date information about frameworks
- ✅ Provides informed recommendations based on latest information

### Phase 3 (Current - Implemented with Proper Multi-Agent Pattern)
- ✅ **Multi-agent architecture** following ADK best practices
- ✅ **analyze_requirements_agent**: Researches and proposes architectures
- ✅ **double_check_agent**: Validates proposals against requirements
- ✅ **architecture_loop_agent**: Orchestrates iterative refinement
- ✅ Natural delegation through agent instructions (not AgentTool)
- ✅ Dynamic research using Google Search for current best practices
- ✅ Intelligent validation and feedback loop
- ✅ Model-driven delegation based on context

### Planned Features
- 🔄 Enhanced questioning templates (Phase 4)
- 🔄 Context tracking and progressive questioning (Phase 4)
- 🔄 Architecture documentation generation (Phase 5)

## Installation

1. Ensure you have Google ADK installed:
```bash
pip install google-adk
```

2. Clone or download this agent to your project

3. **Set up your API key** (REQUIRED):
   - Get a free API key from https://aistudio.google.com/apikey
   - Copy `.env.example` to `.env`
   - Add your API key to the `.env` file: `GOOGLE_API_KEY=your-actual-key`
   
   **Alternative**: Set environment variable directly:
   - Linux/Mac: `export GOOGLE_API_KEY="your-api-key"`
   - Windows: `set GOOGLE_API_KEY=your-api-key`

## Usage

### Interactive Web Interface (Recommended)
```bash
# IMPORTANT: Run from the PARENT directory, not from within architecture_assistant
cd /path/to/agent_practice  # Go to parent directory
adk web

# Or with a specific port
adk web --port 8888
```

Then open http://localhost:8000 (or your specified port) in your browser.

### Example Conversations

#### Basic Architecture Discussion
```
You: I'm building a new web application for e-commerce
Agent: I'd be happy to help you design your e-commerce application architecture! Let me ask some questions to better understand your needs:

1. What type of e-commerce platform are you building?
   - B2C marketplace
   - B2B platform
   - Single vendor store
   - Multi-vendor marketplace

2. What's your expected scale?
   - How many products?
   - Expected daily users?
   - Transaction volume?

[continues conversation...]
```

#### Agent-Based Architecture Analysis (Phase 3)
```
You: I need architecture recommendations for a web app with 50k users, 5 developers, 6 month timeline
Agent: I'll analyze your requirements using our intelligent architecture analysis system.

[Formats requirements and calls architecture_loop_agent]
[Iteration 1]
- analyze_requirements_agent researches current best practices for medium-scale web apps
- Proposes: Next.js + Kubernetes + Microservices
- double_check_agent: "Too complex for 5 developers in 6 months"

[Iteration 2]
- analyze_requirements_agent refines based on feedback
- Proposes: Next.js + Node.js API + PostgreSQL on managed cloud
- double_check_agent: "Appropriate for team size and timeline"
- Loop exits with validated architecture

Final Architecture Recommendation:
- **Pattern**: Modular Monolith (can evolve to microservices)
- **Stack**: Next.js, Node.js/Express, PostgreSQL, Redis
- **Infrastructure**: Vercel/Railway or AWS App Runner
- **Rationale**: Balances scalability with team productivity
```

#### Iterative Framework Analysis (Phase 3)
```
You: Should I use Django or FastAPI for my new API project?
Agent: Let me gather some details first...
[Asks about team experience, performance needs, timeline]

You: Team knows Python, need high performance, 3 month timeline
Agent: I'll analyze both options through our architecture loop system.

[architecture_loop_agent process]
- Researches latest Django vs FastAPI benchmarks
- Considers team Python experience
- Validates against 3-month timeline
- Iterates to find optimal recommendation

Recommendation: FastAPI
- Modern async performance for your high-performance needs
- Faster development than Django for pure APIs
- Strong Python typing helps team productivity
- Can meet 3-month timeline with automatic API documentation
```

## Project Structure
```
architecture_assistant/
├── __init__.py              # Package initialization
├── agent.py                # Main agent definition (imports from agents_redesign)
├── agents_redesign.py      # Multi-agent implementation (Phase 3)
├── test_phase2.py          # Google search capability tests
├── test_multiagent.py      # Multi-agent pattern explanation
├── PHASE3_COMPLETE.md      # Phase 3 implementation notes
├── .env.example           # API key template
└── README.md              # This file
```

## Development Roadmap

- [x] Phase 1: Basic conversational agent
- [x] Phase 2: Add web search capabilities
- [x] Phase 3: Structured analysis tools
- [ ] Phase 4: Enhanced questioning system
- [ ] Phase 5: Documentation generation

## Contributing

This is a simple example agent. Feel free to extend it with:
- Additional tools for specific architecture patterns
- Integration with diagramming tools
- Custom templates for different project types
- Memory/session support for longer conversations

## Troubleshooting

### Running ADK Web
**Important**: Run `adk web` from the parent directory (`agent_practice`), not from within `architecture_assistant`:
```bash
cd /path/to/agent_practice  # Parent directory
adk web
```

### Common Issues

1. **"503 Service Unavailable" Error**
   - This is temporary when the model is overloaded
   - Just wait a few seconds and try again
   - Consider using `gemini-1.5-flash` if it persists

2. **API Key Issues**
   - Ensure your key is in the `.env` file
   - No extra spaces or quotes around the key
   - Get your key from: https://aistudio.google.com/apikey

3. **"No agents found" Error**
   - Make sure you're running `adk web` from the parent directory
   - The directory structure should have `architecture_assistant` as a subdirectory

## License

This project is provided as an example for learning purposes.