estudiantes_list = []
matricula = 0


def crear_estudiante():
    global matricula
    matricula += 1
    nombre = str(input("Ingrese nombre:")).strip()
    edad = int(input("Ingrese edad: "))
    carrera = str(input("Ingrese carrera: ")).strip()


    estudiante = {
        "matricula": matricula,
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera
    }
    estudiantes_list.append(estudiante)
    imprimir_estudiante(estudiante)
    print("Matricula Cargada")
 
def imprimir_estudiante(estudiante):
    print(f'''
        =========================
        matricula: {estudiante["matricula"]}    
        Nombre: {estudiante["nombre"]}      
        Edad: {estudiante["edad"]}
        Carrera {estudiante["carrera"]}
             ''')    
