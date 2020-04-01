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
 
    if opcion == 1:
     a=int (input ("Cuantos animales quieres añadir? \n"))
     for x in range (a):
            oof=input("Dame el nombre del animal \n")
            lista_animal.append(oof)
            p_tipo=input("Que tipo de animal es?\n")
            lista_tipo.append(p_tipo)
    elif opcion == 2:
        lista_mkgasto = lista_animal+lista_tipo
        for element in lista_mkgasto:
         print (element)
    elif opcion == 3:
        cambio= int(input ("Deseas cambiar algo en una de las dos listas?\n1.Si\n2.No\n"))
        if cambio== 1:
         decision= input("A los nombres o a los tipos de los animales?\n ")
         if decision==("nombres"):
          for element in lista_animal:
           print(lista_animal.index(element), element)          
          b=int (input("Dame el id del animal que quieres cambiar\n"))
          lista_animal[b] = input("Nombre nuevo del animal?\n")
          print ("Lista nueva")
          for element in lista_animal:
           print (element)
         if decision==("tipos"):
          for element in lista_tipo:
           print(lista_tipo.index(element), element)          
          b=int (input("Dame el id del tipo de animal que quieres cambiar\n"))
          lista_tipo[b] = input("Nombre nuevo del animal?\n")
          print ("Lista nueva")
          for element in lista_tipo:
           print (element)
         
        if cambio== 2:
         print("")
    elif opcion == 4:
        salir = True
    else:
        print ("Esa no es una opcion, intenta de nuevo")
 
print ("Fin")