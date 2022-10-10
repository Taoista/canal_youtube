
def calculo_impuesto(precio):
    impuesto = 0.19
    return precio * impuesto

def calculo_total(a, b):
    return a + b

precio = 3500
impuesto = calculo_impuesto(precio)
total = calculo_total(precio, impuesto)

print(total)
