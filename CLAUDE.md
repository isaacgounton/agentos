# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

ETUGRAND AgentOS is a comprehensive AI-powered operations management system built on the Agno AgentOS framework. It provides 32 specialized agents, 7 collaborative teams, and 7 advanced workflows for enterprise-grade AI automation.

## Key Commands

### Development
```bash
# Start the application
python my_agentos.py

# Install dependencies
pip install -r requirements.txt

# Run with Docker
docker-compose up --build

# Build Docker image
docker build -t agentos .
```

### Environment Setup
```bash
# Copy environment template
cp .env.example .env

# Required environment variables
export OPENROUTER_API_KEY="your-openrouter-api-key"
export OPENROUTER_MODEL_NAME="anthropic/claude-3-haiku"

# Optional features
export OPENAI_API_KEY="your-openai-api-key"  # For embeddings
export DATABASE_URL="postgresql://..."       # For persistent storage

# X/Twitter API (for Twitter agent functionality)
export X_CONSUMER_KEY="your-twitter-api-key"
export X_CONSUMER_SECRET="your-twitter-api-secret"
export X_ACCESS_TOKEN="your-twitter-access-token"
export X_ACCESS_TOKEN_SECRET="your-twitter-access-token-secret"
export X_BEARER_TOKEN="your-twitter-bearer-token"
```

## Architecture

### Core Framework
- **AgentOS**: Built on Agno AgentOS framework
- **Web Framework**: FastAPI with Uvicorn server
- **Database**: SQLite for development, PostgreSQL with PgVector for production
- **Knowledge Base**: Optional vector-based semantic search (requires sentence-transformers)

### Entry Point
- `my_agentos.py`: Main application entry point that:
  - Imports all agents, teams, and workflows
  - Initializes knowledge base conditionally
  - Collects and registers all components
  - Starts FastAPI server on port 7777

### Agent Structure
Located in `agents/` directory:
- Each agent extends `agno.agent.Agent`
- Uses OpenRouter models with configurable API keys
- Integrates MCP tools (Model Context Protocol)
- Shared database and knowledge base from `config/`

### Team Structure
Located in `teams/` directory:
- Teams coordinate multiple agents
- Uses `agno.team.Team` framework
- Shared database configuration
- Collaborative workflows with delegation

### Workflow Structure
Located in `workflow/` directory:
- Complex multi-step processes
- Built on Agno workflow framework
- Orchestrates agent collaboration

### Configuration
- `config/database.py`: SQLite/PostgreSQL setup
- `config/knowledge.py`: Knowledge base configuration
- `.env`: Environment variables (see .env.example for template)

## Key Components

### OUINHI MCP Integration
Most agents integrate with OUINHI MCP tools:
- Content generation scripts
- Media search and download
- Document processing
- Async workflow management

### Database Usage
- SQLite for development (`agentos.db`)
- PostgreSQL support for production
- Knowledge base stores content and embeddings (when available)

### Agent Types
1. **Content Creation**: Blog, social media, technical documentation
2. **Research & Analytics**: Web research, data analysis, market intelligence
3. **Media Processing**: Image, video, audio generation and processing
4. **Platform Integration**: Twitter, LinkedIn, YouTube, Reddit
5. **Business Operations**: Customer support, sales, financial analysis

### Team Types
1. **Operations Team**: Core business operations
2. **Strategy Team**: Business planning and execution
3. **Platform Team**: Multi-platform coordination
4. **Content Team**: Collaborative content creation
5. **Customer Support Team**: Multi-agent service
6. **Startup Team**: Business planning and validation
7. **News Agency Team**: News gathering and publishing

## Development Patterns

### Adding New Agents
1. Create in `agents/` directory
2. Use existing agent patterns as template
3. Import shared config: `from config.database import db` and `from config.knowledge import knowledge`
4. Add to `my_agentos.py` imports
5. Agent will be auto-collected by `collect_all_agents()`

### Adding New Teams
1. Create in `teams/` directory
2. Import required agents
3. Use `agno.team.Team` framework
4. Add to `my_agentos.py` imports
5. Team will be auto-collected by `collect_all_teams()`

### Adding New Workflows
1. Create in `workflow/` directory
2. Use Agno workflow framework
3. Add to `my_agentos.py` imports
4. Workflow will be auto-collected by `collect_all_workflows()`

## API Endpoints

The application provides a FastAPI server with:
- `/` - System health and configuration
- `/agents` - List all available agents
- `/teams` - List all available teams
- `/workflows` - List all available workflows
- `/api/v1/agents/{agent_id}/run` - Execute specific agent
- `/api/v1/teams/{team_id}/run` - Execute team workflow
- `/api/v1/workflows/{workflow_id}/run` - Execute workflow

## Dependencies

### Core
- `agno`: AgentOS framework
- `fastapi[standard]`: Web framework
- `uvicorn`: ASGI server
- `openai`: For embeddings and models

### Database & Storage
- `sqlalchemy`: ORM
- `pgvector`: Vector database operations
- `psycopg2-binary`: PostgreSQL driver
- `chonkie`: Text chunking

### MCP & Tools
- `mcp`: Model Context Protocol
- `firecrawl-py`: Web scraping
- `youtube-transcript-api`: YouTube content
- `tweepy`: Twitter integration
- Various search and research tools

## Important Notes

- The application uses wildcard imports for agents, teams, and workflows
- Components are auto-collected from global namespace
- Knowledge base initialization is conditional on `sentence-transformers` availability
- SQLite is used by default, PostgreSQL with PgVector for production knowledge base
- All agents share the same database and knowledge base instances
- MCP tools are configured with environment variables for API endpoints