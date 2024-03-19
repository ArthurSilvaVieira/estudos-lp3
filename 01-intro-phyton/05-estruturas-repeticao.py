#   for

palavra = 'Python'
for letra in palavra:
    print(letra)

numeros = [1,2,3,4,5,6,7,8,9]

for numero in numero:
    print(numero)




#   range 
#   range(stop)
#   range(5) - 0,1,2,3,4

#   range(start, stop)
#   range(4,10) - 4,5,6,7,8,9

#   range(star, stop, step)
#   range(3, 10, 2) - 3,5,7,9

for i in range(10):
    print(i)


#   while


contador = 0
while contador < 5:
    print(contador)
    contador +=1


#   break
#   break pula o loop
#   encontrar o primeiro numero par
numeros = [1,3,3,4,6]
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
        break


#   continue
#   pula a interação
for numero in numeros:
    if numero<= 0:
        continue
    print(numero)



#   compreenção de lista
numero = [2,3,4]
quadrados = [4, 9, 16]

for numero in numeros:
    quadrados.append(numero ** 2)

quadrados = [numero ** 2  for numero in numeros]

numero = [1,3,4,5,4,6]
pares = []

for numero in numeros:
    if numero %2 == 0:
        pares.append(numero)

pares = [numero for numero in numeros if numero ]


palavras = ['ola', ' mundo', 'teste']
palavras2 = [palavra.upper() for palavra in palavras]



