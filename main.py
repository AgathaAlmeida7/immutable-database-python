"""
Docstring do projeto
"""

# ============================
# Constantes do domínio
# ============================

TIPO_ENTRADA = "ENTRADA"
TIPO_SAIDA = "SAIDA"


def criar_transacao(transacao_id,tipo,valor,data_hora,descricao):
    """
    Cria e retorna uma transação financeira imutável.

    Uma transação é representada por uma tupla com estrutura fixa:
    (transacao_id, tipo, valor, data_hora, descricao)
    """
    return (transacao_id,tipo,valor,data_hora,descricao)

def registrar_transacao(banco_atual,transacao):
    """
    Registra uma nova transação no banco de dados imutável.

    Retorna um novo banco de dados, sem alterar o banco original.
    """
    return banco_atual+ (transacao,) 
    
def listar_transacoes(banco):
    """
    Lista todas as transações do banco de dados imutável.
    """

    for transacao in banco:
        print(transacao) 

def calcular_saldo(banco):
     """
    Calcula o saldo com base no histórico de transações.
    """
     saldo=0

     for transacao in banco:
        _, tipo,valor,_,=transacao

        if tipo==TIPO_ENTRADA:
            saldo+=valor
        elif tipo==TIPO_SAIDA:
            saldo-=valor
        return saldo