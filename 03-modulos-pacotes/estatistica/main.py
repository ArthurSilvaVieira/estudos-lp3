#   importa tudo de matematica
import matematica

#   importar apenas os elementos (constantes, funções, classes)
#   necessários

from matematica import PI, subtrair
#from matematica import *

#   caso tenha conflito de nome
from matematica import PI as PI_MAT


#   importar a fn media do pacote estatistica e modulo descritiva
from descritiva import media
from inferencial import VALOR
#   from pacote1.subpacote1.subpacote11.modulo 

PI = 99999


print(matematica.PI)
print(matematica.somar(10.0, 3.2))
print(matematica.subtrair(10.0, 3.2))

print(PI)
print(PI_MAT)
print(subtrair(10.0, 3.2))