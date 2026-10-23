nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuál es tu edad? "))
calificacion = float(input("¿Cuál es tu calificación? "))
calificacion2 = float(input("¿Cuál es tu calificación? "))
calificacion3 = float(input("¿Cuál es tu calificación? "))
promedio = (calificacion + calificacion2 + calificacion3) / 3
print("El promedio es:", round(promedio, 1))

if promedio == 100:
    print("Te explotaste")
elif promedio >= 71:
    print("Aprobaste")
else:
    print("Reprobaste")