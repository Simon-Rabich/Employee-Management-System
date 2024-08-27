import os

<<<<<<< HEAD
# Fetch the DATABASE_URL from the environment, or default to a local database connection
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://simonravitz:Aa123456!@localhost:5432/crmdb")
=======
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://simonravitz:your_password@localhost:5432/your_database")
>>>>>>> f0ae657d6e8455067a87cef92b8ffd1a79880ab7
