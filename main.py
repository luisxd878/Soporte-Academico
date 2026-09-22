def registrar_solicitud():
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
    