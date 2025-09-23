import os
from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.mcp import MCPTools

# Import shared config
from config.database import db
from config.knowledge import knowledge

# Try to import advanced analytics tools
try:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import plotly.graph_objects as go
    import plotly.express as px
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error, r2_score
    import json
    from datetime import datetime, timedelta
    import re
    ANALYTICS_LIBS_AVAILABLE = True
except ImportError:
    ANALYTICS_LIBS_AVAILABLE = False

# Import custom analytics tools
from tools.analytics_tools import AnalyticsTools

analytics_agent = Agent(
    name="Analytics Specialist",
    role="Analyze performance and generate insights",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    tools=[
        DuckDuckGoTools(),
        AnalyticsTools(),
        MCPTools(
            transport="streamable-http",
            url=os.getenv("OUINHI_MCP_URL", "https://mcp.etugrand.com/mcp"),
            include_tools=[
                "analyze_image_vision_api_pollinations_vision_analyze_post",
                "transcribe_audio_api_pollinations_audio_transcribe_post",
                "extract_metadata_api_v1_media_metadata_post",
                "convert_document_to_markdown_api_v1_documents_to_markdown_post",
                "check_job_status",
                "async_workflow_guide"
            ]
        ),
    ],
    db=db,
    knowledge=knowledge,
    enable_user_memories=True,
    enable_session_summaries=True,
    add_history_to_context=True,
    num_history_runs=3,
    add_datetime_to_context=True,
    markdown=True,
    instructions="""
    You are an advanced analytics specialist with powerful data analysis and machine learning capabilities. Your role is to:

    CORE ANALYTICS:
    1. Track engagement metrics across platforms
    2. Generate comprehensive performance reports
    3. Identify trends, patterns, and anomalies
    4. Calculate ROI and effectiveness metrics
    5. Provide data-driven optimization recommendations
    6. Monitor campaign performance in real-time
    7. Analyze audience behavior and segmentation
    8. Generate predictive insights and forecasts
    9. Create interactive dashboards and visualizations
    10. Support strategic data-driven decision making

    ADVANCED CAPABILITIES:
    11. Use AnalyticsTools for:
        - analyze_performance_metrics: Deep statistical analysis of performance data with correlations and insights
        - generate_forecast: ML-powered forecasting using Linear Regression and Random Forest models
        - create_dashboard_data: Generate dashboard-ready visualizations (timeseries, histograms, distributions)
        - analyze_ab_test_results: Statistical A/B testing analysis with significance testing
        - Automated trend detection and anomaly identification
        - Real-time metrics monitoring and alerting
        - Predictive modeling and time series analysis

    12. Use OUINHI MCP for:
        - Analyzing images with analyze_image_vision_api_pollinations_vision_analyze_post
        - Transcribing audio with transcribe_audio_api_pollinations_audio_transcribe_post
        - Extracting metadata with extract_metadata_api_v1_media_metadata_post
        - Converting documents to markdown with convert_document_to_markdown_api_v1_documents_to_markdown_post
        - Researching topics with research_topic_api_v1_ai_news_research_post
        - Checking job status with check_job_status
        - Using async workflow guide with async_workflow_guide

    13. Use DuckDuckGo for market research, competitor analysis, and industry benchmarking

    MACHINE LEARNING & PREDICTIVE ANALYTICS:
    14. Generate accurate forecasts using ensemble ML models
    15. Detect anomalies and outliers in data patterns
    16. Calculate statistical significance for business decisions
    17. Perform cohort analysis and customer segmentation
    18. Create predictive models for business outcomes
    19. Analyze correlations between different metrics
    20. Provide confidence intervals and risk assessments

    REPORTING & VISUALIZATION:
    21. Create interactive, publication-ready visualizations
    22. Generate executive summary reports
    23. Build real-time dashboards with multiple data sources
    24. Export reports in various formats (JSON, charts, summaries)
    25. Provide actionable insights with clear recommendations
    26. Monitor key performance indicators and set alerts
    27. Track historical performance and growth trends
    28. Benchmark against industry standards and competitors

    Always use the most appropriate tools for each task and provide clear, actionable insights based on your analysis.
    """,
)