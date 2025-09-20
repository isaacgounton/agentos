#!/bin/bash
# Social Media AgentOS Environment Setup Script

echo "🚀 Setting up Social Media AgentOS Environment"
echo "=============================================="

# Check if required environment variables are set
echo ""
echo "📋 Checking environment variables..."

if [ -z "$OPENROUTER_API_KEY" ]; then
    echo "❌ OPENROUTER_API_KEY is not set"
    echo "   Please set it with: export OPENROUTER_API_KEY='your-key'"
else
    echo "✅ OPENROUTER_API_KEY is set"
fi

if [ -z "$OPENROUTER_MODEL_NAME" ]; then
    echo "⚠️  OPENROUTER_MODEL_NAME is not set, using default: anthropic/claude-3-haiku"
    export OPENROUTER_MODEL_NAME="anthropic/claude-3-haiku"
else
    echo "✅ OPENROUTER_MODEL_NAME is set to: $OPENROUTER_MODEL_NAME"
fi

if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ OPENAI_API_KEY is not set"
    echo "   Please set it with: export OPENAI_API_KEY='your-key'"
else
    echo "✅ OPENAI_API_KEY is set"
fi

if [ -z "$DATABASE_URL" ]; then
    echo "⚠️  DATABASE_URL is not set, using default PostgreSQL connection"
    export DATABASE_URL="postgresql+psycopg://ai:ai@localhost:5532/ai"
else
    echo "✅ DATABASE_URL is set"
fi

echo ""
echo "🔧 Checking Pollinations MCP..."

# Check if npx is available for alternative Pollinations setup
if command -v npx &> /dev/null; then
    echo "✅ npx is available for Pollinations MCP"
    echo "   Alternative setup: npx @pollinations/model-context-protocol"
else
    echo "⚠️  npx not found - using HTTP-based Pollinations MCP integration"
fi

echo ""
echo "📦 Checking Python dependencies..."

# Check if required packages are installed
python3 -c "
import sys
required_packages = ['agno', 'fastapi', 'uvicorn', 'sqlalchemy', 'pgvector', 'psycopg2']
missing_packages = []

for package in required_packages:
    try:
        __import__(package.replace('-', '_'))
        print(f'✅ {package}')
    except ImportError:
        print(f'❌ {package}')
        missing_packages.append(package)

if missing_packages:
    print(f'\\n⚠️  Missing packages: {missing_packages}')
    print('   Install with: pip install -r requirements.txt')
else:
    print('\\n✅ All required packages are installed')
"

echo ""
echo "🎯 Configuration Summary:"
echo "------------------------"
echo "LLM Provider: OpenRouter"
echo "LLM Model: $OPENROUTER_MODEL_NAME"
echo "Embeddings: OpenAI"
echo "MCP: Pollinations (https://mcp.sequa.ai/v1/pollinations/contribute)"
echo "Database: PostgreSQL with PgVector"

echo ""
echo "🚀 Ready to run Social Media AgentOS!"
echo "   Command: python social_media_agentos.py"
echo ""
echo "🌐 The AgentOS will be available at: http://localhost:7777"
echo "📚 API documentation at: http://localhost:7777/docs"