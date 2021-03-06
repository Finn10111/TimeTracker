"""empty message

Revision ID: 241f44970fd0
Revises: a49fac099242
Create Date: 2021-02-03 21:38:13.935686

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '241f44970fd0'
down_revision = 'a49fac099242'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('unique_task_per_user', 'task', ['name', 'user_id'])
    op.drop_index('ix_task_name', table_name='task')
    op.create_index(op.f('ix_task_name'), 'task', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_task_name'), table_name='task')
    op.create_index('ix_task_name', 'task', ['name'], unique=True)
    op.drop_constraint('unique_task_per_user', 'task', type_='unique')
    # ### end Alembic commands ###
