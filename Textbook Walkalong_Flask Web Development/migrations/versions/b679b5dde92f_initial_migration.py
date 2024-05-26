"""initial migration

Revision ID: b679b5dde92f
Revises: 
Create Date: 2024-05-26 08:58:19.029004

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b679b5dde92f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
#     # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_Users_username'), ['username'], unique=True)

#     # op.drop_table('unique_dogs')
#     # op.drop_table('employees')
#     # op.drop_table('cats')
#     # op.drop_table('people')
#     # op.drop_table('unique_cats')
#     # op.drop_table('dogs')
#     # op.drop_table('unique_monkeys')
#     # ### end Alembic commands ###


def downgrade():
#     # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('unique_monkeys',
    sa.Column('name', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('cat_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('age', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('cat_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('dogs',
    sa.Column('name', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('breed', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('age', mysql.INTEGER(), autoincrement=False, nullable=True),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('unique_cats',
    sa.Column('name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('catID', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('age', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('catID'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('people',
    sa.Column('first_name', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('last_name', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('age', mysql.INTEGER(), autoincrement=False, nullable=True),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('cats',
    sa.Column('cat_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('breed', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('age', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('cat_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('employees',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('last_name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('first_name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('middle_name', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('age', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('current_status', mysql.VARCHAR(length=50), server_default=sa.text("'employed'"), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('unique_dogs',
    sa.Column('name', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('cat_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('age', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('cat_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('Users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_Users_username'))

    op.drop_table('Users')
    op.drop_table('roles')
    # ### end Alembic commands ###
