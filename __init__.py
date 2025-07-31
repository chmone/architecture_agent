# Copyright 2025
# Architecture Assistant Agent Package
"""
A simple agent to help users think through software architecture decisions.
"""

# Import the agents submodule to ensure it's available
from . import agents

# Import root_agent from agent module
from .agent import root_agent

__all__ = ['root_agent', 'agents']