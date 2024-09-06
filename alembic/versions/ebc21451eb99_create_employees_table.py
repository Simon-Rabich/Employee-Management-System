from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ebc21451eb99'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'employees',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('emp_id', sa.String, index=True),
        sa.Column('name', sa.String, index=True),
        sa.Column('position', sa.String, index=True),
        sa.Column('salary', sa.Numeric),
        sa.Column('creation_time', sa.DateTime(timezone=True), server_default=sa.func.now()),
        sa.Column('last_update_time', sa.DateTime(timezone=True), onupdate=sa.func.now()),
    )

def downgrade():
    op.drop_table('employees')
