##Grupo #1 Password Manager
# Jorge Azmitia
# Cristina Bautista
# Sebastian Maldonado
# Abril Palencia
# Cesar Rodas

from keychain import *
import random



ans=True
while ans:
    print ("""
        Password Manager
        \n""")
    password = input("\nIngrese la clave maestra: ")

    k = Keychain()

    k.init(password)
    
    isload = k.load("holi", None, None)
    
    # si isload = true se ejecutan las opciones del programa, sino se vuelve a solicitar la clave maestra.
    while isload:
        
        choice = int(input(
            """
            1. Ingresar/actualizar sitio - contraseña
            2. Consultar sitio - contraseña
            3. Eliminar sitio del gestor
            4. Salir\n"""))

        print("choice---->", choice)

        if choice==1:
            # solicitar datos sitio y contraseña y guardarlos
            print("holi ingresar")
        elif choice==2:
            # solicitar sitio y mostrar la contraseña
            print("holi consultar")
        elif choice==3:
            # solicitar sitio y eliminarlo
            print("holi elimniar")
        elif choice==4:
            # salir
            print("salir")
            ans = False
            isload = False
            exit()
