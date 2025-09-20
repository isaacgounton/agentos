import os
from agno.knowledge.knowledge import Knowledge

# Import database config
from .database import db

# Knowledge base for business operations and strategies
# Using SQLite database without vector database for development/demo
knowledge = Knowledge(
    name="ETUGRAND Operations Knowledge",
    contents_db=db,
    vector_db=None,  # No vector database for basic functionality
)