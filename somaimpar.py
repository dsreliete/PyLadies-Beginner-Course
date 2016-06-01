print('Soma de números ímpares')
lista = [1,2,3,4,5,6,7,8,9,10]
somaImpar = 0
for x in lista:
    if (x % 2) != 0:
        somaImpar = somaImpar + x
        print('n = %d' %x)
        print('a soma dos n. impares da lista é %d' %somaImpar)
