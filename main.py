# Req. 11: funcion que ejecuta pruebas de validacion
def ejecutar_pruebas():
    print("\n=== EJECUTANDO PRUEBAS ===\n")

    # Prueba 1: datos válidos
    codigo_valido = validar_codigo("12345678")
    print("Prueba 1 - Código válido:", "OK" if codigo_valido else "FALLÓ")

    # Prueba 2: código vacío
    codigo_vacio = validar_codigo("")
    print("Prueba 2 - Código vacío detectado:", "OK" if not codigo_vacio else "FALLÓ")

    # Prueba 3: tipo de consulta incorrecto
    tipo_incorrecto = validar_tipo_consulta("base de datos")
    print("Prueba 3 - Tipo incorrecto detectado:", "OK" if not tipo_incorrecto else "FALLÓ")

    # Prueba 4: prioridad alta
    prioridad_alta = asignar_prioridad("pagos")
    print("Prueba 4 - Prioridad alta (pagos):", "OK" if prioridad_alta == "Alta" else "FALLÓ")

    # Prueba 5: prioridad baja
    prioridad_baja = asignar_prioridad("constancia")
    print("Prueba 5 - Prioridad baja (constancia):", "OK" if prioridad_baja == "Baja" else "FALLÓ")

    print("\n=== FIN DE PRUEBAS ===\n")
# Req. 7: funcion sin retorno - muestra resumen de la solicitud
def mostrar_resumen(solicitud):
    print("\n--- Resumen de la solicitud ---")
    print("Código:", solicitud["codigo"])
    print("Nombre:", solicitud["nombre"])
    print("Tipo de consulta:", solicitud["tipo_consulta"])
    print("Descripción:", solicitud["descripcion"])
    print("Prioridad:", solicitud["prioridad"])
    print("-------------------------------\n")
# Req. 5: funcion con retorno - asigna prioridad segun tipo de consulta
def asignar_prioridad(tipo_consulta):
    if tipo_consulta == "plataforma":
        return "Alta"
    elif tipo_consulta == "pagos":
        return "Alta"
    elif tipo_consulta == "matricula":
        return "Media"
    elif tipo_consulta == "constancia":
        return "Baja"
    else:
        return "Baja"
# Req. 4: funcion sin retorno - muestra el menu principal
def mostrar_menu():
    print("=== Sistema de Orientación y Registro de Atenciones ===")
    print("1. Registrar nueva solicitud")
    print("2. Salir")
# Req. 2: funcion con retorno - valida codigo de estudiante
def validar_codigo(codigo, longitud_minima=6):
    if codigo.strip() == "":
        return False
    if len(codigo) < longitud_minima:
        return False
    return True
# Req. 6: funcion con retorno - valida que un texto no este vacio
def validar_texto_obligatorio(texto):
    return texto.strip() != ""

# Req. 3: funcion con retorno - valida tipo de consulta
def validar_tipo_consulta(tipo_consulta):
    tipos_validos = ["matricula", "pagos", "constancia", "plataforma", "otro"]
    return tipo_consulta.strip().lower() in tipos_validos

# Req. 1: registra los datos basicos de una solicitud
# Req. 8 y 9: los datos se pasan como parametros entre funciones,
# sin variables globales. Las variables (codigo, nombre, etc.) son
# locales a cada funcion.

def registrar_solicitud():
    codigo = input("Código de estudiante: ")
    while not validar_codigo(codigo):
        print("Código inválido. Debe tener al menos 6 caracteres y no estar vacío.")
        codigo = input("Código de estudiante: ")

    nombre = input("Nombre: ")
    while not validar_texto_obligatorio(nombre):
        print("El nombre no puede estar vacío.")
        nombre = input("Nombre: ")

    tipo_consulta = input("Tipo de consulta (matricula/pagos/constancia/plataforma/otro): ")
    while not validar_tipo_consulta(tipo_consulta):
        print("Tipo de consulta inválido. Opciones: matricula, pagos, constancia, plataforma, otro.")
        tipo_consulta = input("Tipo de consulta (matricula/pagos/constancia/plataforma/otro): ")

    descripcion = input("Descripción breve: ")
    while not validar_texto_obligatorio(descripcion):
        print("La descripción no puede estar vacía.")
        descripcion = input("Descripción breve: ")

    prioridad = asignar_prioridad(tipo_consulta)

    solicitud = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo_consulta": tipo_consulta,
        "descripcion": descripcion,
        "prioridad": prioridad
    }
    return solicitud

if __name__ == "__main__":
    ejecutar_pruebas()
    
    solicitudes = []

    for i in range(3):
        print(f"\n--- Registrando solicitud N° {i + 1} ---")
        solicitud = registrar_solicitud()
        solicitudes.append(solicitud)
        mostrar_resumen(solicitud)

    print(f"\nSe registraron {len(solicitudes)} solicitudes en total.")