# if
# if condição
#     codigo
#     codigo
# codigo
 
idade = 20
if idade >= 18:
    print()


# if/else

if idade >= 18:
    print('maior de idade')
    print('fasfdads')
else:
    print("menor de idade")    


#if/elif/else
# criança 0 a 12, adolescente 13 a 17,
# adulto 18 a 59, idoso 60+

if idade > 0 and idade <= 12:
    print('criança')
if idade > 12 and idade <= 17:
    print('adolescente')
if idade > 18 and idade <= 59:
    print('adulto')
if idade > 60:
    print('idoso')



if idade <= 12:
    print('criança')
elif idade <= 17:
    print('adolescente')
elif idade <= 59:
    print('adulto')
else:
    print('idoso')  


# condições aninhadas

email = 'admin@email.com'
senha = '123'

if email == 'admin@email.com' and senha == '123':
    print('liberado')
else:
    print('erro')




# entrada email, senha
# saída True ou False
def liberar_acesso(email, senha):
    return email == 'admin@email.com' and senha == '123'


# entrada hora_atual
# sim ou não
def dentro_horario_comercial(hora_atual):
    return hora_atual >= 8 and hora_atual <=18




# dia 1, 2, 3, 4, 5, 6, 7
# palavra  domingo, segunda, terça, quarta, quinta, sexta, sábado

dia = 3

dias = {
    1: 'domingo',
    2: 'segundo',
    3: 'terça',
}

errors = {
    404: "sfsf"
}

if dia in dias:
    print(dias[dia])

for valor in dias.values():

    print(valor)