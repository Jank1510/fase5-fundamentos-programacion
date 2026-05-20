# Fase 5 - Evaluación Final POA
# Curso: Fundamentos de Programación
# Problema 5: Cálculo de horas semanales por recurso

def calcular_jornada(horas):
    """
    Función que recibe una lista con las horas trabajadas
    de lunes a viernes, calcula el total semanal y clasifica la jornada.
    """
    total_horas = sum(horas)

    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return total_horas, clasificacion


# Matriz con los datos de los recursos
# Formato: [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]
recursos = [
    ["Carlos", 8, 8, 8, 8, 8],
    ["María", 9, 8, 9, 8, 7],
    ["Andrés", 7, 8, 7, 8, 7],
    ["Laura", 10, 9, 8, 9, 8]
]


print("INFORME DE HORAS SEMANALES")
print("=" * 45)

for recurso in recursos:
    nombre = recurso[0]
    horas_trabajadas = recurso[1:]

    total, clasificacion = calcular_jornada(horas_trabajadas)

    print(f"Recurso: {nombre}")
    print(f"Horas trabajadas: {horas_trabajadas}")
    print(f"Total de horas semanales: {total}")
    print(f"Clasificación de jornada: {clasificacion}")
    print("-" * 45)