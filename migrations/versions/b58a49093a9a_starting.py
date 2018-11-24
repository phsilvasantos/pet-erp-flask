"""starting

Revision ID: b58a49093a9a
Revises: 
Create Date: 2018-11-18 11:37:18.809205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b58a49093a9a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clientes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=30), nullable=False),
    sa.Column('sexo', sa.String(length=1), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contatos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tel1', sa.String(length=13), nullable=True),
    sa.Column('tel2', sa.String(length=13), nullable=True),
    sa.Column('email', sa.String(length=30), nullable=True),
    sa.Column('cliente_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cliente_id'], ['clientes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('enderecos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rua', sa.String(length=30), nullable=True),
    sa.Column('numero', sa.Integer(), nullable=True),
    sa.Column('bairro', sa.String(length=30), nullable=True),
    sa.Column('cidade', sa.String(length=30), nullable=True),
    sa.Column('estado', sa.CHAR(length=2), nullable=True),
    sa.Column('distancia', sa.Float(), nullable=True),
    sa.Column('cliente_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cliente_id'], ['clientes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('peludos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=30), nullable=False),
    sa.Column('breed', sa.String(length=20), nullable=False),
    sa.Column('pelagem', sa.String(length=6), nullable=False),
    sa.Column('nascimento', sa.Date(), nullable=True),
    sa.Column('data_start', sa.Date(), nullable=True),
    sa.Column('sexo', sa.String(length=1), nullable=False),
    sa.Column('castrado', sa.String(length=1), nullable=False),
    sa.Column('cliente_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cliente_id'], ['clientes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vendas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo', sa.String(length=10), nullable=False),
    sa.Column('descricao', sa.Text(), nullable=False),
    sa.Column('data_venda', sa.Date(), nullable=False),
    sa.Column('valor_servicos', sa.Float(), nullable=True),
    sa.Column('valor_taxi', sa.Float(), nullable=True),
    sa.Column('cliente_id', sa.Integer(), nullable=True),
    sa.Column('saldo', sa.Float(), nullable=True),
    sa.Column('data_pbanho', sa.Date(), nullable=True),
    sa.Column('n_banhos', sa.Integer(), nullable=True),
    sa.Column('tipo_banho', sa.String(length=15), nullable=True),
    sa.Column('pacote', sa.String(length=10), nullable=True),
    sa.Column('data_entrada', sa.Date(), nullable=True),
    sa.Column('data_saida', sa.Date(), nullable=True),
    sa.Column('valor_diarias', sa.Float(), nullable=True),
    sa.Column('valor_prod', sa.Float(), nullable=True),
    sa.Column('custo_prod', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['cliente_id'], ['clientes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('association',
    sa.Column('peludos_id', sa.Integer(), nullable=True),
    sa.Column('vendas_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['peludos_id'], ['peludos.id'], ),
    sa.ForeignKeyConstraint(['vendas_id'], ['vendas.id'], )
    )
    op.create_table('pagamentos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.Date(), nullable=False),
    sa.Column('valor', sa.Float(), nullable=False),
    sa.Column('valor_entrada', sa.Float(), nullable=False),
    sa.Column('forma_pagto', sa.String(length=15), nullable=False),
    sa.Column('venda_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['venda_id'], ['vendas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pagamentos')
    op.drop_table('association')
    op.drop_table('vendas')
    op.drop_table('peludos')
    op.drop_table('enderecos')
    op.drop_table('contatos')
    op.drop_table('clientes')
    # ### end Alembic commands ###