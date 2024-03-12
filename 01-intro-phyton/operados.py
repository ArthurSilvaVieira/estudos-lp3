# Operadores aritméticos
# +, -, *, /, **, ...

nota1 = 10.0
nota2 = 5.5
nota3 = 7.5

# mumero elevado a outro
# e elevado n
# 10 elevado a 2

num = 10
num_ele_2 = num **2

# Operados lógicos
# and, or, not

print(True and True)  #True
print(True and False) #False
print(False and True) #False
print(False and False)#False

print(True or True)  #True
print(True or False) #False
print(False or True) #False
print(False or False)#True 

print(not True)  #False
print(not False) #False


# permitir entrada
# - o usuario for funcionario E
# - o usuario não estiver bloqueado
# - hora atual estiver entre 8h e 18h

# permitir entrada 
# - admin 

usuario_funcionario = True
usuario_bloqueado = False
hora_atual = 17
usuario_admin = False
hora_comercial = hora_atual >=8 and hora_atual <= 18
funcionario_ativo = usuario_funcionario and not usuario_bloqueado

if  usuario_admin or (funcionario_ativo and hora_comercial):
    print('acesso permitido')

idade = 25
maior_idade = idade >= 18 # True
# operadores de comparação
# ==, !=, >, <, >=, <=
# comparando valores iguais

if media >= 6.0:
    print('aprovado')

# is, is not
# operador de identidade
# comparar se os objetos ocupam o mesmo 
# espaço de memória   

a = [1, 2, 3] 
b = [1, 2, 3] 

print(a == b) # True
print(a is b) # False

c = b
print(c is b) # True


# operador in, not in
# verificar se um elemento existe ou não em uma sequência
# str, lis, tuple

opcoes = ('sim', 'não', 'talvez')
opcao = input('Digite uma opção') #"   Sim   "
opcao = opcao.lower()             #"   sim   "
opcao = opcao.strip()             #"sim"


if opao in opcoes:
    print('ok')
else:
    print('não tem essa opção')


numeros = [1, 3, 5, 6]

for numero in numeros:
    print(numero)
