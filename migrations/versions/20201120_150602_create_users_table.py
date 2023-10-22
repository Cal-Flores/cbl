"""create_users_table

Revision ID: ffdc0a98111c
Revises:
Create Date: 2020-11-20 15:06:02.230689

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = 'ffdc0a98111c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )

    op.create_table('fighters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('nickname', sa.String()),
    sa.Column('prof_img', sa.String()),
    sa.Column('body_img', sa.String()),
    sa.Column('weight', sa.String()),
    sa.Column('medal', sa.String()),
    sa.Column('team_name', sa.String()),
    sa.Column('tour_win', sa.Integer()),
    sa.Column('tour_loss', sa.Integer())
    )

    op.create_table('teams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String()),
    sa.Column('logo_img', sa.String()),
    sa.Column('background_img', sa.String()),
    sa.Column('conf', sa.String()),
    sa.Column('divison', sa.String()),
    sa.Column('fly', sa.String()),
    sa.Column('bantam', sa.String()),
    sa.Column('feather', sa.String()),
    sa.Column('light', sa.String()),
    sa.Column('welter', sa.String()),
    sa.Column('middle', sa.String()),
    sa.Column('light_heavy', sa.String()),
    sa.Column('heavy', sa.String()),
    )

    op.create_table('tournaments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.String()),
    sa.Column('img', sa.String()),
    sa.Column('cons_img', sa.String()),
    )
    op.create_table('tour_results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('winner', sa.String()),
    sa.Column('loser', sa.String()),
    sa.Column('match', sa.String()),
    sa.Column('method', sa.String()),
    sa.Column('round', sa.String()),
    sa.Column('year', sa.String()),
    )

    op.create_table('medals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fighter', sa.String()),
    sa.Column('place', sa.String()),
    sa.Column('year', sa.String()),
    )

    if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")
    # ### end Alembic commands ###qqqqqqqqq


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('fighters')
    op.drop_table('teams')
    op.drop_table('tournaments')
    # ### end Alembic commands ###
