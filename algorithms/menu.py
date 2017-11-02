"""Menu."""
numero1 = float(input('Ingresa el primer numero'))
numero2 = float(input('Ingresa el segundo numero'))

print("""Eliga una opción\n[1]Sumar ambos numeros
[2]Restar el primero menos el segundo
[3]Multiplicar los numeros""")

opcion = int(input('Ingrese su opción'))

if opcion == 1:
    print(numero1 + numero2)
elif opcion == 2:
    print(numero1 - numero2)
elif opcion == 3:
    print(numero1 * numero2)
else:
    print('Opción inexistente')
