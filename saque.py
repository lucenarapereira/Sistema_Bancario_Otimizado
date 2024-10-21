def sacar(saldo, limite, extrato, numero_saques, LIMITE_SAQUES):
    try:
        valor = float(input("Informe o valor do saque: "))
        
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
            return saldo, extrato, numero_saques
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")

    except ValueError:
        print("Operação falhou! O valor informado deve ser um número.")

    return saldo, extrato, numero_saques
