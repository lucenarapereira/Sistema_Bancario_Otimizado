def criar_conta(usuarios, contas):
    cpf = input("Informe o CPF do titular da conta (apenas números): ")
    
    usuario_encontrado = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)

    if usuario_encontrado is None:
        print("Erro: Usuário não encontrado. Cadastre o usuário antes de criar uma conta.")
        return contas

    numero_conta = len(contas) + 1  
    agencia = "0001" 

    nova_conta = {
        'agencia': agencia,
        'numero_conta': numero_conta,
        'usuario': usuario_encontrado['nome']  
    }
    
    contas.append(nova_conta) 
    print(f"Conta criada com sucesso para {usuario_encontrado['nome']}! Agência: {agencia}, Número da conta: {numero_conta}")

    return contas
