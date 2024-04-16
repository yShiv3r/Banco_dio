saques_por_dia = 3
limite_saque = 500
saldo = 0
total_sacado = list ()
quantS = 0
total_depositado = list()
quantD = 0
menu = (f'''{{:-^15}}
[1] Deposito
[2] Saque
[3] Extrato
[4] Sair
{('-'*15)}'''.format(' BANCO DIO '))
opcoes = [1,2,3,4]

while True:

    print(menu)
    num = int(input('Escolha uma opção de 1 a 4: '))
    while num not in opcoes:
        num = int(input('Escolha uma opção de 1 a 4: '))

    #DEPOSITO
    if num == 1:
        deposito = float(input('Qual o valor que deseja depositar: R$'))
        if deposito > 0:
            saldo += deposito
            total_depositado.append(deposito)
            quantD += 1
            print('-='*40)
            print(f'Foi efetuado o DEPOSITO no valor de R${deposito:.2f} agora o seu saldo é de R${saldo:.2f}')
            print('-='*40)

        else:
            print('-='*40)
            print('Não é posivel efetuar um deposito de valor negativo!')
            print('-='*40)

    #SAQUE
    if num == 2:
        saque = float(input('Qual o valor que deseja sacar: R$'))
        if saque <= saldo and saque <= limite_saque:
            saldo -= saque
            saques_por_dia -= 1
            total_sacado.append(saque)
            quantS += 1
            print('-='*40)
            print(f'Foi efetuado o SAQUE no valor de R${saque:.2f} agora o seu saldo é de R${saldo:.2f}')
            print('-='*40)
        else:
            print('Não foi possivel concluir o saque, pois você excedeu o limite de saldo, valor de saque e/ ou saques diarios')
    #EXTRATO
    if num == 3:
        print('{:-^30}'.format(' EXTRATO '))
        print(f'Saldo: R${saldo:.2f}')
        for c in range(quantD):
            print(f'{c+1}° Deposito {total_depositado[c]}')
        for c in range(quantS):
            print(f'{c+1}° Saque {total_sacado[c]}')
        print('-'*30)
    #SAIDA
    if num == 4:
        break