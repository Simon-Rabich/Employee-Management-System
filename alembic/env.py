from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from importlib import import_module
import pkgutil
import os

# Import your Base
from src.database.connection import Base

# this is the Alembic Config object, which provides access to values within the .ini file.
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Dynamically discover all models in the src.models folder
models_package = 'src.models'

def import_all_models(package_name):
    """Import all models from a given package."""
    package_dir = os.path.dirname(import_module(package_name).__file__)
    for _, module_name, _ in pkgutil.iter_modules([package_dir]):
        import_module(f'{package_name}.{module_name}')

# Import all models dynamically
import_all_models(models_package)

# Add your model's MetaData object here for 'autogenerate' support
target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # Ensure column type changes are detected
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
