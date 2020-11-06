"""empty message

Revision ID: c4f382ffc9e4
Revises: e2c279ca17c0
Create Date: 2020-11-04 00:46:45.015137

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c4f382ffc9e4'
down_revision = 'e2c279ca17c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contact', sa.Column('communication_status', sa.Enum('no answer', 'answered but not available', 'not interested any more'), nullable=True))
    op.drop_column('question', 'score_max')
    op.drop_column('question', 'score_min')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('score_min', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('question', sa.Column('score_max', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('contact', 'communication_status')
    # ### end Alembic commands ###