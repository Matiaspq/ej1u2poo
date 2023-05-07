import csv
from claseEmail import Email
def creadArchivo(lista):
    archivo = open('archivo.csv')
    reader = csv.reader(archivo, delimiter=',')
    print("\n----------------Archivo---------------")
    for fila in reader:
        for i in range(len(archivo)):
            if "@" in fila[0]:
                if "." in fila[0]:
                    print ("Si tiene @ y .")
    """else: print(f"Direccion: {fila} no valida.")"""