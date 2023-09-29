# Equilibrando o Saldo

## Descrição
Este projeto tem como objetivo auxiliar na implementação e melhoria do sistema empresarial de uma empresa bancária. A equipe financeira identificou a necessidade de desenvolver uma solução que permita aos clientes equilibrar seu saldo bancário. Para isso, o programa solicita uma entrada representando o saldo atual do cliente e, em seguida, são informados o valor de um depósito e um saque. O programa calcula e exibe o saldo final com base nessas transações.

**Informação:** As transações de depósito e retirada devem ser tratadas como valores positivos e negativos, respectivamente, para garantir o correto cálculo do saldo final.

## Entrada
- `saldoAtual`: um número decimal representando o saldo atual da conta bancária.
- `valorDeposito`: um número decimal representando o valor a ser depositado na conta.
- `valorRetirada`: um número decimal representando o valor a ser retirado da conta.

**Regra de Formatação:** Considerar apenas uma casa decimal para esse desafio.

## Saída
Um número decimal que representa o saldo atualizado na conta bancária após o processamento das transações.

## Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada (saldoAtual, valorDeposito, valorRetirada) | Saída (Saldo Atualizado) |
|----------------------------------------------------|--------------------------|
| 1000, 500, 200                                     | 1300.0                   |
| 100,  10,  50                                      | 60.0
| 4000, 1500, 200                                    | 1000.0                   |
