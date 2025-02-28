# Sistema Bancário em Python

Este é um sistema bancário simples desenvolvido em Python, que permite ao usuário realizar operações básicas como depósito, saque e consulta de extrato. O sistema funciona por meio de um menu interativo no terminal.

## Funcionalidades

- **Depósito**: O usuário pode depositar um valor positivo na conta.
- **Saque**: O usuário pode sacar um valor, respeitando o limite de R$500 por saque e o limite de três saques diários.
- **Extrato**: Exibe o saldo atual da conta.
- **Sair**: Encerra a execução do sistema.

## Regras do Sistema

1. O saldo inicial da conta é zero.
2. O usuário pode fazer depósitos de qualquer valor positivo.
3. O saque tem um limite máximo de R$500 por transação.
4. O usuário pode realizar no máximo 3 saques por dia.
5. O sistema exibe um extrato contendo o saldo atualizado.

## Como Usar

1. Execute o script em Python.
2. Escolha uma opção do menu digitando a letra correspondente.
3. Siga as instruções para cada operação.
4. Para sair, escolha a opção "q" no menu.

## Exemplo de Uso

```text
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> d
Informe o valor que deseja depositar: 1000
Depósito realizado com sucesso!

=> s
Informe o valor que deseja sacar: 300
Saque de R$ 300.00 realizado com sucesso!

=> e
========= EXTRATO =========
Saldo atual: R$ 700.00
===========================

=> q
Obrigado por usar nosso banco!
```

## Requisitos

- Python 3.x instalado

## Autor

Desenvolvido por @roaring90s como exercício de programação em Python.

