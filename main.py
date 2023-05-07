import csv
from claseEmail import Email
from buscaDominio import busca
from creaArchivo import creadArchivo

if __name__ == '__main__':
    listaValidos=[]
    creadArchivo(listaValidos)
    nombre = input("Ingrese nombre: ")
    idCuenta = input("Ingrese ID de la cuenta: ")
    dominio = input("Ingrese dominio de la cuenta: ")
    tipoDominio = input("Ingrese tipo de dominio de la cuenta: ")
    contraseña = input("Ingrese contraseña: ")
    mail=Email(idCuenta,dominio,tipoDominio,contraseña)
    listaValidos.append(mail)
    print(f"Estimado {nombre} te enviaremos tus mensajes a la dirección {mail.retornaEmail()}")
    contraseña=input("Ingresa contraseña actual para modificarla: ")
    mail.modificaContraseña(contraseña)
    correo=input("Ingrese direccion de correo: ")
    contraseña=input("Ingrese contraseña: ")
    n=mail.crearCuenta(correo,contraseña)
    listaValidos.append(n)
    print(n.retornaEmail())
    creadArchivo(listaValidos)
    print("Direcciones válidas creadas: ")
    for i in listaValidos:
            print(i.retornaEmail())
    busca(listaValidos)


            
            
        
        
    
