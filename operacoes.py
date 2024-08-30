def depositar(saldo, valor):
    return saldo + valor

def saque(saldo, valor):
    if saldo >= valor:
        return saldo - valor
    else:
        print("Saldo Insuficiente")

def extrato(saldo):
    print(f"Saldo atual: R${saldo:.2f}")