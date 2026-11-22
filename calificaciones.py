estudiantes = int(input("cuantos estudiantes tiene el grupe??"))
materias = int(input("cuantas materies tienen??"))

calificaciones = []

for file in range(estudiantes):
    estudiante = []
    print(f"estudiante {file + 1}")

    for columnes in range(materias):
        nota = float(input(f"calificacion de la materie {columnes + 1}:"))

        while nota < 0 or nota > 100:
            print("la calificacion debe de estar entre 0 y 100")
            nota = float(input(f"calificacion de la materie: {columnes +1}"))

        estudiante.append(nota)

    calificaciones.append(estudiante)

print("promedie de los estudiantes")

for file in range(estudiantes):
    promedio = sum(calificaciones[file])/ materias
    print(f"estudiante {file + 1}: {promedio:.2f}")


print("promedie de materie")

for columnes in range(materias):
    suma = 0

    for file in range(estudiantes):
        suma += calificaciones[file][columnes]

    promedio = suma / estudiantes
    print(f"materie {columnes + 1}: {promedio:.2f}")

mayor = calificaciones[0][0]
menor = calificaciones[0][0]

for file in range(estudiantes):
    for columnes in range(materias):
        nota = calificaciones[file][columnes]

        if nota > mayor:
            mayor = nota

        if nota < menor:
            menor = nota

print("calificaciones mas altes y mas bajes")
print(f"calificacion mas alte: {mayor}")
print(f"calificacion mas baje: {menor}")