'''

Obtener el precio final que se tiene que pagar si se
aplica el 36% de descuento del total de la compra.

'''


compra = float(input("Ingrese el precio de la compra: "))
descuento = (compra*36)/100
pFinal = compra-descuento
print(f"El precio final con descuento es: {pFinal:.1f}")