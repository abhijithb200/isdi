"""empty message

Revision ID: ba39c8ffa596
Revises: 
Create Date: 2019-06-26 23:13:45.733097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba39c8ffa596'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients_notes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('consultant_initials', sa.String(length=100), server_default='', nullable=False),
    sa.Column('fjc', sa.Enum('Brooklyn', 'Queens', 'The Bronx', 'Manhattan', 'Staten Island'), server_default='', nullable=False),
    sa.Column('referring_professional', sa.String(length=100), server_default='', nullable=False),
    sa.Column('referring_professional_email', sa.String(length=255), nullable=True),
    sa.Column('recorded', sa.Enum('Yes', 'No'), server_default='', nullable=False),
    sa.Column('chief_concerns', sa.String(length=400), server_default='', nullable=False),
    sa.Column('chief_concerns_other', sa.String(length=400), server_default='', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clients_notes')
    # ### end Alembic commands ###