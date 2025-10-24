"""
A Bindu AI agent for intelligent task handling

Bindu Agent Entry Point
"""

import json
import os
from pathlib import Path
from typing import Any

from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from bindu.penguin.bindufy import bindufy


def load_config() -> dict:
    """Load agent configuration from project root."""
    # Get path to agent_config.json in project root
    project_root = Path(__file__).parent.parent
    config_path = project_root / "agent_config.json"

    with open(config_path) as f:
        return json.load(f)


# Load configuration
config = load_config()

# Check if OpenRouter key is available
openrouter_key = os.getenv("OPENROUTER_API_KEY")


# Create the agent instance
agent = Agent(
    instructions=config.get("description", "Provide helpful responses to user messages"),
    model=OpenRouter(id="gpt-4o", api_key=openrouter_key),
)


def handler(messages: list[dict[str, str]]) -> Any:
    """Handle incoming agent messages.

    Args:
        messages: List of message dicts with 'role' and 'content' keys
                  e.g., [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}]

    Returns:
        Agent response (ManifestWorker will handle extraction)
    """

    # Run agent with messages
    result = agent.run(input=messages)
    return result


if __name__ == "__main__":
    # Bindufy and start the agent server
    bindufy(agent, config, handler)
