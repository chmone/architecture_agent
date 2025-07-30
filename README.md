# Architecture Assistant - Your Technical Co-Founder

A friendly AI assistant that helps non-technical founders and entrepreneurs turn their ideas into actionable technical plans. Built with Google ADK and Gemini 2.0 Flash, it focuses on education and empowerment rather than technical jargon.

## 🎯 What It Does

- **Discovers Your Real Needs**: Through conversation, uncovers requirements you didn't know you had
- **Explains Technical Choices**: Uses everyday analogies to help you understand complex decisions
- **Provides Reality Checks**: Honest assessment of challenges with practical solutions
- **Creates Action Plans**: Step-by-step roadmaps you can actually follow
- **Builds Your Confidence**: Empowers you to talk to developers and make informed decisions

## 🤝 How It Works

Think of it as having a conversation with a knowledgeable friend who:
1. **Listens** to understand your vision
2. **Asks smart questions** to uncover what you really need
3. **Explains options** in terms you understand
4. **Gives honest advice** about challenges and solutions
5. **Creates a roadmap** you can actually follow

## 👥 Perfect For

- **Entrepreneurs** with an idea but no technical background
- **Product Managers** who need to understand architecture
- **Business Owners** looking to digitize their operations
- **Anyone** who's ever said "I have an app idea but..."

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

## 💬 Example Conversations

**Starting Fresh:**
- "I want to build an app like Uber but for dog walking"
- "I have an idea for helping restaurants reduce food waste"
- "I need to modernize my business but don't know where to start"

**Getting Clarity:**
- "What do you mean by 'cloud'? Where does my app actually live?"
- "Should I build a mobile app or web app first?"
- "How do I know if my idea is technically feasible?"

**Making Decisions:**
- "What's the real difference between hiring freelancers vs an agency?"
- "How much should I budget for building an MVP?"
- "When do I need to worry about things like 'scaling'?"

## 🛠️ Your Journey

1. **Discovery Phase** → We explore your idea together through conversation
2. **Reality Check** → Honest assessment of what's involved (time, money, complexity)
3. **Education** → Learn key concepts with everyday analogies (no jargon!)
4. **Planning** → Get a step-by-step roadmap with clear milestones
5. **Confidence** → Leave knowing exactly what to do next

## 📁 Project Structure

```
architecture_assistant/
├── agent.py           # Main implementation (all agents defined here)
├── __init__.py        # Package initialization
├── README.md          # This file
└── .env              # Your Google API key (create this)
```

## 📈 What You'll Get

After working with the Architecture Assistant, you'll receive:

1. **Clear Understanding** of what you're building and why
2. **Technology Recommendations** explained in plain English  
3. **Realistic Timeline & Budget** based on similar projects
4. **Step-by-Step Roadmap** with specific milestones
5. **Risk Assessment** with practical solutions
6. **Hiring Guide** for finding the right developers
7. **Glossary** of terms you'll need to know
8. **Confidence** to move forward with your project

## 🚧 Evolution

### Current: User-Centric Foundation ✅
- Socratic discovery process
- Plain-language explanations
- Reality-based planning
- Educational approach

### Coming Soon: Enhanced Features
- Visual architecture diagrams
- Cost calculator with real estimates
- Team-building assistant
- Progress tracking
- Direct developer matchmaking

## 🌟 Our Philosophy

**We believe that:**
- Everyone with a good idea deserves to build it
- Technical decisions shouldn't require a CS degree
- Understanding > Implementation
- Empowerment > Dependency
- Honesty > Hype

## 🛠️ Technical Implementation

For developers interested in the implementation:
- Built with Google ADK (Agent Development Kit)
- Uses Gemini 2.0 Flash for natural conversation
- Multi-agent architecture with specialized roles
- NO TOOLS on parent agents (avoids function calling conflicts)
- Natural language delegation between agents

## 🤝 Feedback & Support

We're constantly improving based on user feedback. If you:
- Get confused by something → We'll make it clearer
- Need a feature → We'll consider adding it
- Have a success story → We'd love to hear it!

Remember: There are no "stupid questions" - if you're wondering about something, ask!

## 📝 License

Copyright 2025 - See individual files for details