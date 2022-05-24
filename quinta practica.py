# def suma(a, b):
#    print("se sumas dos numeros")
#    resultado = a + b
#    return resultado

#sumatoria = suma(1, 4)
#print(sumatoria)

def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿cuantos pesos" + tipo_pesos + " tienes?:  ")
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares = round(dolares,  2)
    dolares = str(dolares)
    print("tienes $"  +  dolares  +  " dolares ")

menu = """  
Bienvenido al conversor de monedas

1 - pesos colombianos
2 - pesos argentinos
3 - pesos mexicanos

Elije una opcion: """

opcion = int(input(menu))


if opcion ==  1:
    conversor("colombiano", 3875)
elif opcion == 2:
    conversor("argentinos", 65) 
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print("ingresa una opcion correcta por favor")

