def divide(n1, n2):
    if n2 > 0:
        decimal = n1 / n2
        inteiro = int(decimal)
        resto = n1 % n2
        return print ('O valor exato da divisão é %f.\nO inteiro é %d.\nO resto é %d. ' %(decimal, inteiro, resto))  
    else:
        return print('Impossível fazer divisão por zero')

n1 = float(input('Informe n1: '))
n2 = float(input('Informe n2: '))
print(divide(n1,n2))
