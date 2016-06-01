def calculaPessoasBebeCafe(n, p):
    return n * (p / 100)

def calculaQtdCafe(n, p, m):
    total = calculaPessoasBebeCafe(n, p) * m
    if(total < 1000):
        return print('Serão necessários %.2f ml de café' %(total))
    else:
        return print('Será necessário %.2f L de café' %(total / 1000))


n = float(input('Digite o n de participantes: '))
p = float(input('Digite o percentual de participantes que bebem café: '))
m = float(input('Digite o volume que cada um bebe em ml: '))
calculaQtdCafe(n,p,m)

    
    

    
