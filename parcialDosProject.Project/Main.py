
salario_base = int(input("Ingrese el salario base $: "))
cargo = input("Ingrese el cargo (directivo/operativo): ")
desempeño = input("Ingrese el desempeño (alto/medio/bajo): ")



def calcular_bonificacion(salario_base, cargo, desempeño):
    if cargo.lower() == "directivo":
        if desempeño.lower() == "alto":
            bonificacion = salario_base * 0.20
        elif desempeño.lower() == "medio":
            bonificacion = salario_base * 0.10
        else:
            bonificacion = 0
    elif cargo.lower() == "operativo":
        if desempeño.lower() == "alto":
            bonificacion = salario_base * 0.15
        elif desempeño.lower() == "medio":
            bonificacion = salario_base * 0.05
        else:
            bonificacion = 0
    else:
        return "cargo no válido"

    total_a_recibir = salario_base + bonificacion
    return total_a_recibir, bonificacion


salario_base = 3000000  # Salario base del empleado
cargo = "directivo"  # Nivel del empleado
desempeño = "alto"  # Desempeño del empleado

total, bonificacion = calcular_bonificacion(salario_base, cargo, desempeño)


# Imprimir
print("-----Resumen del Pago-----")
print(f"Cargo: {cargo.capitalize()}")
print(f"Nivel de Desempeño: {desempeño.capitalize()}")
print(f"Salario Base: ${salario_base.capitalize()}")
print(f"Bonificación: ${bonificacion.capitalize()}")
print(f"Total a Recibir: ${total, bonificacion.capitalize()}")
print("------------------------------------\n")





