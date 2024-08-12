import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://simonravitz:your_password@localhost:5432/your_database")
