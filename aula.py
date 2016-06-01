Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print ('Hello, Ladies')
Hello, Ladies
>>> a = 2
>>> print a
SyntaxError: Missing parentheses in call to 'print'
>>> a
2
>>> type (a)
<class 'int'>
>>> m = true
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    m = true
NameError: name 'true' is not defined
>>> m = True
>>> type (m)
<class 'bool'>
>>> a = 2
>>> b = 4
>>> c = 0
>>> d = 2.0
>>> e = 4E-2
>>> f = 0
>>> g = 2 + 3j
>>> g
(2+3j)
>>> i = a . c + 4j
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    i = a . c + 4j
AttributeError: 'int' object has no attribute 'c'
>>> i = a * c
>>> i
0
>>> h = 4 + j
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    h = 4 + j
NameError: name 'j' is not defined
>>> 4 + i
4
>>> a,b, c = 2, 3, 4
>>> a
2
>>> a, b, c
(2, 3, 4)
>>> a, b = b, c
>>> a, b, c
(3, 4, 4)
>>> a, b, c = 'Jet'
>>> a, b, c
('J', 'e', 't')
>>> a,b = b, a
>>> a, b, c
('e', 'J', 't')
>>> a, b, c = "Je"
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a, b, c = "Je"
ValueError: need more than 2 values to unpack
>>> a = 2
>>> type (a)
<class 'int'>
>>> b = float(a)
>>> type b
SyntaxError: invalid syntax
>>> type (b)
<class 'float'>
>>> b
2.0
>>> c = complex (a)
>>> c
(2+0j)
>>> d = str(a)
>>> d
'2'
>>> e = int d
SyntaxError: invalid syntax
>>> e = int (d)
>>> e
2
>>> type (d)
<class 'str'>
>>> type (e)
<class 'int'>
>>> print ('a' a)
SyntaxError: invalid syntax
>>> print ('a' + a)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print ('a' + a)
TypeError: Can't convert 'int' object to str implicitly
>>> print ('a' + str(a))
a2
>>> a =2
>>> b = 3
>>> c = (a + b - 2 * a + a ** a) / 5
>>> c
1.0
>>> a = 2, b = 3, c = 2.0, d = '2.0'
SyntaxError: can't assign to literal
>>> a, b, c, d = 2, 3, 2.0, '2.0'
>>> a, b, c , d
(2, 3, 2.0, '2.0')
>>> a == c
True
>>> a, b, c, d
(2, 3, 2.0, '2.0')
>>> a + b
5
>>> b ** a
9
>>> a + c
4.0
>>> a + d
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a + d
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print (a + d)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    print (a + d)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> a + d
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a + d
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> a == c
True
>>> a, b, c , d
(2, 3, 2.0, '2.0')
>>> a == c
True
>>> a <= b
True
>>> a < b and b < c
False
>>> a < b or b < c
True
>>>  a > c or a >= c
 
SyntaxError: unexpected indent
>>> a > c or a >= c
True
>>> not (a != b and b <= (a**2)-1)
False
>>> print (a + d)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    print (a + d)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print (str(a) + d)
22.0
>>> a = 'eliete'
>>> b = 'sheldon'
>>> a + b
'elietesheldon'
>>> a = 'São Paulo'
>>> b = 'você'
>>> a + b
'São Paulovocê'
>>> b = " você"
>>> a + b
'São Paulo você'
>>> print (a + ' ' + b)
São Paulo  você
>>> eliete = 'eliete'
>>> eliete[0]
'e'
>>> eliete[-1]
'e'
>>> eliete[-2]
't'
>>> eliete[3:4]
'e'
>>> eliete[3:5
KeyboardInterrupt
>>> eliete[3:5]
'et'
>>> eliete[-1]
'e'
>>> eliete[-1:]
'e'
>>> eliete[4:]
'te'
>>> eliete[4:4]
''
>>> eliete[4:5]
't'
>>> eliete[::-1]
'eteile'
>>> eliete[3:6:1]
'ete'
>>> eliete[3:6:2]
'ee'
>>> a = 'maine coon'
>>> a.upper()
'MAINE COON'
>>> a.capitalize()
'Maine coon'
>>> a[::-1]
'nooc eniam'
>>> c = "Bicheti'
SyntaxError: EOL while scanning string literal
>>> c = 'Bicheti'
>>> c[6]
'i'
>>> c[6] = 'e'
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    c[6] = 'e'
TypeError: 'str' object does not support item assignment
>>> c[6]
'i'
>>> c[0:5] + c[6] = 'e'
SyntaxError: can't assign to operator
>>> c[0:5]
'Biche'
>>> c[0:6]
'Bichet'
>>> d = 'e'
>>> c[0:6]+d
'Bichete'
>>> c[0:6]+'e'
'Bichete'
>>> c[0:6]+c[5]
'Bichett'
>>> c[0:6]+c[6]
'Bicheti'
>>> c[0:6] + c[4]
'Bichete'
>>> c.startswith('e')
False
>>> c.startswith(b')
	     
SyntaxError: EOL while scanning string literal
>>> c.startswith('b')
False
>>> c.startswith('B')
True
>>> len(a)
10
>>> len(c)
7
>>> a = '''Gatos amam mais as pessoas do que elas permitiriam.Mas eles permitiriam. Mas eles tem sabedoria suficiente para manter isso em segredo'''
>>> print a
SyntaxError: Missing parentheses in call to 'print'
>>> print(a)
Gatos amam mais as pessoas do que elas permitiriam.Mas eles permitiriam. Mas eles tem sabedoria suficiente para manter isso em segredo
>>> a.startswith('G')
True
>>> a.endswith('.')
False
>>> a.find('e', 5)
20
>>> a .find('a')
1
>>> len(a)
134
>>> a.replace('T', 0)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    a.replace('T', 0)
TypeError: Can't convert 'int' object to str implicitly
>>> a.replace('G', 'T')
'Tatos amam mais as pessoas do que elas permitiriam.Mas eles permitiriam. Mas eles tem sabedoria suficiente para manter isso em segredo'
>>> a = ['Gato', 9, True, [5, 'Rapper Bits']]
>>> a[3]
[5, 'Rapper Bits']
>>> a[2]
True
>>> a = ['Gato', 9, True, [5, 'Rapper Bits'], 'eliete']
>>> print a
SyntaxError: Missing parentheses in call to 'print'
>>> print (a)
['Gato', 9, True, [5, 'Rapper Bits'], 'eliete']
>>> a.append('sapo')
>>> print(a)
['Gato', 9, True, [5, 'Rapper Bits'], 'eliete', 'sapo']
>>> print(a[3][0])
5
>>> print(a[0][0])
G
>>> print(a[1])
9
>>> print(a[2])
True
>>> print(a[1][0])
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    print(a[1][0])
TypeError: 'int' object is not subscriptable
>>> 
>>> 
>>> 
>>> 
>>> chas = ['Camomila', 'Hortela', 'Cidreira']
>>> '/'.join(chas)
'Camomila/Hortela/Cidreira'
>>> chas2= {'Camomila', 'Hortela', 'Cidreira'}
>>> type(chas2)
<class 'set'>
>>> type(chas)
<class 'list'>
>>> '/'.join(chas2)
'Cidreira/Hortela/Camomila'
>>> print chas2
SyntaxError: Missing parentheses in call to 'print'
>>> print (chas2)
{'Cidreira', 'Hortela', 'Camomila'}
>>> chas2.append('Boldo')
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    chas2.append('Boldo')
AttributeError: 'set' object has no attribute 'append'
>>> chas.append('Boldo')
>>> print (chas)
['Camomila', 'Hortela', 'Cidreira', 'Boldo']
>>> chas.split('.')
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    chas.split('.')
AttributeError: 'list' object has no attribute 'split'
>>> s.o.s.plit(' ')
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    s.o.s.plit(' ')
NameError: name 's' is not defined
>>> s.o.s.split(' ')
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    s.o.s.split(' ')
NameError: name 's' is not defined
>>> sos = 's.o.s'
>>> sos.split(' ')
['s.o.s']
>>> 's.o.s'.split('.')
['s', 'o', 's']
>>> sos.split('.')
['s', 'o', 's']
>>> sos.capitalize[0]
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    sos.capitalize[0]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> sos[0]
's'
>>> sos.split(' ')
['s.o.s']
>>> sos.split('.')
['s', 'o', 's']
>>> a = 3,5,8
>>> print (a)
(3, 5, 8)
>>> c = ('Gato', 9, True, [10, 'fos'], ('Lello', 'Leloo', 'Lello', 'Leloo'))
>>> c[0]
'Gato'
>>> c[3]
[10, 'fos']
>>> c[3].append('eliete')
>>> c[3]
[10, 'fos', 'eliete']
>>> c[4].append('eliete')
Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    c[4].append('eliete')
AttributeError: 'tuple' object has no attribute 'append'
>>> type(c[4])
<class 'tuple'>
>>> c[3][0]
10
>>> c[4][0]
'Lello'
>>> var = 'Para medir o calor do dia, olhem para o comprimento do gato que dorme'
>>> len(var)
69
>>> var.startswith('p')
False
>>> var + '.'
'Para medir o calor do dia, olhem para o comprimento do gato que dorme.'
>>> var
'Para medir o calor do dia, olhem para o comprimento do gato que dorme'
>>> var += '.'
>>> var
'Para medir o calor do dia, olhem para o comprimento do gato que dorme.'
>>> var.endswith('.')
True
>>> var.find(',')
25
>>> var.replace('.', ',')
'Para medir o calor do dia, olhem para o comprimento do gato que dorme,'
>>> var.replace(',', '!')
'Para medir o calor do dia! olhem para o comprimento do gato que dorme.'
>>> var.replace('!', ',')
'Para medir o calor do dia, olhem para o comprimento do gato que dorme.'
>>> var.replace('.','!')
'Para medir o calor do dia, olhem para o comprimento do gato que dorme!'
>>> lista = ['1 kg de banana', '12 ovos', '1kg de farinha']
>>> list.append('fermento em po')
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    list.append('fermento em po')
TypeError: descriptor 'append' requires a 'list' object but received a 'str'
>>> lista.append('fermento em po')
>>> print (lista)
['1 kg de banana', '12 ovos', '1kg de farinha', 'fermento em po']
>>> id(lista)
52855240
>>> id('fermento em po')
52855408
>>> id('12 ovos')
52800848
>>> id(var)
52836392
>>> ================================ RESTART ================================
>>> 
Entre com o nome de ser personagem de quadrinho favorito: sheldon
>>> print(hq)
sheldon
>>> ================================ RESTART ================================
>>> 
Escreva quantos quadrinhos em média você compra por semana: 5
>>> print 5
SyntaxError: Missing parentheses in call to 'print'
>>> print(gasto)
5
>>> 
