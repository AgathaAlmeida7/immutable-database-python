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
def validar_tipo_transacao(tipo):
        """
    Valida se o tipo da transação é permitido.
    """
        if tipo not in (TIPO_ENTRADA,TIPO_SAIDA):
            raise ValueError('tipo de transação invalida.')
        
def validar_valor(valor):
     """
    Valida se o valor da transação é válido.
    """
     if not isinstance(valor,(int,float)):
         raise ValueError('valor deve ser numerico')
     
     if valor<=0:
         raise ValueError('valor deve ser maior que zero:\n')
     
def validar_saldo_para_saida(saldo_atual,valor):
      """
    Impede que uma transação de saída gere saldo negativo.
    """
      if valor>saldo_atual:
           raise ValueError('saldo insuficiente para realizar a saida')

def registrar_transacao(banco,transacao_id,tipo,valor,data_hora,descricao):
     """
    Registra uma transação após validar todas as regras de negócio.
    Retorna um novo banco (imutável).
    """
     validar_tipo_transacao(tipo)
     validar_valor(valor)

     saldo_atual=calcular_saldo(banco)

     if tipo==TIPO_SAIDA:
            (saldo_atual,valor)
            nova_transacao=criar_transacao(transacao_id,tipo,valor,data_hora,descricao)
            return banco+(nova_transacao,) 

     