massa = float(input('Digite o seu peso em quilogramas: '))
altura = float(input('Digite sua altura em centimetros: '))/100
imc = massa/(altura*altura)
IDEAL = 24.9

print(f'Seu IMC é: {imc:.1f}')

if imc < 18.5:             
    print('Baixo peso')
elif imc>18.5 and imc<IDEAL:     
    print('Peso normal')
elif imc>25.0 and imc<29.9:     
    print('Excesso de peso')
elif imc>30.0 and imc<34.9:
    print('Obesidade de Classe 1')
elif imc>35.0 and imc<39.9:
    print('Obesidade de Classe 2')
else:
    print('Obesidade de Classe 3')

if imc>IDEAL:
    print(f'Perca: {(imc-IDEAL)*altura*altura:.1f} kg para alcançar o ideal(IMC:{IDEAL})')
elif imc<IDEAL:
    print(f'Ganhe: {(IDEAL-imc)*altura*altura:.1f} kg para alcançar o ideal(IMC:{IDEAL})')
elif imc == IDEAL:
    print('Peso Ideal')