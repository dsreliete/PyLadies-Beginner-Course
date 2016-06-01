pessoa = input('Olá qual o seu nome? \n')
bebida = int(input(pessoa + ' , escolha uma opção de bebida para tomar \n 1: CHA \n 2: CAFÉ \n 3: SUCO \n'))
if bebida == 1:
    print('vc escolheu chá')
elif bebida == 2:
    print('vc escolheu café')
elif bebida == 3:
    print('vc escolheu suco')
else:
    print(':(')
