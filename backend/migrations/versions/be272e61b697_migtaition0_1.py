"""migtaition0.1

Revision ID: be272e61b697
Revises: 20a1ef17adc6
Create Date: 2023-10-04 14:33:45.307351

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be272e61b697'
down_revision: Union[str, None] = '20a1ef17adc6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_who_left_review_id', sa.Integer(), nullable=False),
    sa.Column('to_the_seller_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('review_id', sa.Integer(), nullable=True),
    sa.Column('review_text', sa.String(), nullable=True),
    sa.Column('grade', sa.Float(), nullable=True),
    sa.Column('added_db_at', sa.DateTime(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['review_id'], ['review.id'], ),
    sa.ForeignKeyConstraint(['to_the_seller_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_who_left_review_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_review_id'), 'review', ['id'], unique=False)
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_address_id'), 'address', ['id'], unique=False)
    op.create_table('payment_methods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('method_names', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_payment_methods_id'), 'payment_methods', ['id'], unique=False)
    op.create_table('check',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('buyer_id', sa.Integer(), nullable=False),
    sa.Column('address_id', sa.Integer(), nullable=False),
    sa.Column('total_price', sa.Float(), nullable=True),
    sa.Column('delivery_price', sa.Float(), nullable=True),
    sa.Column('method_names_id', sa.Integer(), nullable=True),
    sa.Column('basket_created_at', sa.DateTime(), nullable=True),
    sa.Column('check_created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['address.id'], ),
    sa.ForeignKeyConstraint(['buyer_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['method_names_id'], ['payment_methods.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_check_id'), 'check', ['id'], unique=False)
    op.add_column('seller_product', sa.Column('is_deleted', sa.Boolean(), nullable=False))
    op.add_column('seller_product', sa.Column('added_db_at', sa.DateTime(), nullable=True))
    op.add_column('seller_product', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('seller_product', 'deleted_at')
    op.drop_column('seller_product', 'added_db_at')
    op.drop_column('seller_product', 'is_deleted')
    op.drop_index(op.f('ix_check_id'), table_name='check')
    op.drop_table('check')
    op.drop_index(op.f('ix_payment_methods_id'), table_name='payment_methods')
    op.drop_table('payment_methods')
    op.drop_index(op.f('ix_address_id'), table_name='address')
    op.drop_table('address')
    op.drop_index(op.f('ix_review_id'), table_name='review')
    op.drop_table('review')
    # ### end Alembic commands ###