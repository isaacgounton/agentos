import os
from agno.db.postgres import PostgresDb

# Database setup
db_url = os.getenv("DATABASE_URL", "postgresql+psycopg://ai:ai@localhost:5532/ai")
db = PostgresDb(db_url=db_url)