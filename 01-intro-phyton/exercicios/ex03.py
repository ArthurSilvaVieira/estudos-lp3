Compra = 7999.9


if Compra >= 0.01 and Compra < 10:
    Desconto = 0
elif Compra <100:
    Desconto =20
    
elif Compra <500:
    Desconto = 10
else:
    Desconto = 15

valor_final = Compra*(1-(Desconto/100))

print(f'Valor com desconto: R$ {valor_final}, Desconto: {Desconto}%')    