"""
Projeto: Banco de Dados Imutável com Tuplas

Este arquivo conterá a lógica do sistema financeiro imutável.

Regras fundamentais:
- Nenhuma transação pode ser alterada
- Transações são representadas por tuplas
- O banco de dados é uma tupla de transações
- O saldo será calculado a partir do histórico
"""

# Estrutura conceitual de uma transação:
# (transacao_id, tipo, valor, data_hora, descricao)

# Estrutura conceitual do banco de dados:
# banco_de_dados = (
#     transacao,
#     transacao,
#     transacao,
# )

# Na próxima fase, serão implementadas funções para:
# - Registrar transações
# - Listar histórico
# - Calcular saldo
