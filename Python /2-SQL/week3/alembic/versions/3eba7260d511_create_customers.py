"""create customers

Revision ID: 3eba7260d511
Revises: 
Create Date: 2023-03-20 16:28:35.461264

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3eba7260d511'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE customers(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL

        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE customers;
        """
    )
