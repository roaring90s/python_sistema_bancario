menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input (menu)

    if opcao == "d":
        valor = float(input ("Informe o valor que deseja depositar:"))

        if valor > 0:
            saldo +=valor
            extrato+= f"Depósito: RS {valor:.2f}\n"
        else:
            print("Operação falhou! Quantia inválida.")    


    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar:"))



        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.") 
        elif valor < 0:
            print ("Operação falhou! Número inválido.")      
        elif valor < saldo:
            saldo -= valor
            extrato = saldo - valor

            print(f"Saque realizado no valor de RS {valor:.2f}\n")
        else:
            print("Operação falhou! Saldo insuficiente.")   


    elif opcao == "e":
        print("\n========= EXTRATO ========")
        print(f"Saldo atual de: RS{saldo:.2f}\n")
        print("=============================")


    elif opcao == "q":
        print("Obrigado por usar nosso banco!")
        break

    else:
        print("Entrada inválida.")