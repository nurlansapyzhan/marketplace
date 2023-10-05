"""migtaition0.2

Revision ID: 4baa7958dc08
Revises: be272e61b697
Create Date: 2023-10-05 12:04:00.138110

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4baa7958dc08'
down_revision: Union[str, None] = 'be272e61b697'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('discount_coupon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_coupons', sa.String(), nullable=False),
    sa.Column('coupon_code', sa.String(), nullable=False),
    sa.Column('discount_percentage', sa.Float(), nullable=True),
    sa.Column('discount_amount', sa.Float(), nullable=True),
    sa.Column('smallest_check_amount', sa.Float(), nullable=True),
    sa.Column('largest_check_amount', sa.Float(), nullable=True),
    sa.Column('total_number_activations', sa.Integer(), nullable=True),
    sa.Column('number_activations_per_user', sa.Integer(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('coupon_start_date', sa.DateTime(), nullable=True),
    sa.Column('coupon_expiration_date', sa.DateTime(), nullable=True),
    sa.Column('coupon_creation_date', sa.DateTime(), nullable=True),
    sa.Column('coupon_delete_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_discount_coupon_id'), 'discount_coupon', ['id'], unique=False)
    op.create_table('users_coupon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('seller_who_provides_coupon_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('buyer_who_can_use_coupon_id', sa.Integer(), nullable=True),
    sa.Column('coupon_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['buyer_who_can_use_coupon_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['coupon_id'], ['discount_coupon.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['seller_who_provides_coupon_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_coupon_id'), 'users_coupon', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_coupon_id'), table_name='users_coupon')
    op.drop_table('users_coupon')
    op.drop_index(op.f('ix_discount_coupon_id'), table_name='discount_coupon')
    op.drop_table('discount_coupon')
    # ### end Alembic commands ###
