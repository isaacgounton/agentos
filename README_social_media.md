# Social Media AgentOS

A proper AgentOS implementation for AI-powered social media management, following the correct AgentOS patterns.

## Features

- **Content Creation Agent**: Creates engaging, platform-optimized social media content
- **Engagement Analyst**: Analyzes performance and provides optimization recommendations
- **Content Scheduler**: Optimizes posting schedules and timing
- **Team Coordination**: Multi-agent team for comprehensive social media strategies
- **Knowledge Base**: Vector-based knowledge storage for content strategies and insights
- **MCP Integration**: Model Context Protocol support for external tools and services

## Prerequisites

1. PostgreSQL with PgVector extension
2. Python 3.8+
3. OpenRouter API key and model name (for LLM)
4. OpenAI API key (for embeddings)

## Setup

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Set up PostgreSQL:**

   ```sql
   CREATE DATABASE ai;
   CREATE EXTENSION vector;
   ```

3. **Set environment variables:**

   ```bash
   export OPENROUTER_API_KEY="your-openrouter-api-key"
   export OPENROUTER_MODEL_NAME="anthropic/claude-3-haiku"
   export OPENAI_API_KEY="your-openai-api-key"
   export DATABASE_URL="postgresql+psycopg://ai:ai@localhost:5532/ai"
   ```

## Providers Used

- **LLM**: OpenRouter with Claude-3-Haiku (configured via `OPENROUTER_API_KEY` and `OPENROUTER_MODEL_NAME`)
- **Embeddings**: OpenAI (configured via `OPENAI_API_KEY`)
- **MCP**: Pollinations for images, vision, audio, and video generation
- **Database**: PostgreSQL with PgVector extension

## Usage

### Running the AgentOS

```bash
python social_media_agentos.py
```

This will start the AgentOS server with:

- REST API endpoints
- Web playground interface
- All configured agents, teams, and workflows

### API Endpoints

- `GET /` - Health check and system info
- `POST /api/v1/agents/{agent_id}/run` - Run a specific agent
- `POST /api/v1/teams/{team_id}/run` - Run a team
- `POST /api/v1/workflows/{workflow_id}/run` - Execute a workflow

### Example Usage

```python
from social_media_agentos import content_agent, engagement_agent, social_media_team

# Create content
result = content_agent.run("Create a LinkedIn post about AI technology trends")

# Analyze engagement
analysis = engagement_agent.run("Analyze engagement for our last 10 posts")

# Run team workflow
team_result = social_media_team.run("Plan a social media campaign for Q4")
```

## Architecture

This implementation follows proper AgentOS patterns:

- **Direct Agent Usage**: Uses base `Agent` classes with configuration, not inheritance
- **Simple Configuration**: Agents configured with tools, knowledge, and instructions
- **Team Coordination**: Multiple agents working together through `Team` class
- **Workflow Orchestration**: Complex processes handled by `Workflow` class
- **Knowledge Management**: Vector-based knowledge storage and retrieval
- **MCP Integration**: External tools and services via Model Context Protocol

## Agents

### Content Creator

- Creates platform-optimized content
- Suggests hashtags and mentions
- Adapts content for different platforms
- Generates content calendars

### Engagement Analyst

- Analyzes post performance metrics
- Identifies audience behavior patterns
- Monitors competitor performance
- Provides optimization recommendations

### Content Scheduler

- Determines optimal posting times
- Creates content calendars
- Coordinates multi-platform campaigns
- Handles time zone considerations

## Workflows

### Content Creation Workflow

1. Research trending topics and audience interests
2. Create engaging content based on research
3. Schedule content for optimal timing
4. Review and publish to platforms

## MCP Tools

The system integrates with Pollinations MCP for multimedia content creation:

- **Pollinations MCP**: AI-powered generation of images, vision analysis, audio, and video content
- **Integration URL**: `https://mcp.sequa.ai/v1/pollinations/contribute`
- **Alternative Setup**: Can also use `npx @pollinations/model-context-protocol`

All agents are configured to use Pollinations MCP for:

- Generating images for social media posts
- Creating video content
- Audio content creation
- Vision analysis for content optimization

## Development

To extend this AgentOS:

1. Add new agents by creating `Agent` instances with specific tools and instructions
2. Create teams by grouping related agents
3. Build workflows for complex multi-step processes
4. Add knowledge sources to the vector database
5. Integrate additional MCP tools for new capabilities

## License

This is a demonstration of proper AgentOS usage patterns.
