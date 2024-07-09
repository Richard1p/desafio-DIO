from cgi import print_directory


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == 'd': 
        valor = float(input('Qual o valor a depositar? '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print(f'Seu saldo atual: R$ {saldo}')

        else:
            print('Operação falhou, o valor informadoé invalido.')

    elif opcao =='s':
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite 

        excedeu_saque = numero_saques >= LIMITE_SAQUES


        if excedeu_saldo:
            print('Operação falhou! sem saldo suficiente.')

        elif excedeu_limite:
            print('O valor do saque excede o limite.')

        elif excedeu_saque:
            print('Numero maximo de saque excedido.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
        
        else:
            print('Operação falhou! Ovalor informado é inválido')

    elif opcao == 'e':
        print('\nextrato')
        print('Não foram realizado movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')

    elif opcao == 'q':
        break
    
    else:    
        print('Operação inválida, por favor seleciona novamente a operação desejada')