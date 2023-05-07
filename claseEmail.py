class Email:
    def __init__(self, id, dominio, tipodominio, contr):
        self.__idCuenta = id
        self.__dominio = dominio
        self.__tipoDominio = tipodominio
        self.__contraseña = contr

    def retornaEmail(self):
        return f"{self.__idCuenta}@{self.__dominio}.{self.__tipoDominio}"
    
    def getDominio(self):
        return self.__dominio
    
    def crearCuenta(self, direccion,contra):
        id=direccion.split("@")
        dominio=id[1].split(".")
        nuevomail=Email(id[0],dominio[0],dominio[1],contra)
        return nuevomail
    
    def modificaContraseña(self, contra):
        if contra==self.__contraseña:
            self.__contraseña=input("Ingresa nueva contraseña: ")
        else:
            print("Contraseña incorrecta")

