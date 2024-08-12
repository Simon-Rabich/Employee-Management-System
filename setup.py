from setuptools import setup, find_packages

setup(
    name="employee_management_system",  # This should be unique across PyPI
    version="0.1.0",
    description="A FastAPI-based Employee Management System",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/yourproject",  # Your project's URL
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "fastapi",
        "sqlalchemy",
        "psycopg2-binary",
        "uvicorn",
        "python-dotenv",
        "pydantic"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
