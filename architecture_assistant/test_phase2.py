#!/usr/bin/env python3
"""
Test script for Phase 2 - Google Search capability
This script tests the architecture assistant's ability to research frameworks and APIs
"""

import os
from dotenv import load_dotenv
from agent import root_agent

# Load environment variables
load_dotenv()

def test_search_capability():
    """Test the agent's ability to search for current information"""
    
    print("=== Testing Phase 2: Google Search Capability ===\n")
    
    # Test queries that should trigger search
    test_queries = [
        "What are the latest features in Next.js 14?",
        "Can you compare Remix vs Next.js for a new e-commerce project?",
        "What's the current state of Bun runtime vs Node.js?",
        "What are the best practices for implementing OAuth 2.0 in 2025?"
    ]
    
    for i, query in enumerate(test_queries, 1):
        print(f"\nTest {i}: {query}")
        print("-" * 50)
        
        # Note: In a real test environment, you'd use the ADK test framework
        # This is just a demonstration of what queries would trigger search
        print(f"Expected behavior: Agent should use google_search tool")
        print(f"Query type: {'Framework-specific' if 'Next.js' in query or 'Remix' in query or 'Bun' in query else 'Best practices'}")
        
    print("\n\n=== Test queries that should NOT trigger search ===\n")
    
    # Test queries that should use built-in knowledge
    no_search_queries = [
        "What's the difference between monolithic and microservices architecture?",
        "When should I use a message queue?",
        "What are the SOLID principles?",
        "How do I decide between SQL and NoSQL?"
    ]
    
    for i, query in enumerate(no_search_queries, 1):
        print(f"\nTest {i}: {query}")
        print("-" * 50)
        print(f"Expected behavior: Agent should use built-in knowledge")
        print(f"Query type: General architectural concept")

    print("\n\n=== Summary ===")
    print("Phase 2 implementation adds google_search tool to the agent.")
    print("The agent now can research current frameworks and best practices.")
    print("\nTo test interactively:")
    print("1. Run 'adk web' from the parent directory")
    print("2. Try the test queries above")
    print("3. Verify the agent uses search when appropriate")

if __name__ == "__main__":
    # Check if API key is set
    if not os.getenv("GOOGLE_API_KEY"):
        print("ERROR: GOOGLE_API_KEY not found in environment!")
        print("Please set your API key in .env file or environment variable")
        exit(1)
    
    test_search_capability()