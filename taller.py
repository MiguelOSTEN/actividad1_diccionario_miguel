 
     
estudiantes = []

pendiente = []
while True:
    codigo = input("Ingrese el código del estudiante: ")
    nombres = input("Ingrese los nombres del estudiante: ")
    apellidos = input("Ingrese los apellidos del estudiante: ")
    contactos = input("Ingrese los contactos del estudiante: ")
    correos = input("Ingrese los correos del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    estrato = int(input("Ingrese el estrato del estudiante: "))
    sexo = input("Ingrese el sexo del estudiante (masculino/femenino): ")
    direccion = input("Ingrese la dirección del estudiante: ")
    telefono = input("Ingrese el teléfono del estudiante: ")

    # Verificar si el estudiante cumple los criterios
    if (sexo.lower() == "masculino" and 15 <= edad <= 25 and 1 <= estrato <= 2) or (sexo.lower() == "femenino" and 20 <= edad <= 35 and 1 <= estrato <= 4):
       
        estudiantes.append({
            "Código": codigo,
            "Nombres": nombres,
            "Apellidos": apellidos,
            "Contactos": contactos,
            "Correos": correos,
            "Edad": edad,
            "Estrato": estrato,
            "Sexo": sexo,
            "Dirección": direccion,
            "Teléfono": telefono
        })
    else:
        # Agregar el estudiante a la lista de pendientes
        pendiente.append({
            "Código": codigo,
            "Nombres": nombres,
            "Apellidos": apellidos,
            "Contactos": contactos,
            "Correos": correos,
            "Edad": edad,
            "Estrato": estrato,
            "Sexo": sexo,
            "Dirección": direccion,
            "Teléfono": telefono
        })

    respuesta = input("¿Desea capturar información de otro estudiante? (s/n): ")
    if respuesta.lower() != "s":
        break

# Imprimir la lista de estudiantes que cumplen los criterios
print("Estudiantes que cumplen los criterios:")
for estudiante in estudiantes:
    print(estudiante)

# Imprimir la lista de estudiantes pendientes
print("Estudiantes pendientes:")
for estudiante in pendiente:
    print(estudiante)
    
