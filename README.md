# Banco de Dados Imutável com Tuplas em Python

## 📌 Descrição do Projeto

Este projeto simula um **banco de dados financeiro imutável**, utilizando exclusivamente **tuplas** como estrutura principal de dados.

O objetivo é demonstrar conceitos fundamentais de **imutabilidade**, **modelagem de dados**, **histórico de eventos** e **pensamento backend profissional**, sem dependência de banco de dados real.

---

## 🎯 Objetivo

Registrar **transações financeiras imutáveis**, garantindo:

- Integridade dos dados
- Histórico confiável
- Facilidade de auditoria
- Previsibilidade do sistema

Nenhuma transação pode ser alterada após ser registrada.

---

## 💰 O que é uma Transação

Uma transação representa um **evento financeiro único**, que ocorre apenas uma vez e nunca pode ser modificado.

### Tipos de transação:
- **ENTRADA** → valores recebidos
- **SAÍDA** → valores gastos

---

## 📊 Dados obrigatórios de uma transação

Cada transação contém obrigatoriamente:

1. Identificador único da transação
2. Tipo da transação (entrada ou saída)
3. Valor financeiro
4. Data e hora do evento
5. Descrição da transação

---

## 🧱 Estrutura de Dados

### Transação
Uma transação é representada por uma **tupla**, com estrutura fixa e imutável:

(transacao_id, tipo, valor, data_hora, descricao)


### Banco de Dados
O banco de dados é representado por uma **tupla de tuplas**, onde cada item é uma transação:

(
transacao,
transacao,
transacao,
...
)


---

## 🔒 Regras do Sistema

- Transações **não podem ser alteradas**
- Correções são feitas por **novas transações**
- O saldo **não é armazenado**, é calculado a partir do histórico
- O histórico financeiro é permanente

---

## 🧠 Conceitos Demonstrados

- Imutabilidade com tuplas
- Modelagem de domínio
- Histórico de eventos
- Pensamento backend
- Boas práticas de design de dados

---

## 🚀 Próximas Etapas

- Implementar funções para:
  - Registrar novas transações
  - Listar histórico
  - Calcular saldo a partir das transações
