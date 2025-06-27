ticket_list = []   # BD vacia!!!
# --------------------------------------
def crear_ticket():
    # pedir y validar datos
    while True:
        codigo = str(input("Ingrese código:")).strip().upper()
        if validar_codigo(codigo):
            break
    # Propuesto    
    nombre = str(input("Ingrese nombre:")).strip()
    
    while True:
        tipo_entrada = str(input("Ingrese tipo P/G: ")).strip().upper()
        if validar_entrada(tipo_entrada):
            break
    
    while True:
        cantidad = int(input("Ingrese cantidad:"))
        if validar_cantidad(cantidad):
            break
        
    # armar el json
    ticket = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo_entrada": tipo_entrada,
        "cantidad": cantidad
    }
    ticket_list.append(ticket)  #-> se agrega a la BD!!!!
    imprimir_ticket(ticket)  #-> visualizo lo grabado!!!!
    print("...grabo!!!")

#-------------------------------------------------
def imprimir_ticket(ticket):
    print(f'''
        =========================
        Código: {ticket["codigo"]}    
        Nombre: {ticket["nombre"]}      
        Tipo entrada: {ticket["tipo_entrada"]}
        Cantidad: {ticket["cantidad"]}      ''')    

######################################################
######## validadores #################################
def validar_codigo_largo(codigo):
    if len(codigo)!=4:
        print("Debe tener 4 caractes de largo")
        return False # -->no paso la validación
    return True   #--> aprobo la validación

#----------------------------------------------------
def validar_codigo_unico(codigo):
    for ticket in ticket_list:
        if ticket["codigo"]== codigo:
            print("El código ya esta registrado")
            return False
    return True    

#----------------------------------------------------
def validar_codigo(codigo):
    if not validar_codigo_largo(codigo):
        return False
    if not validar_codigo_unico(codigo):
        return False    
    return True

#--------------------------------------------------
def validar_entrada(tipo_entrada):
    if tipo_entrada in ["P", "G"]:
        return True
    else:
        print("Debe ser P(platea) o G(general)")
        return False
    
#--------------------------------------------
def validar_cantidad(cantidad):
    if cantidad>0:
        return True
    else:
        print("Debe ser maoyor a cero!!!")
        return False
            
#----------------------------------------------------------
def consultar_por_comprador():
    encontrado = False
    if not ticket_list:
        print("NO se han vendido entradas!!!!")            
    else:
        nombre = str(input("Ingrese nombre:")).strip()
        for ticket in ticket_list:
            if ticket["nombre"] ==nombre:
                encontrado = True
                imprimir_ticket(ticket)
        if encontrado == False:
            print(f"No hay entradas asociadas a {nombre}")    
    
#----------------------------------------------------------
def anular_compra():
    encontrado = False
    if not ticket_list:
        print("NO se han vendido entradas!!!!")            
    else:
        print("VAMOS A ANULAR LA COMPRA!!!!")
        nombre = str(input("Ingrese nombre:")).strip()
        for ticket in ticket_list:
            if ticket["nombre"] ==nombre:
                encontrado = True
                ticket_list.remove(ticket)
                print("...eliminado!!!!")
        if encontrado == False:
            print(f"No hay entradas asociadas a {nombre}")     
