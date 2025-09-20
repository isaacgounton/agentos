# Coolify Deployment Guide for AgentOS

## Prerequisites

1. **Coolify Instance**: You need a running Coolify instance
2. **Git Repository**: Your code should be in a Git repository accessible to Coolify
3. **API Keys**: Required API keys for the application

## Deployment Steps

### 1. Connect Your Repository

1. In Coolify dashboard, go to "Projects"
2. Click "Add Project" → "From Git Repository"
3. Enter your repository URL: `https://github.com/isaacgounton/agentos`
4. Select the branch (usually `main`)

### 2. Configure the Service

1. **Service Type**: Select "Docker Compose"
2. **Source**: Choose your repository
3. **Docker Compose File**: `docker-compose.yml` (should be auto-detected)

### 3. Environment Variables

Set the following environment variables in Coolify:

#### Required

- `OPENROUTER_API_KEY`: Your OpenRouter API key
- `OPENROUTER_MODEL_NAME`: `anthropic/claude-3-haiku` (or your preferred model)

#### Optional

- `OPENAI_API_KEY`: For embeddings and knowledge base features
- `DATABASE_URL`: PostgreSQL connection string (if using persistent storage)

### 4. Port Configuration

- **Internal Port**: `7777`
- **Exposed Port**: Choose a port for external access (e.g., `7777`)

### 5. Domains

1. Add a domain in Coolify
2. Point your domain's DNS to your Coolify server
3. Coolify will automatically configure SSL

### 6. Storage

If you need persistent storage for the database file:

1. Add a storage volume in Coolify
2. Mount it to `/app/agentos.db`

### 7. Deploy

1. Click "Deploy" in Coolify
2. Monitor the build logs
3. Once deployed, access your application at the configured domain

## Alternative: Manual Docker Deployment

If you prefer manual deployment:

```bash
# Clone the repository
git clone https://github.com/isaacgounton/agentos
cd agentos

# Copy environment file
cp .env.example .env
# Edit .env with your API keys

# Build and run with Docker Compose
docker-compose up -d
```

## Health Checks

The application includes health checks that monitor:

- Service availability on port 7777
- Basic API responsiveness

## Troubleshooting

### Common Issues

1. **Missing API Keys**: Ensure all required environment variables are set
2. **Port Conflicts**: Make sure port 7777 is available
3. **Memory Issues**: The application may need 2-4GB RAM depending on usage
4. **Build Failures**: Check that all dependencies in requirements.txt are available

### Logs

View logs in Coolify dashboard under your service → "Logs"

## Scaling

For production use:

- Consider using a PostgreSQL database instead of SQLite
- Add Redis for session management if needed
- Configure proper backup strategies for the database

## Security Notes

- Keep API keys secure and rotate them regularly
- Use HTTPS (automatically configured by Coolify)
- Consider adding authentication middleware for production use
