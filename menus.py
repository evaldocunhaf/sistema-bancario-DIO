import datetime
import operacoes as ops

id_conta = 0


def menu_usuario(usuarios, contas_gerais):
    global id_conta
    contas = []
    while True:
        acao_login = int(input("""Bem vindo ao sistema bancário
        O que deseja fazer?
        > 1 - Login
        > 2 - Cadastro
        > """))

        if acao_login == 1:
            cpf = str(input('Digite o CPF: '))
            if cpf in usuarios.keys():
                print(f"Olá senhor(a): {usuarios[cpf]['nome']}")
                senha = str(input('Digite a Senha: '))
                if senha == usuarios[cpf]['senha']:
                    print("Seja bem vindo!")
                    usuario = usuarios[cpf]
                    contas = [conta for conta in contas_gerais if conta['usuario'] == cpf]
                    break
                else:
                    print("Senha incorreta!")
                    continue
            else:
                print("usuário não encontrado")
                continue
        elif acao_login == 2:
            cpf = str(input('Digite o CPF: '))
            if cpf in usuarios.keys():
                print("Não podem haver 2 usuários com o mesmo cpf")
                continue
            nome = str(input('Digite o Nome: '))
            senha = str(input('Digite a Senha: '))
            data_nascimento = datetime.datetime.strptime(input('Data de Nascimento: '), '%d/%m/%Y')
            print("Agora vamos registrar seu endereço")
            logradouro = str(input('Digite o logradouro: '))
            numero = str(input('Digite o numero: '))
            bairro = str(input('Digite o bairro: '))
            cidade = str(input('Digite o cidade: '))
            estado = str(input('Digite o estado(sigla): '))
            endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"
            usuarios[f"{cpf}"] = {"nome": nome, "data_nascimento": data_nascimento.date(), "senha": senha,
                                  "endereco": endereco}
            usuario = usuarios[cpf]
            contas.append(
                {"usuario": cpf, "agencia": '0001', "numero": id_conta, 'extrato': [], 'saldo': 0, 'numero_saques': 0,
                 'data_uso': datetime.date.today()})
            id_conta += 1
            break
        else:
            continue
    return usuario, contas

def menu_contas(contas):
    print("Qual conta voce deseja selecionar?")
    for conta in contas:
        print(f"{conta['numero']} - {conta['saldo']}")
    escolha = int(input("> "))
    return contas[escolha]


def menu_da_conta(conta, limite):
    acao = int(input(f"""O que você deseja fazer hoje?
> 1 - Ver Saldo Atual
> 2 - Fazer um depósito
> 3 - Fazer um extrato({3 - conta["numero_saques"]} disponíveis)
> 4 - Sair 
> """))

    if acao == 1:
        ops.mostrar_extrato(conta["saldo"], extrato=conta["extrato"])
    elif acao == 2:
        deposito = float(input("Quanto você deseja depositar?\n"))
        conta["saldo"], conta["extrato"] = ops.depositar(conta["saldo"], deposito, conta["extrato"])
    elif acao == 3:
        saque = float(input("Quanto você deseja extrair?\n> "))
        conta["saldo"], conta["extrato"] = ops.saque(saldo = conta["saldo"], valor = saque, limite = limite, extrato = conta["extrato"], limite_saques = 3, numero_saques = conta["numero_saques"])
        conta["numero_saques"] += 1

