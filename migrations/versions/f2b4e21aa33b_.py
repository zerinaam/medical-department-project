"""empty message

Revision ID: f2b4e21aa33b
Revises: e1e659b5e1f9
Create Date: 2023-05-22 15:13:58.221661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2b4e21aa33b'
down_revision = 'e1e659b5e1f9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('doctors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('sector_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sector_id'], ['sectors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('nurses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('sector_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sector_id'], ['sectors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('hospitals', sa.Column('building_year', sa.Integer(), nullable=True))
    op.add_column('sectors', sa.Column('floor', sa.Integer(), nullable=True))
    op.add_column('sectors', sa.Column('capacity', sa.Integer(), nullable=True))
    op.add_column('sectors', sa.Column('occupied', sa.Integer(), nullable=True))
    op.add_column('sectors', sa.Column('visits_allowed_until', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sectors', 'visits_allowed_until')
    op.drop_column('sectors', 'occupied')
    op.drop_column('sectors', 'capacity')
    op.drop_column('sectors', 'floor')
    op.drop_column('hospitals', 'building_year')
    op.drop_table('nurses')
    op.drop_table('doctors')
    # ### end Alembic commands ###
