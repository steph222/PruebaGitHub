

# Pedir la cantidad de exámenes
cantidad_examenes = 3

# Pedir notas
nota1 = int(input("Ingrese la nota del examen #1: "))
nota2 = int(input("Ingrese la nota del examen #2: "))
nota3 = int(input("Ingrese la nota del examen #3: "))

# Calcular el promedio
promedio = (nota1 + nota2 + nota3) / cantidad_examenes

# nota 
print(f"\nLa nota final del estudiante es: {promedio:.2f}")

# Ver el resultado
if promedio >= 70:
    print("El estudiante aprobó el curso.")
elif promedio >= 60:
    print("El estudiante debe ir a ampliación.")
else:
    print("El estudiante reprobó el curso.")
