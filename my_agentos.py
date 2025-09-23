"""
ETUGRAND Company Operations Manager - AI-powered business operations platform
"""

import os
import signal
import sys
from typing import Any
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from agno.os import AgentOS

# Import all agents
from agents.content_agent import content_agent
from agents.engagement_agent import engagement_agent
from agents.publisher_scheduler_agent import publisher_scheduler_agent
from agents.image_agent import image_agent
from agents.video_agent import video_agent
from agents.audio_agent import audio_agent
from agents.operations_manager_agent import operations_manager_agent
from agents.research_agent import research_agent
from agents.analytics_agent import analytics_agent
from agents.twitter_agent import twitter_agent
from agents.linkedin_agent import linkedin_agent
from agents.youtube_agent import youtube_agent as youtube_platform_agent
from agents.reddit_agent import reddit_agent
from agents.s3_agent import s3_agent

# Import existing agents from agents/ directory
from agents.competitor_analysis_agent import *
from agents.media_trend_analysis_agent import *
from agents.startup_idea_validator import *
from agents.web_extraction_agent import *
from agents.web_search import *
from agents.youtube_agent import *  # This is the existing YouTube agent

# Import all teams
from teams.operations_team import operations_team
from teams.platform_team import platform_team
from teams.strategy_team import strategy_team

# Import existing teams from teams/ directory
from teams.ai_customer_support_team import *
from teams.autonomous_startup_team import *
from teams.content_team import *
from teams.news_agency_team import *

# Import all workflows
from workflow.operations_workflow import operations_workflow
from workflow.daily_operations_workflow import daily_operations_workflow
from workflow.crisis_workflow import crisis_workflow
from workflow.campaign_workflow import campaign_workflow

# Import existing workflows from workflow/ directory
from workflow.blog_post_generator import *
from workflow.research_agent import *
# from workflow.research_workflow import *

def initialize_knowledge_base():
    """Initialize knowledge base with content loading if embeddings are available."""
    try:
        # Try to import sentence transformers to check if embeddings are available
        import sentence_transformers
        embeddings_available = True
        print("✅ Sentence transformers available - knowledge base will include semantic search")
    except ImportError:
        embeddings_available = False
        print("⚠️  Sentence transformers not available - knowledge base disabled")

    if embeddings_available:
        try:
            # Import shared knowledge and load content
            from config.knowledge import knowledge
            from agno.knowledge.reader.website_reader import WebsiteReader

            print("📚 Loading knowledge base content...")
            knowledge.add_content(
                url="https://etugrand.com",
                reader=WebsiteReader(max_links=10),
            )
            print("✅ Knowledge base content loaded successfully")
        except Exception as e:
            print(f"⚠️  Failed to load knowledge content: {e}")
            print("   Continuing without knowledge content...")
    else:
        print("📚 Skipping knowledge content loading (no embeddings available)")

# Initialize knowledge base conditionally
initialize_knowledge_base()

def collect_all_agents():
    """Collect all agent objects from the global namespace."""
    import sys
    from agno.agent import Agent
    agents = []

    # Add explicitly imported agents
    explicit_agents = [
        content_agent, engagement_agent, image_agent, video_agent, audio_agent,
        publisher_scheduler_agent, operations_manager_agent, research_agent,
        analytics_agent, twitter_agent, linkedin_agent, youtube_platform_agent, reddit_agent, s3_agent
    ]
    agents.extend(explicit_agents)

    # Collect agents from wildcard imports by checking global namespace
    current_module = sys.modules[__name__]
    for attr_name in dir(current_module):
        if not attr_name.startswith('_'):
            attr = getattr(current_module, attr_name)
            # Check if it's an Agent instance (proper type checking)
            if (isinstance(attr, Agent) and
                attr not in agents and
                attr not in [content_agent, engagement_agent, image_agent,
                video_agent, audio_agent, publisher_scheduler_agent, operations_manager_agent,
                research_agent, analytics_agent, twitter_agent, linkedin_agent, youtube_platform_agent, reddit_agent, s3_agent]):
                agents.append(attr)

    return agents

def collect_all_teams():
    """Collect all team objects from the global namespace."""
    import sys
    teams = []

    # Add explicitly imported teams
    explicit_teams = [operations_team, platform_team, strategy_team]
    teams.extend(explicit_teams)

    # Collect teams from wildcard imports by checking global namespace
    current_module = sys.modules[__name__]
    for attr_name in dir(current_module):
        if not attr_name.startswith('_'):
            attr = getattr(current_module, attr_name)
            # Check if it's a Team instance
            if (hasattr(attr, 'name') and hasattr(attr, 'members') and hasattr(attr, 'model') and
                hasattr(attr, 'instructions') and attr not in teams and
                attr not in [operations_team, platform_team, strategy_team]):
                teams.append(attr)

    return teams

def collect_all_workflows():
    """Collect all workflow objects from the global namespace."""
    import sys
    workflows = []

    # Add explicitly imported workflows
    explicit_workflows = [operations_workflow, daily_operations_workflow, crisis_workflow, campaign_workflow]
    workflows.extend(explicit_workflows)

    # Collect workflows from wildcard imports by checking global namespace
    current_module = sys.modules[__name__]
    for attr_name in dir(current_module):
        if not attr_name.startswith('_'):
            attr = getattr(current_module, attr_name)
            # Check if it's a Workflow instance
            if (hasattr(attr, 'name') and hasattr(attr, 'description') and hasattr(attr, 'steps') and
                attr not in workflows and attr not in [operations_workflow, daily_operations_workflow,
                crisis_workflow, campaign_workflow]):
                workflows.append(attr)

    return workflows

# Collect all available agents, teams, and workflows
all_agents = collect_all_agents()
all_teams = collect_all_teams()
all_workflows = collect_all_workflows()

print(f"📊 Registered {len(all_agents)} agents, {len(all_teams)} teams, {len(all_workflows)} workflows")

# Main AgentOS application
agent_os = AgentOS(
    os_id="etugrand-operations-manager",
    description="ETUGRAND Company Operations Manager - AI-powered business operations platform",
    agents=all_agents,
    teams=all_teams,
    workflows=all_workflows,
    enable_mcp=True,  # Enable MCP server at /mcp endpoint
)

# Get the FastAPI app
app = agent_os.get_app()

def signal_handler(signum: int, frame: Any) -> None:
    """Handle shutdown signals gracefully"""
    print("\n🛑 Received shutdown signal. Stopping ETUGRAND Operations Manager...")
    print("Cleaning up connections...")
    # Force exit to avoid MCP cleanup issues
    os._exit(0)

if __name__ == "__main__":
    # Register signal handlers for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    try:
        print("🚀 Starting ETUGRAND Company Operations Manager...")
        agent_os.serve(app="my_agentos:app", port=7777)
    except KeyboardInterrupt:
        print("\n🛑 ETUGRAND Operations Manager stopped by user (Ctrl+C)")
        os._exit(0)
    except Exception as e:
        print(f"\n❌ Error starting ETUGRAND Operations Manager: {e}")
        os._exit(1)