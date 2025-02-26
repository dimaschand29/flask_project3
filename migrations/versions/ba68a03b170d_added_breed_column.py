"""added breed column

Revision ID: ba68a03b170d
Revises: 
Create Date: 2020-02-15 14:55:54.800927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba68a03b170d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('puppies', sa.Column('breed', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('puppies', 'breed')
    # ### end Alembic commands ###
