saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())

def calcular_saldo_final(saldo_atual, valor_deposito, valor_retirada):
    saldo_final = saldo_atual + valor_deposito - valor_retirada
    return saldo_final

saldo_final = calcular_saldo_final(saldo_atual, valor_deposito, valor_retirada)
print(f"Saldo atualizado na conta: {saldo_final:.1f}")
