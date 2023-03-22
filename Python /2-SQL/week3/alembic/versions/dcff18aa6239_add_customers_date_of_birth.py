"""add customers date_of_birth 

Revision ID: dcff18aa6239
Revises: 3eba7260d511
Create Date: 2023-03-20 16:41:48.378027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcff18aa6239'
down_revision = '3eba7260d511'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ADD COLUMN date_of_birth TIMESTAMP ;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers 
        DROP COLUMN date_of_birth;
        """
    )
