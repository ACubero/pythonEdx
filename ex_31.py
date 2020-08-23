horas = input("Introduzca horas:")
h = float(horas)
tarifa = input("Introduzca tarifa: ")
t = float(tarifa)
if h <= 40:
    total = h * t
else:
    totalhoranormales = 40 * t
    totalhorasextra = (h - 40) * (t * 1.5)
    total = totalhoranormales + totalhorasextra
print(total)
