import os
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.pgvector import PgVector

# Import database config
from .database import db

# Vector database for knowledge (using OpenAI for embeddings)
vector_db = PgVector(
    db_url=db.db_url,
    table_name="operations_knowledge",
)

# Knowledge base for business operations and strategies
knowledge = Knowledge(
    name="ETUGRAND Operations Knowledge",
    contents_db=db,
    vector_db=vector_db,
)