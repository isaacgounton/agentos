# ETUGRAND AgentOS Deployment Guide

## Quick Start with Docker Compose

### 1. Copy environment file
```bash
cp .env.docker .env
```

### 2. Edit environment variables
```bash
nano .env
```
Set at minimum:
- `OPENROUTER_API_KEY=your-openrouter-api-key-here`

### 3. Start the application
```bash
docker-compose up --build
```

### 4. Access the application
- Web Interface: http://localhost:7777
- API Health: http://localhost:7777/

## Production Deployment

### Environment Variables

Required:
```bash
OPENROUTER_API_KEY=your-openrouter-api-key-here
OPENROUTER_MODEL_NAME=anthropic/claude-3-haiku
```

Optional but recommended:
```bash
# Twitter integration
X_CONSUMER_KEY=your-twitter-api-key
X_CONSUMER_SECRET=your-twitter-api-secret
X_ACCESS_TOKEN=your-twitter-access-token
X_ACCESS_TOKEN_SECRET=your-twitter-access-token-secret
X_BEARER_TOKEN=your-twitter-bearer-token

# Reddit integration
REDDIT_CLIENT_ID=your-reddit-client-id
REDDIT_CLIENT_SECRET=your-reddit-client-secret
REDDIT_USERNAME=your-reddit-username
REDDIT_PASSWORD=your-reddit-password
REDDIT_USER_AGENT=RedditTools v1.0

# Note: S3 configuration is handled by OUINHI MCP internally

# Optional: OpenAI for embeddings
OPENAI_API_KEY=your-openai-api-key-here

# Optional: PostgreSQL for persistent storage
DATABASE_URL=postgresql+psycopg://user:password@localhost:5432/agentos
```

### Docker Compose Commands

```bash
# Build and start
docker-compose up --build

# Start in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Clean build (remove images and rebuild)
docker-compose down --rmi all
docker-compose up --build
```

### Data Persistence

The Docker Compose setup includes:
- SQLite database: `./agentos.db:/app/agentos.db`
- Temporary files: `./tmp:/app/tmp`
- Downloaded files: `./downloads:/app/downloads`

### Health Checks

The container includes health checks that:
- Verify the web server is responding
- Automatically restart on failure
- Wait 40 seconds for startup before checking

### Scaling

For production, consider:
1. **Add a reverse proxy** (nginx/traefik) for SSL termination
2. **Use external database** (PostgreSQL) instead of SQLite
3. **Add monitoring** with tools like Prometheus/Grafana
4. **Set up logging** with ELK stack or similar

### Security Notes

- The container runs as a non-root user `app`
- Only port 7777 is exposed
- Environment variables should be kept secure
- Consider using Docker secrets for sensitive data

## Deployment Platforms

### Docker Swarm
```bash
docker stack deploy -c docker-compose.yml agentos
```

### Kubernetes
Use the Docker Compose file as reference to create Kubernetes manifests.

### Cloud Platforms
- **AWS ECS**: Use Fargate with the built Docker image
- **Google Cloud Run**: Container-optimized deployment
- **Azure Container Instances**: Simple container hosting

## Troubleshooting

### Common Issues
1. **Port conflicts**: Change the host port in docker-compose.yml
2. **Permission errors**: Ensure local directories exist and have correct permissions
3. **Environment variables**: Double-check .env file formatting
4. **API key issues**: Verify OpenRouter API key is valid

### Logs
```bash
# View all logs
docker-compose logs

# Follow logs
docker-compose logs -f

# View service-specific logs
docker-compose logs agentos
```

### Health Check Status
```bash
# Check container health
docker ps

# Manual health check
curl http://localhost:7777/
```

## Backup and Recovery

### Database Backup
```bash
# Copy SQLite database
cp agentos.db backup/agentos-$(date +%Y%m%d).db
```

### Configuration Backup
```bash
# Backup environment file
cp .env backup/.env-$(date +%Y%m%d)
```

### Restore
```bash
# Stop containers
docker-compose down

# Restore database
cp backup/agentos-YYYYMMDD.db agentos.db

# Restart
docker-compose up -d
```