def depositar(saldo, valor, extrato):
    extrato.append(f"Deposito no valor {valor}")
    return saldo + valor, extrato

def saque(saldo, valor, extrato, numero_saques, limite_saques, limite):
    if saldo >= valor and numero_saques < limite_saques and valor <= limite:
        saldo = saldo - valor
        print("Saque realizado com sucesso")
        extrato.append(f"Saque no valor {valor}")
        return saldo, extrato

def mostrar_extrato(saldo, extrato):
    for item in extrato:
        print(item)
    print(f"Saldo atual: R${saldo:.2f}")