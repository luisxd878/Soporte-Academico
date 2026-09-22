def validar_codigo(codigo, longitud_minima=6):
    if codigo.strip() == "":
        return False
    if len(codigo) < longitud_minima:
        return False
    return True
def registrar_solicitud():
    codigo = input("Código de estudiante: ")
    while not validar_codigo(codigo):
        print("Código inválido. Debe tener al menos 6 caracteres y no estar vacío.")
        codigo = input("Código de estudiante: ")

    nombre = input("Nombre: ")
    tipo_consulta = input("Tipo de consulta: ")
    descripcion = input("Descripción breve: ")

    solicitud = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo_consulta": tipo_consulta,
        "descripcion": descripcion
    }
    return solicitud
if __name__ == "__main__":
    solicitud = registrar_solicitud()
    print(solicitud)