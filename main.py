from deposito import depositar
from saque import sacar
from extrato import mostrar_extrato
from usuarios import cadastrar_usuario
from conta import criar_conta

def menu_opcoes():
    return """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Cadastrar Usuário
    [c] Criar Conta
    [q] Sair
    => """

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = [] 

    while True:
        opcao = input(menu_opcoes())

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, limite, extrato, numero_saques, LIMITE_SAQUES)

        elif opcao == "e":
            mostrar_extrato(saldo, extrato)

        elif opcao == "u": 
            usuarios = cadastrar_usuario(usuarios)

        elif opcao == "c": 
            contas = criar_conta(usuarios, contas) 

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
