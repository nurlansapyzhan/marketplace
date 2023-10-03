"""migtaition

Revision ID: 20a1ef17adc6
Revises: 
Create Date: 2023-10-03 15:10:58.691715

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '20a1ef17adc6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('permissions', sa.JSON(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('registered_at', sa.TIMESTAMP(), nullable=True),
                    sa.Column('role_id', sa.Integer(), nullable=True),
                    sa.Column('hashed_password', sa.String(), nullable=False),
                    sa.Column('is_active', sa.Boolean(), nullable=False),
                    sa.Column('is_superuser', sa.Boolean(), nullable=False),
                    sa.Column('is_verified', sa.Boolean(), nullable=False),
                    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('affiliation',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_affiliation_id'), 'affiliation', ['id'], unique=False)
    op.create_table('brand',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('brand_name', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_brand_id'), 'brand', ['id'], unique=False)
    op.create_table('category',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('category', sa.String(), nullable=False),
                    sa.Column('category_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_category_id'), 'category', ['id'], unique=False)
    op.create_table('collection',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('added_db_at', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_collection_id'), 'collection', ['id'], unique=False)
    op.create_table('color',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('color_name', sa.String(), nullable=False),
                    sa.Column('number_color', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_color_id'), 'color', ['id'], unique=False)
    op.create_table('compound',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('compound_name', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_compound_id'), 'compound', ['id'], unique=False)
    op.create_table('pattern',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('patterns_name', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_pattern_id'), 'pattern', ['id'], unique=False)
    op.create_table('product_sales_type',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_product_sales_type_id'), 'product_sales_type', ['id'], unique=False)
    op.create_table('season',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('seasons_name', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_season_id'), 'season', ['id'], unique=False)
    op.create_table('size_letter',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('size', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_size_letter_id'), 'size_letter', ['id'], unique=False)
    op.create_table('size_numbers',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('size', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_size_numbers_id'), 'size_numbers', ['id'], unique=False)
    op.create_table('product',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('brand_id', sa.Integer(), nullable=True),
                    sa.Column('description', sa.String(), nullable=True),
                    sa.Column('color_id', sa.Integer(), nullable=True),
                    sa.Column('product_rating', sa.Float(), nullable=True),
                    sa.Column('number_of_reviews', sa.Integer(), nullable=True),
                    sa.Column('compound_id', sa.Integer(), nullable=True),
                    sa.Column('pattern_id', sa.Integer(), nullable=True),
                    sa.Column('season_id', sa.Integer(), nullable=True),
                    sa.Column('collection_id', sa.Integer(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('added_db_at', sa.DateTime(), nullable=True),
                    sa.Column('affiliation_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['affiliation_id'], ['affiliation.id'], ),
                    sa.ForeignKeyConstraint(['brand_id'], ['brand.id'], ),
                    sa.ForeignKeyConstraint(['collection_id'], ['collection.id'], ),
                    sa.ForeignKeyConstraint(['color_id'], ['color.id'], ),
                    sa.ForeignKeyConstraint(['compound_id'], ['compound.id'], ),
                    sa.ForeignKeyConstraint(['pattern_id'], ['pattern.id'], ),
                    sa.ForeignKeyConstraint(['season_id'], ['season.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_product_id'), 'product', ['id'], unique=False)
    op.create_table('size',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('size_numbers_id', sa.Integer(), nullable=False),
                    sa.Column('size_letter_id', sa.Integer(), nullable=False),
                    sa.Column('affiliation_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['affiliation_id'], ['affiliation.id'], ),
                    sa.ForeignKeyConstraint(['size_letter_id'], ['size_letter.id'], ),
                    sa.ForeignKeyConstraint(['size_numbers_id'], ['size_numbers.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_size_id'), 'size', ['id'], unique=False)
    op.create_table('photo',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('url', sa.String(), nullable=False),
                    sa.Column('product_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_photo_id'), 'photo', ['id'], unique=False)
    op.create_table('product_category',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('product_id', sa.Integer(), nullable=False),
                    sa.Column('category_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
                    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_product_category_id'), 'product_category', ['id'], unique=False)
    op.create_table('seller_product',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('product_id', sa.Integer(), nullable=False),
                    sa.Column('salesman_id', sa.Integer(), nullable=False),
                    sa.Column('price', sa.Float(), nullable=False),
                    sa.Column('discount', sa.Float(), nullable=False),
                    sa.Column('sale_type_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
                    sa.ForeignKeyConstraint(['sale_type_id'], ['product_sales_type.id'], ),
                    sa.ForeignKeyConstraint(['salesman_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_seller_product_id'), 'seller_product', ['id'], unique=False)
    op.create_table('seller_products_size',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('product_id', sa.Integer(), nullable=False),
                    sa.Column('size_numbers_id', sa.Integer(), nullable=True),
                    sa.Column('size_letter_id', sa.Integer(), nullable=True),
                    sa.Column('quantity', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
                    sa.ForeignKeyConstraint(['size_letter_id'], ['size_letter.id'], ),
                    sa.ForeignKeyConstraint(['size_numbers_id'], ['size_numbers.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_seller_products_size_id'), 'seller_products_size', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('role')
    op.drop_index(op.f('ix_seller_products_size_id'), table_name='seller_products_size')
    op.drop_table('seller_products_size')
    op.drop_index(op.f('ix_seller_product_id'), table_name='seller_product')
    op.drop_table('seller_product')
    op.drop_index(op.f('ix_product_category_id'), table_name='product_category')
    op.drop_table('product_category')
    op.drop_index(op.f('ix_photo_id'), table_name='photo')
    op.drop_table('photo')
    op.drop_index(op.f('ix_size_id'), table_name='size')
    op.drop_table('size')
    op.drop_index(op.f('ix_product_id'), table_name='product')
    op.drop_table('product')
    op.drop_index(op.f('ix_size_numbers_id'), table_name='size_numbers')
    op.drop_table('size_numbers')
    op.drop_index(op.f('ix_size_letter_id'), table_name='size_letter')
    op.drop_table('size_letter')
    op.drop_index(op.f('ix_season_id'), table_name='season')
    op.drop_table('season')
    op.drop_index(op.f('ix_product_sales_type_id'), table_name='product_sales_type')
    op.drop_table('product_sales_type')
    op.drop_index(op.f('ix_pattern_id'), table_name='pattern')
    op.drop_table('pattern')
    op.drop_index(op.f('ix_compound_id'), table_name='compound')
    op.drop_table('compound')
    op.drop_index(op.f('ix_color_id'), table_name='color')
    op.drop_table('color')
    op.drop_index(op.f('ix_collection_id'), table_name='collection')
    op.drop_table('collection')
    op.drop_index(op.f('ix_category_id'), table_name='category')
    op.drop_table('category')
    op.drop_index(op.f('ix_brand_id'), table_name='brand')
    op.drop_table('brand')
    op.drop_index(op.f('ix_affiliation_id'), table_name='affiliation')
    op.drop_table('affiliation')
    # ### end Alembic commands ###
