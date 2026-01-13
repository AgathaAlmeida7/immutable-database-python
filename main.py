"""
Sistema Financeiro Imutável com Tuplas
"""

# ============================
# Constantes do domínio
# ============================

TIPO_ENTRADA = "ENTRADA"
TIPO_SAIDA = "SAIDA"

"""
CONTRATO DE DADOS — TRANSAÇÃO FINANCEIRA

Cada transação é uma tupla imutável com exatamente 5 posições:
0 - transacao_id (int)
1 - tipo (ENTRADA | SAIDA)
2 - valor (float)
3 - data_hora (str)
4 - descricao (str)
"""


def criar_transacao(transacao_id, tipo, valor, data_hora, descricao):
    return (transacao_id, tipo, valor, data_hora, descricao)


def calcular_saldo(banco):
    saldo = 0
    for transacao in banco:
        _, tipo, valor, _, _ = transacao
        if tipo == TIPO_ENTRADA:
            saldo += valor
        elif tipo == TIPO_SAIDA:
            saldo -= valor
    return saldo


def validar_tipo_transacao(tipo):
    if tipo not in (TIPO_ENTRADA, TIPO_SAIDA):
        raise ValueError("Tipo de transação inválido.")


def validar_valor(valor):
    if not isinstance(valor, (int, float)):
        raise ValueError("Valor deve ser numérico.")
    if valor <= 0:
        raise ValueError("Valor deve ser maior que zero.")


def validar_saldo_para_saida(saldo_atual, valor):
    if valor > saldo_atual:
        raise ValueError("Saldo insuficiente para realizar a saída.")


def registrar_transacao(banco, transacao_id, tipo, valor, data_hora, descricao):
    validar_tipo_transacao(tipo)
    validar_valor(valor)

    saldo_atual = calcular_saldo(banco)

    if tipo == TIPO_SAIDA:
        validar_saldo_para_saida(saldo_atual, valor)

    nova_transacao = criar_transacao(
        transacao_id, tipo, valor, data_hora, descricao
    )

    return banco + (nova_transacao,)


def listar_transacoes(banco):
    if not banco:
        print("Nenhuma transação registrada.")
        return

    for transacao in banco:
        print(transacao)


def exibir_menu():
    print("\n=== SISTEMA FINANCEIRO IMUTÁVEL ===")
    print("1 - Registrar ENTRADA")
    print("2 - Registrar SAÍDA")
    print("3 - Ver SALDO")
    print("4 - Ver HISTÓRICO")
    print("0 - Sair")


def executar_sistema():
    banco = ()
    contador_id = 1

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando sistema...")
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

            contador_id += 1
            print("Entrada registrada com sucesso.")

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
            listar_transacoes(banco)

        else:
            print("Opção inválida.")


# ============================
# PONTO DE ENTRADA DO SISTEMA
# ============================

if __name__ == "__main__":
    print("🚀 Sistema iniciado com sucesso!")
    executar_sistema()
