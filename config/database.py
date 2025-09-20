import os
from agno.db.sqlite import SqliteDb

# Database setup - using SQLite for development/demo
db_file = os.getenv("DATABASE_FILE", "agentos.db")
db = SqliteDb(db_file=db_file)