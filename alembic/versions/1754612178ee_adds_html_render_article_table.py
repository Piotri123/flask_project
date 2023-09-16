"""adds html render article table

Revision ID: 1754612178ee
Revises: fd204cf6d182
Create Date: 2023-09-16 20:47:42.500836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1754612178ee'
down_revision = 'fd204cf6d182'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("article",
                  sa.Column("html_render", sa.String, server_default=""))


def downgrade():
    op.drop_column("article", "html_render")
