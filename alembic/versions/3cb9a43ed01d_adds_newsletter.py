"""adds newsletter

Revision ID: 3cb9a43ed01d
Revises: 1754612178ee
Create Date: 2023-09-16 21:20:04.199597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cb9a43ed01d'
down_revision = '1754612178ee'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "newsletter",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String, unique=True)
    )


def downgrade():
    op.drop_table("newsletter")
