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
     
def exibir_menu():
    print("\n=== SISTEMAA FINANCEIRO IMUTÁVEL === ")
    print('1- REGISTRAR ENTRADA')
    print('2- REGISTRAR SAÍDA')
    print('3- VER SALDO')
    print('4- VER HISTÓRICO')
    print('0- SAIR')
     
def executar_sistema():
    banco=()
    contador_id=1

    while True:
            exibir_menu()
            opcao=input('escolha uma opção:')

            if opcao=="0":
              print('Encerrando sistema...')
              break
            elif opcao == "1":
                valor = float(input("Valor da entrada: "))
                descricao = input("Descrição: ")
                data_hora = input("Data/Hora: ")

                banco = registrar_transacao(
                banco,
                contador_id,
                TIPO_ENTRADA,
                valor,
                data_hora,
                descricao
            )

                contador_id+=1
                print('entrada registrada com sucesso.')
            elif opcao == "2":
                valor = float(input("Valor da saída: "))
                descricao = input("Descrição: ")
                data_hora = input("Data/Hora: ")

            try:
                banco = registrar_transacao(
                    banco,
                    contador_id,
                    TIPO_SAIDA,
                    valor,
                    data_hora,
                    descricao
                )
                contador_id += 1
                print("Saída registrada com sucesso.")
            except ValueError as erro:
                print(f"Erro: {erro}")
                    elif opcao == "3":
            saldo = calcular_saldo(banco)
            print(f"Saldo atual: R$ {saldo:.2f}")
                elif opcao == "4":
            if not banco:
                print("Nenhuma transação registrada.")
            else:
                for transacao in banco:
                    print(transacao)
                if __name__ == "__main__":
                    executar_sistema()
