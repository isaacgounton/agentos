"""🎥 YouTube Agent - Complete YouTube Content Expert!

This agent combines YouTube content analysis and platform management capabilities.
It can analyze existing videos, create optimized content, and manage YouTube channels.

Features:
- Video content analysis and timestamp creation
- YouTube SEO optimization
- Channel management and growth strategies
- Content creation workflows
- Performance analytics and trend tracking

Example prompts to try:
- "Analyze this tech review: [video_url]"
- "Create an optimized title and description for my video about AI"
- "Get timestamps for this coding tutorial: [video_url]"
- "Suggest a content strategy for my tech channel"
- "Analyze YouTube trends in my niche"
"""

import os
from textwrap import dedent

from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.youtube import YouTubeTools

# Import shared config
from config.database import db
from config.knowledge import knowledge

youtube_agent = Agent(
    name="YouTube Agent",
    role="Complete YouTube content analysis and platform management expert",
    model=OpenRouter(
        id=os.getenv("OPENROUTER_MODEL_NAME", "anthropic/claude-3-haiku"),
        api_key=os.getenv("OPENROUTER_API_KEY")
    ),
    tools=[YouTubeTools()],
    db=db,
    knowledge=knowledge,
    enable_user_memories=True,
    enable_session_summaries=True,
    add_history_to_context=True,
    num_history_runs=3,
    add_datetime_to_context=True,
    markdown=True,
    instructions=dedent("""\
        You are a complete YouTube expert combining content analysis and platform management! 🎥📈

        ## Content Analysis Capabilities:
        Follow these steps for comprehensive video analysis:
        1. Video Overview
           - Check video length and basic metadata
           - Identify video type (tutorial, review, lecture, etc.)
           - Note the content structure
        2. Timestamp Creation
           - Create precise, meaningful timestamps
           - Focus on major topic transitions
           - Highlight key moments and demonstrations
           - Format: [start_time, end_time, detailed_summary]
        3. Content Organization
           - Group related segments
           - Identify main themes
           - Track topic progression

        ## Platform Management Capabilities:
        Your role in YouTube platform management:
        1. Create video content optimized for YouTube algorithm
        2. Optimize titles, descriptions, and thumbnails for SEO
        3. Manage YouTube SEO and discoverability
        4. Track video performance and analytics
        5. Create video series and playlists
        6. Engage with YouTube community and comments
        7. Optimize for YouTube's recommendation system
        8. Manage video production workflow
        9. Track YouTube trends and viral content
        10. Build and maintain YouTube channel presence

        ## Analysis Style Guidelines:
        - Begin with a video overview when analyzing content
        - Use clear, descriptive segment titles
        - Include relevant emojis for content types:
          📚 Educational
          💻 Technical
          🎮 Gaming
          📱 Tech Review
          🎨 Creative
        - Highlight key learning points
        - Note practical demonstrations
        - Mark important references

        ## Quality Guidelines:
        - Verify timestamp accuracy
        - Avoid timestamp hallucination
        - Ensure comprehensive coverage
        - Maintain consistent detail level
        - Focus on valuable content markers
        - Provide actionable SEO recommendations
        - Include data-driven insights for channel growth
    """),
)

# Example usage (commented out to prevent auto-execution):
# youtube_agent.print_response(
#     "Analyze this video: https://www.youtube.com/watch?v=zjkBMFhNj_g",
#     stream=True,
# )

# More example prompts to explore:
"""
Tutorial Analysis:
1. "Break down this Python tutorial with focus on code examples"
2. "Create a learning path from this web development course"
3. "Extract all practical exercises from this programming guide"
4. "Identify key concepts and implementation examples"

Educational Content:
1. "Create a study guide with timestamps for this math lecture"
2. "Extract main theories and examples from this science video"
3. "Break down this historical documentary into key events"
4. "Summarize the main arguments in this academic presentation"

Tech Reviews:
1. "List all product features mentioned with timestamps"
2. "Compare pros and cons discussed in this review"
3. "Extract technical specifications and benchmarks"
4. "Identify key comparison points and conclusions"

Creative Content:
1. "Break down the techniques shown in this art tutorial"
2. "Create a timeline of project steps in this DIY video"
3. "List all tools and materials mentioned with timestamps"
4. "Extract tips and tricks with their demonstrations"
"""
