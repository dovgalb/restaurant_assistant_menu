"""fixes

Revision ID: 2ba2ef54266f
Revises: d780030f7166
Create Date: 2023-05-27 11:11:14.760620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ba2ef54266f'
down_revision = 'd780030f7166'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('menu_id', sa.Integer(), nullable=False))
    op.create_foreign_key(op.f('fk_categories_menu_id_menus'), 'categories', 'menus', ['menu_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_categories_menu_id_menus'), 'categories', type_='foreignkey')
    op.drop_column('categories', 'menu_id')
    # ### end Alembic commands ###