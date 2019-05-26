"""empty message

Revision ID: 5100f68ca1ee
Revises: 
Create Date: 2019-05-19 19:28:17.660885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5100f68ca1ee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('juice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('recipe', sa.String(length=254), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('store',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('open_h', sa.Integer(), nullable=True),
    sa.Column('close_h', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('store')
    op.drop_table('juice')
    # ### end Alembic commands ###