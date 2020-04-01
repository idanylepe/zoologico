lista_animal=[]
lista_tipo=[]
lista_mkgasto=[]
class Animal: 
    def init(self, nombre, tipo):
        self.nombre = nombre
        self.tipo   = tipo
       
    def set_nombre(self,nombre): 
        self.nombre = nombre
          
    def get_nombre(self):
        print(self.nombre)
        self.get_miprueba()

def Menu():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Que opcion deseas?....: "))
            correcto=True
        except ValueError:
            print('Error, intenta de nuevo')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("\n \n1. Añadir animal")
    print ("2. Ver la lista")
    print ("3. Realizar cambio en lista")
    print ("4. Salir") 
    print ("Elige una opcion")
 
    opcion = Menu()
 
    