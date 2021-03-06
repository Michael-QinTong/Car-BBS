"""empty message

Revision ID: 14b5d4ff2114
Revises: d3c0f90744f6
Create Date: 2020-12-23 13:57:30.154525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14b5d4ff2114'
down_revision = 'd3c0f90744f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_shared', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_column('is_shared')

    # ### end Alembic commands ###
