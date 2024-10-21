def cadastrar_usuario(usuarios):
    nome = input("Informe seu nome (min 3 caracteres, max 50): ")
    
    if len(nome) < 3 or len(nome) > 50:
        print("Erro: O nome deve ter entre 3 e 50 caracteres.")
        return usuarios

    nascimento = input("Informe sua data de nascimento (DD/MM/AAAA): ")
    cpf = input("Informe seu CPF (pode incluir pontos e hífens): ")
    
    cpf = cpf.replace('.', '').replace('-', '').strip()
    
    if len(cpf) != 11 or not cpf.isdigit():
        print("Erro: O CPF deve conter exatamente 11 números.")
        return usuarios

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Erro: Já existe um usuário cadastrado com este CPF.")
            return usuarios

    endereco = input("Informe seu endereço no formato 'Logradouro, NRO - Bairro - Cidade/Sigla Estado': ")

    novo_usuario = {
        'nome': nome,
        'nascimento': nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")

    return usuarios
