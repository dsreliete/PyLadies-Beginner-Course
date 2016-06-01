def testaPalindromo(p):
    inverte = p[::-1] 
    if inverte == p:
        return print('A palavra é um palíndromo %s = %s' %(p, inverte))
    else:
       return print('A palavra não é um palíndromo %s diferente %s' %(p, inverte))

p = input('Digite a palavra que deseja verificar se é um palíndromo: ')
testaPalindromo(p)
