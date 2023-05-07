def busca(lista):
    cont=0
    dominio=input("Ingrese dominio a buscar:")
    for j in lista:
        if(j.getDominio()==dominio):
            cont+=1
    print(f"Hay {cont} objetos de la clase Email con el mismo dominio al ingresado")