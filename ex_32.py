#3.3 Escriba un programa para solicitar una puntuación entre 0.0 y 1.0. Si el puntaje está fuera de rango, imprima un error. 
# Si el puntaje está entre 0.0 y 1.0, imprima un grado usando la siguiente tabla:
#Score Grado
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#Si el usuario ingresa un valor fuera de rango, imprima un mensaje de error adecuado y salga. Para probar el código, 
# ingrese un puntaje de 0.85.
punt = input("Puntuación: ")
p = float(punt)
if (p >= 0.9):
    print("A")
elif (p >= 0.8):
    print("B")
elif (p >= 0.7):
    print("C")
elif (p>= 0.6):
    print("D")
else:
    print("F")
