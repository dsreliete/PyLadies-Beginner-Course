lista = ['Java', 'JavaScript', 'PHP', 'C', 'Python']
i = 0
while i < len(lista):
    if lista[i].startswith('P'):
        print(lista[i].upper())
    i = i + 1

for x in lista:
    if x.startswith('P'):
        print(x.upper())
    i = i + 1
