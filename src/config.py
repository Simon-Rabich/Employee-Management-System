import os

# Fetch the DATABASE_URL from the environment, or default to a local database connection
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://simonravitz:Aa123456!@localhost:5432/crmdb")
