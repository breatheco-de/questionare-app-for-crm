"""empty message

Revision ID: ea8de496dd78
Revises: 
Create Date: 2020-11-09 16:15:18.207454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea8de496dd78'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('questionnaire',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=False),
    sa.Column('last_name', sa.String(length=80), nullable=False),
    sa.Column('interview_status', sa.String(length=80), nullable=False),
    sa.Column('approved_status', sa.String(length=80), nullable=True),
    sa.Column('communication_status', sa.String(length=80), nullable=True),
    sa.Column('contacted_at', sa.DateTime(), nullable=True),
    sa.Column('contact_attemps', sa.Integer(), nullable=True),
    sa.Column('agent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['agent_id'], ['agent.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('activity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('details', sa.String(length=350), nullable=False),
    sa.Column('label', sa.String(length=100), nullable=True),
    sa.Column('activity_type', sa.Enum('note', 'event'), nullable=True),
    sa.Column('contact_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['contact_id'], ['contact.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('interview',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('starting_time', sa.DateTime(), nullable=True),
    sa.Column('ending_time', sa.DateTime(), nullable=True),
    sa.Column('agent_id', sa.Integer(), nullable=False),
    sa.Column('questionnaire_id', sa.Integer(), nullable=False),
    sa.Column('contact_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=80), nullable=False),
    sa.Column('score_total', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['agent_id'], ['agent.id'], ),
    sa.ForeignKeyConstraint(['contact_id'], ['contact.id'], ),
    sa.ForeignKeyConstraint(['questionnaire_id'], ['questionnaire.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('questionnaire_id', sa.Integer(), nullable=False),
    sa.Column('interview_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['interview_id'], ['interview.id'], ),
    sa.ForeignKeyConstraint(['questionnaire_id'], ['questionnaire.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('option',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('value', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comments', sa.String(length=120), nullable=False),
    sa.Column('interview_id', sa.Integer(), nullable=False),
    sa.Column('option_id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['interview_id'], ['interview.id'], ),
    sa.ForeignKeyConstraint(['option_id'], ['option.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('answer')
    op.drop_table('option')
    op.drop_table('question')
    op.drop_table('interview')
    op.drop_table('activity')
    op.drop_table('contact')
    op.drop_table('questionnaire')
    op.drop_table('agent')
    # ### end Alembic commands ###