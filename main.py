saldo = 0
saques = 0
import operacoes as ops

acao = int(input(f"""Bem Vindo ao sistema bancário
O que você deseja fazer hoje?
> 1 - Ver Saldo Atual
> 2 - Fazer um depósito
> 3 - Fazer um extrato({3 - saques} disponíveis)
> 4 - Sair """))

if acao == 1:
    ops.extrato(saldo)
elif acao == 2:
    deposito = float(input("Quanto você deseja depositar?\n"))
    ops.depositar(saldo, deposito)
elif acao == 3:
    if(saques <=3):
        saque = float(input("Quanto você deseja extrair?\n"))
        ops.saque(saldo)
        saques = saques+1
    else:
        print("Não é possível mais fazer extratos hoje")