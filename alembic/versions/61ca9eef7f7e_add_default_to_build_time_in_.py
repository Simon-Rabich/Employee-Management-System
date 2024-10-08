"""Add default to build_time in ProductVersion

Revision ID: 61ca9eef7f7e
Revises: 2908060f8be4
Create Date: 2024-09-16 18:42:10.082747

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '61ca9eef7f7e'
down_revision: Union[str, None] = '2908060f8be4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product_version', 'build_time',
               existing_type=sa.DateTime(),
               nullable=True,
               server_default=sa.func.now())  # This line should be present to reflect the default value
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product_version', 'build_time',
               existing_type=sa.DateTime(),
               nullable=True,
               server_default=None)  # This is for reverting the change in case of a downgrade
    # ### end Alembic commands ###
