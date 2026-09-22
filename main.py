def mostrar_resumen(solicitud):
    print("\n--- Resumen de la solicitud ---")
    print("Código:", solicitud["codigo"])
    print("Nombre:", solicitud["nombre"])
    print("Tipo de consulta:", solicitud["tipo_consulta"])
    print("Descripción:", solicitud["descripcion"])
    print("Prioridad:", solicitud["prioridad"])
    print("-------------------------------\n")
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
def mostrar_menu():
    print("=== Sistema de Orientación y Registro de Atenciones ===")
    print("1. Registrar nueva solicitud")
    print("2. Salir")
def validar_codigo(codigo, longitud_minima=6):
    if codigo.strip() == "":
        return False
    if len(codigo) < longitud_minima:
        return False
    return True
def validar_texto_obligatorio(texto):
    return texto.strip() != ""

def validar_tipo_consulta(tipo_consulta):
    tipos_validos = ["matricula", "pagos", "constancia", "plataforma", "otro"]
    return tipo_consulta.strip().lower() in tipos_validos

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
    solicitud = registrar_solicitud()
    mostrar_resumen(solicitud)