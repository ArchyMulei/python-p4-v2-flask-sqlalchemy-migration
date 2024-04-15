"""rename department

Revision ID: f51f2e4d21b7
Revises: 6156ddeecf72
Create Date: 2024-04-15 18:24:18.278410

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f51f2e4d21b7'
down_revision = '6156ddeecf72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
