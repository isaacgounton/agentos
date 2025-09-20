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
from agents.youtube_platform_agent import youtube_agent as youtube_platform_agent
from agents.reddit_agent import reddit_agent

# Import existing agents from agents/ directory
from agents.competitor_analysis_agent import *
from agents.media_trend_analysis_agent import *
from agents.social_media_agent import *
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
# Main AgentOS application
agent_os = AgentOS(
    os_id="etugrand-operations-manager",
    description="ETUGRAND Company Operations Manager - AI-powered business operations platform",
    agents=[
        content_agent,
        engagement_agent,
        image_agent,
        video_agent,
        audio_agent,
        publisher_scheduler_agent,
        operations_manager_agent,
        research_agent,
        analytics_agent,
        twitter_agent,
        linkedin_agent,
        youtube_platform_agent,  # Platform-specific YouTube agent
        reddit_agent,
        # Include existing agents from agents/ directory
        # Note: These will be imported via the wildcard imports above
    ],
    teams=[
        operations_team,
        platform_team,
        strategy_team,
        # Include existing teams from teams/ directory
        # Note: These will be imported via the wildcard imports above
    ],
    workflows=[
        operations_workflow,
        daily_operations_workflow,
        crisis_workflow,
        campaign_workflow,
        # Include existing workflows from workflow/ directory
        # Note: These will be imported via the wildcard imports above
    ],
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
        agent_os.serve(app="etugrand_agentos:app", port=7777)
    except KeyboardInterrupt:
        print("\n🛑 ETUGRAND Operations Manager stopped by user (Ctrl+C)")
        os._exit(0)
    except Exception as e:
        print(f"\n❌ Error starting ETUGRAND Operations Manager: {e}")
        os._exit(1)