import menus


usuarios = {} #'{cpf}':{'nome': nome_usuario, 'data_nascimento': data nascimento, 'endereco': endereco}}
contas_gerais = [] #{'usuario': cpf, 'agencia': '0001', 'numero': 0, 'saldo': saldo, 'extrato': extrato, 'limite_saques': 0}
limite = 500

while True:
    usuario, contas = menus.menu_usuario(usuarios, contas_gerais)
    conta = menus.menu_contas(contas)
    menus.menu_da_conta(conta, limite)
