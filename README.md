# ETUGRAND AgentOS

A comprehensive AI-powered operations management system built with AgentOS, featuring multi-agent teams, advanced workflows, and extensive tool integrations for enterprise-grade AI automation.

**Repository**: [https://github.com/isaacgounton/agentos](https://github.com/isaacgounton/agentos)

## 🚀 Features

### Core Capabilities

- **32 Specialized Agents** - Content creation, analytics, research, social media management, and more
- **7 Collaborative Teams** - CEO operations, customer support, content creation, and business teams
- **7 Advanced Workflows** - Blog generation, research automation, and complex business processes
- **Knowledge Base** - Vector-based semantic search (optional - requires sentence-transformers)
- **MCP Integration** - Model Context Protocol support for external AI tools and services

### Agent Categories

- **Content & Media**: Content creation, image/video generation, audio processing
- **Research & Analytics**: Web research, data analysis, market intelligence
- **Social Media**: Platform management, engagement analysis, scheduling
- **Business Operations**: Customer support, sales, financial analysis, legal compliance
- **Development**: Code generation, documentation, technical writing

### Tool Integrations

- **AI Models**: OpenRouter (Claude, GPT-4), OpenAI embeddings
- **Media Processing**: Pollinations MCP (images, video, audio, vision analysis)
- **Web Tools**: Firecrawl, YouTube transcripts, web search
- **Social Platforms**: Twitter/X, LinkedIn, Reddit integration
- **Business Tools**: Financial data, news aggregation, document processing

## 📋 Prerequisites

- **Python 3.12+**
- **Virtual Environment** (recommended)
- **API Keys**:
  - OpenRouter API key (for LLM models)
  - OpenAI API key (for embeddings - optional)
- **Optional Dependencies**:
  - PostgreSQL with PgVector (for persistent knowledge base)
  - Sentence-transformers (for semantic embeddings)

## 🛠️ Installation

### 1. Clone and Setup

```bash
git clone <repository-url>
cd agentos
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file or set environment variables:

```bash
# Required
export OPENROUTER_API_KEY="your-openrouter-api-key"
export OPENROUTER_MODEL_NAME="anthropic/claude-3-haiku"

# Optional (for embeddings and knowledge base)
export OPENAI_API_KEY="your-openai-api-key"
export DATABASE_URL="postgresql+psycopg://user:pass@localhost:5432/agentos"
```

## 🚀 Usage

### Start the AgentOS Server

```bash
python etugrand_agentos.py
```

The server will start on `http://localhost:7777` with:

- **REST API** - Programmatic access to all agents and workflows
- **Web Interface** - Interactive playground for testing agents
- **WebSocket Support** - Real-time workflow execution
- **Security Enabled** - Authentication and authorization

### API Endpoints

#### Core Endpoints

- `GET /` - System health and configuration
- `GET /agents` - List all available agents
- `GET /teams` - List all available teams
- `GET /workflows` - List all available workflows

#### Agent Operations

- `POST /api/v1/agents/{agent_id}/run` - Execute specific agent
- `POST /api/v1/teams/{team_id}/run` - Execute team workflow
- `POST /api/v1/workflows/{workflow_id}/run` - Execute workflow

#### Knowledge Base (when enabled)

- `GET /knowledge/content` - Search knowledge base
- `POST /knowledge/content` - Add content to knowledge base
- `GET /knowledge/config` - Knowledge base configuration

### Python Usage Example

```python
from etugrand_agentos import (
    content_agent, research_agent, analytics_agent,
    autonomous_startup_team, content_team
)

# Run individual agents
content = content_agent.run("Create a blog post about AI trends")
research = research_agent.run("Research quantum computing applications")
analysis = analytics_agent.run("Analyze market trends for renewable energy")

# Execute team workflows
startup_plan = autonomous_startup_team.run("Create a business plan for a fintech startup")
content_strategy = content_team.run("Develop a content marketing strategy")
```

## 🏗️ Architecture

### AgentOS Framework

Built on the Agno AgentOS framework with proper patterns:

- **Direct Agent Configuration** - No inheritance, clean tool-based configuration
- **Team Coordination** - Multi-agent collaboration with delegation
- **Workflow Orchestration** - Complex multi-step process automation
- **Knowledge Integration** - Vector-based semantic search and retrieval
- **MCP Tool Ecosystem** - External AI service integration

### Project Structure

```
agentos/
├── etugrand_agentos.py      # Main application entry point
├── agents/                  # 32 specialized agents
├── teams/                   # 7 collaborative teams
├── workflow/               # 7 advanced workflows
├── config/                 # Knowledge base and configuration
├── venv/                   # Python virtual environment
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

### Key Components

#### Agents (32 total)

- **Content Agents**: Blog writing, social media, technical documentation
- **Research Agents**: Web research, data analysis, academic research
- **Media Agents**: Image generation, video editing, audio processing
- **Business Agents**: Sales, marketing, customer support, financial analysis
- **Platform Agents**: Twitter, LinkedIn, YouTube, Reddit integration

#### Teams (7 total)

- **CEO Operations Team** - Executive decision making and strategy
- **Customer Support Team** - Multi-agent customer service
- **Content Creation Team** - Collaborative content production
- **Autonomous Startup Team** - Business planning and execution
- **News Agency Team** - News gathering and publishing
- **Financial Analysis Team** - Investment research and analysis

#### Workflows (7 total)

- **Blog Post Generator** - Complete blog creation pipeline
- **Research Workflows** - Automated research and analysis
- **Business Process Automation** - Complex business workflows

## 🔧 Configuration

### Environment Variables

```bash
# AI Model Configuration
OPENROUTER_API_KEY=your_key_here
OPENROUTER_MODEL_NAME=anthropic/claude-3-haiku

# Optional Features
OPENAI_API_KEY=your_key_here          # For embeddings
DATABASE_URL=postgresql://...         # For persistent storage

# Development
DEBUG=true                            # Enable debug logging
LOG_LEVEL=INFO                        # Logging verbosity
```

### Knowledge Base Setup (Optional)

For semantic search capabilities:

1. **Install sentence-transformers**:

   ```bash
   pip install sentence-transformers
   ```

2. **Set up PostgreSQL with PgVector**:

   ```sql
   CREATE DATABASE agentos;
   CREATE EXTENSION vector;
   ```

3. **Configure database connection** in environment variables

## 🛠️ Development

### Adding New Agents

```python
from agno.agent import Agent
from agno.tools import Tool

new_agent = Agent(
    name="My Agent",
    role="Specialized assistant",
    instructions="How to perform tasks",
    tools=[custom_tool],
    model=openrouter_model
)
```

### Creating Teams

```python
from agno.team import Team

my_team = Team(
    name="My Team",
    mode="collaborate",
    members=[agent1, agent2, agent3]
)
```

### Building Workflows

```python
from agno.workflow import Workflow

workflow = Workflow(
    name="My Workflow",
    steps=[step1, step2, step3]
)
```

## 📊 Monitoring & Logs

The application provides comprehensive logging:

- **Agent Execution** - Individual agent runs and results
- **Team Coordination** - Inter-agent communication and delegation
- **Workflow Progress** - Step-by-step execution tracking
- **MCP Tool Usage** - External service integration logs
- **Knowledge Base** - Content indexing and search operations

## 🔒 Security

- **API Authentication** - Secure access to all endpoints
- **Environment Variables** - Sensitive data protection
- **Input Validation** - Safe agent prompt handling
- **Rate Limiting** - API usage protection

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add agents, teams, or workflows following the established patterns
4. Test thoroughly with the AgentOS playground
5. Submit a pull request

## 📄 License

This project demonstrates advanced AgentOS implementation patterns for enterprise AI automation.

## 🙏 Acknowledgments

- **[Agno Framework](https://github.com/agno-agi/agno)** - AgentOS foundation
- **OpenRouter** - AI model access
- **Pollinations** - MCP tool ecosystem
- **OpenAI** - Embedding services
- **Community Contributors** - Agent and workflow implementations

---

**Built with ❤️ using AgentOS**
