"""Create users table

Revision ID: fd204cf6d182
Revises: 
Create Date: 2023-09-14 16:32:01.966296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd204cf6d182'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String),
        sa.Column("password", sa.String))


def downgrade():
    op.drop_table("users")
