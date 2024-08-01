comprimento = float(input('Insira o comprimento do seu aquário em centimetros: '))
altura = float(input('Insira a altura do seu aquário em centimetros: '))
largura = float(input('Insira a largura do seu aquário em centimetros: '))
volume = (comprimento * altura * largura) / 1000.0
temperatura_ambiente = float(input('Insira a temperatura ambiente em °C: '))
temperatura_desejada = float(input('Insira a temperatura desejada em °C: '))
potencia = volume * 0.05 * (temperatura_desejada - temperatura_ambiente)
filtragem_min1 = volume * 2
filtragem_min2 = volume * 3

print(f'O volume é: {volume} litros')
print(f'A potência necessária para o termostato é: {potencia} Watts')
print(f'A quantidade de filtragem deve ser no mínimo: {filtragem_min1} litros/hora ou {filtragem_min2} litros/hora')