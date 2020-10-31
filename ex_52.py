#5.2 Escriba un programa que solicite repetidamente números enteros a un usuario hasta que el usuario ingrese 'hecho'. 
# Una vez que se ingrese 'hecho', imprima el más grande y el más pequeño de los numeros. Si el usuario ingresa algo que 
# no sea un número válido, atrápelo con un try / except y envíe un mensaje apropiado e ignore el número. Ingrese 7, 2, 
# bob, 10 y 4 y haga coincidir la salida a continuación.
numeros = []
largest = None
smallest = None
while True:
    num = input("Ingrese un número: ")
    if num == "hecho" : break
    try:
        inum = int(num)
        numeros.append(inum)
    except:
        print("Valor inválido")
largest = numeros[0]
smallest = numeros[0]
for numero in numeros:
    if numero < smallest:
        smallest = numero
    if numero > largest:
        largest = numero 

print("Máximo es", largest)
print("Mínimo es", smallest)
