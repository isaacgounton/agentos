from agno.agent import Agent
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools

# Optional Gemini model - fallback to OpenAI if not available
try:
    from agno.models.google.gemini import Gemini
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    from agno.models.openai import OpenAIChat
    print("⚠️  Gemini model not available - using OpenAI fallback")

# Create individual specialized agents
researcher = Agent(
    name="Researcher",
    role="Expert at finding information",
    tools=[DuckDuckGoTools()],
    model=Gemini("gemini-2.0-flash-001") if GEMINI_AVAILABLE else OpenAIChat("gpt-4o"),
)

writer = Agent(
    name="Writer",
    role="Expert at writing clear, engaging content",
    model=Gemini("gemini-2.0-flash-001") if GEMINI_AVAILABLE else OpenAIChat("gpt-4o"),
)

# Create a team with these agents
content_team = Team(
    name="Content Team",
    model=Gemini("gemini-2.5-flash") if GEMINI_AVAILABLE else OpenAIChat("gpt-4o"),
    # model=Gemini("gemini-2.0-flash-lite"),  # Try a small model for faster response
    members=[researcher, writer],
    instructions="You are a team of researchers and writers that work together to create high-quality content.",
    show_members_responses=True,
)

# Team definition only - execution handled by AgentOS
# No standalone execution allowed
