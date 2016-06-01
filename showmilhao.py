questao1 = 'Quem é o autor da seguinte frase? "Independência ou morte!"'
alternativa1 = ['a.Janio Quadros', 'b.Floriano Peixoto','c.Pedro Alvares Cabral','d.Dom Pedro I']
questao2 = 'Em que ano foi feita a proclamação da república do Brasil?'
alternativa2 = ['a.1956','b.1989', 'c.1974', 'd.1922']
questao3 = 'Quem foi que pôs fim a Lei Áurea'
alternativa3 = ['a.Isabel Cristina Leopoldina de Bragança - Princesa Isabel', 'b.Domitila de Castro Canto e Melo - Marquesa de Santos', 'c.Maria Antonieta Josefa Joana de Habsburgo-Lorena', 'd.Maria Leopoldina de Áustria']
questao4 = 'Em que ano as mulheres brasileiras conquistaram o direito de participar das eleições como eleitoras e candidatas?'
alternativa4=['a.1965', 'b.1988', 'c.1974', 'd.1935']
questao5 = 'Quem foi a primeira programadora do mundo?'
alternativa5=['a.Jenyffer Mayer','b.Maria Stonievsky','c.Ada Lovelace','d.Susan Richards']
corretas = ['d', 'b', 'a', 'd', 'c']
questao = [questao1, questao2, questao3, questao4, questao5]
alternativa = [alternativa1, alternativa2, alternativa3, alternativa4, alternativa5]

i = 0
while(i < len(questao)):
    print(questao[i])
    print('Escolha uma das alternativas')
    for x in alternativa[i]:
        print(x)
    resposta = input()
    if resposta == corretas[i]:
        print('RESPOSTA CORRETA')
    else:
        print('RESPOSTA INCORRETA')
    print('\n')    
    i = i + 1

    

    
    

