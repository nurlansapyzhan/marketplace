"""address_update

Revision ID: 7f98a4febfd9
Revises: 99c606471e2a
Create Date: 2023-10-12 16:58:29.692765

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f98a4febfd9'
down_revision: Union[str, None] = '99c606471e2a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('address', sa.Column('is_deleted', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('address', 'is_deleted')
    # ### end Alembic commands ###
