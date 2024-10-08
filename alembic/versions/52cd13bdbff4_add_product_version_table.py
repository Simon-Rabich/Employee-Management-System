"""Add product_version table

Revision ID: 52cd13bdbff4
Revises: 73dc31a46693
Create Date: 2024-09-20 11:55:06.326267

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '52cd13bdbff4'
down_revision: Union[str, None] = '73dc31a46693'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bridge',
    sa.Column('environment', sa.String(), nullable=False),
    sa.Column('version', sa.String(), nullable=True),
    sa.Column('build_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('environment')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bridge')
    # ### end Alembic commands ###
