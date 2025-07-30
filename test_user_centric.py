#!/usr/bin/env python3
"""
Test script for the user-centric Architecture Assistant
Demonstrates the educational, conversational approach
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def show_user_journey():
    """Shows example user interactions with the new system"""
    
    print("=== Architecture Assistant - User-Centric Experience ===\n")
    
    print("🎯 WHO IT'S FOR:")
    print("   • Entrepreneurs with ideas but no technical background")
    print("   • Business owners looking to digitize")
    print("   • Anyone who's said 'I have an app idea but...'\n")
    
    print("🤝 HOW IT WORKS:")
    print("   1. Discovery: We explore your idea together")
    print("   2. Education: Learn concepts with simple analogies") 
    print("   3. Reality Check: Honest assessment with solutions")
    print("   4. Planning: Clear roadmap you can follow")
    print("   5. Confidence: Know exactly what to do next\n")
    
    print("💬 EXAMPLE CONVERSATIONS:\n")
    
    print("Example 1: The Dog Walking App")
    print("-" * 50)
    print("User: 'I want to build an app like Uber for dog walking'")
    print("\nAssistant: 'That's a great idea! I love how you're thinking about")
    print("making pet care more convenient. Let me help you explore what you")
    print("really need to make this successful.'")
    print("\n[Discovery Agent explores the business model, users, problems...]")
    print("[Reality Check Agent assesses feasibility and challenges...]")
    print("[Roadmap Agent creates actionable plan...]\n")
    
    print("Example 2: Understanding Technology")
    print("-" * 50)
    print("User: 'Should I use microservices?'")
    print("\nAssistant: 'Great question! Let me explain what that really means")
    print("for your project. Think of it like choosing between living in a")
    print("single house vs an apartment complex...'")
    print("\n[Education Agent explains with analogies and business impact...]\n")
    
    print("Example 3: Budget Reality")
    print("-" * 50)
    print("User: 'Can I build this for $10,000?'")
    print("\nAssistant: 'Let's get realistic about the investment needed. I'll")
    print("analyze similar projects and give you honest numbers with options")
    print("for different budget levels.'")
    print("\n[Reality Check Agent provides real data and alternatives...]\n")
    
    print("📦 WHAT YOU GET:")
    print("   ✓ Clear understanding of your project")
    print("   ✓ Technology choices explained simply")
    print("   ✓ Realistic timeline and budget")
    print("   ✓ Step-by-step implementation plan")
    print("   ✓ Confidence to talk to developers\n")
    
    print("🚀 READY TO START?")
    print("   Run 'adk web' and select 'architecture_assistant'")
    print("   Then just start talking about your idea!\n")
    
    print("💡 REMEMBER:")
    print("   • No technical knowledge required")
    print("   • No stupid questions")
    print("   • Focus on YOUR success")
    print("   • We explain everything clearly\n")

if __name__ == "__main__":
    # Check if API key is set
    if not os.getenv("GOOGLE_API_KEY"):
        print("❌ ERROR: GOOGLE_API_KEY not found!")
        print("Please set your API key in .env file:")
        print("echo 'GOOGLE_API_KEY=your-key-here' > .env")
        exit(1)
    
    show_user_journey()
    
    print("✅ Ready to help non-technical users build their dreams!")