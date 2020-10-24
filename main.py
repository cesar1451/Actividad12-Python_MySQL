import mysql.connector

#Conectar a la base de datos
bd = mysql.connector.connect(
    user='Cesar', password='Cesar14ilse21', database='nopalito')

#Hacer consultas, inserciones o consultas en la base de datos
cursor = bd.cursor()

while True:
    print("1) Agregar usuario")
    print("2) Mostrar usuarios")
    print("0) Salir")
    opc = input("Ingresa una opción: ")
    
    if opc == '1':
        #Pedir datos
        nombre = input("Ingresa el nombre: ")
        email = input("Ingresa el correo: ")
        contra = input("Ingresa la contraseña: ")
        
        #Insertar los datos a la base de datos
        consulta = "INSERT INTO usuario (nombre, email, pass) VALUES (%s, %s, %s)"
        cursor.execute(consulta, (nombre, email, contra)) #Intentar insertar en la tabla
        bd.commit() #Guardar los datos (información)
        if cursor.rowcount: #Nos dice cuantas filas se modificaron por lo que regresa 1 (1 fila modificada)
            print("Se agregó usuario.")
        else:
            print("Error.")
    
    elif opc == '2':
        consulta = "SELECT * FROM usuario" #Hacer consulta
        cursor.execute(consulta) #Crear la consulta
        for row in cursor.fetchall(): #Sacar los datos o resultas y genera una lista la funcion fetchall()
            print("id: ", row[0])
            print("Nombre: ", row[1])
            print("Email: ", row[2])
            print("Contraseña: ", row[3], '\n')
            
    elif opc == '0':
        print("Gracias por utilizar el programa, hasta luego.")
        break
    else:
        print("Error. No se encontro la opción elegida.")

bd.close() #Cerrar base de datos