"""created pizza_id and restaurant_id

Revision ID: 8215768630a0
Revises: fc2445d4c3e6
Create Date: 2024-04-15 12:29:19.705241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8215768630a0'
down_revision = 'fc2445d4c3e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pizza_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('restaurant_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_restaurant_pizzas_restaurant_id_restaurants'), 'restaurants', ['restaurant_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_restaurant_pizzas_pizza_id_pizzas'), 'pizzas', ['pizza_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_restaurant_pizzas_pizza_id_pizzas'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_restaurant_pizzas_restaurant_id_restaurants'), type_='foreignkey')
        batch_op.drop_column('restaurant_id')
        batch_op.drop_column('pizza_id')

    # ### end Alembic commands ###
