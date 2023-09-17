"""test

Revision ID: 82916ca3493d
Revises: 326cab64a71b
Create Date: 2023-09-17 16:52:25.550092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82916ca3493d'
down_revision = '326cab64a71b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('unit', sa.String(length=3), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['ingredients.id'], name=op.f('fk_ingredients_parent_id_ingredients'), onupdate='CASCADE', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_ingredients'))
    )
    op.create_index(op.f('ix_ingredients_name'), 'ingredients', ['name'], unique=True)
    op.create_table('menus',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_menus'))
    )
    op.create_index(op.f('ix_menus_name'), 'menus', ['name'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users'))
    )
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('menu_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['menu_id'], ['menus.id'], name=op.f('fk_categories_menu_id_menus')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_categories')),
    sa.UniqueConstraint('name', name=op.f('uq_categories_name'))
    )
    op.create_table('restaurants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_restaurants_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_restaurants')),
    sa.UniqueConstraint('address', name=op.f('uq_restaurants_address'))
    )
    op.create_index(op.f('ix_restaurants_name'), 'restaurants', ['name'], unique=True)
    op.create_table('restaurant_menu',
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('menu_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['menu_id'], ['menus.id'], name=op.f('fk_restaurant_menu_menu_id_menus')),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], name=op.f('fk_restaurant_menu_restaurant_id_restaurants')),
    sa.PrimaryKeyConstraint('restaurant_id', 'menu_id', name=op.f('pk_restaurant_menu'))
    )
    op.create_table('subcategories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], name=op.f('fk_subcategories_category_id_categories')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_subcategories'))
    )
    op.create_index(op.f('ix_subcategories_name'), 'subcategories', ['name'], unique=True)
    op.create_table('dishes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('photo', sa.LargeBinary(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('subcategory_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['subcategory_id'], ['subcategories.id'], name=op.f('fk_dishes_subcategory_id_subcategories')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_dishes'))
    )
    op.create_index(op.f('ix_dishes_name'), 'dishes', ['name'], unique=True)
    op.create_table('dish_ingredient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('dish_id', sa.Integer(), nullable=False),
    sa.Column('ingredient_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['dish_id'], ['dishes.id'], name=op.f('fk_dish_ingredient_dish_id_dishes')),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredients.id'], name=op.f('fk_dish_ingredient_ingredient_id_ingredients')),
    sa.PrimaryKeyConstraint('id', 'dish_id', 'ingredient_id', name=op.f('pk_dish_ingredient'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dish_ingredient')
    op.drop_index(op.f('ix_dishes_name'), table_name='dishes')
    op.drop_table('dishes')
    op.drop_index(op.f('ix_subcategories_name'), table_name='subcategories')
    op.drop_table('subcategories')
    op.drop_table('restaurant_menu')
    op.drop_index(op.f('ix_restaurants_name'), table_name='restaurants')
    op.drop_table('restaurants')
    op.drop_table('categories')
    op.drop_table('users')
    op.drop_index(op.f('ix_menus_name'), table_name='menus')
    op.drop_table('menus')
    op.drop_index(op.f('ix_ingredients_name'), table_name='ingredients')
    op.drop_table('ingredients')
    # ### end Alembic commands ###