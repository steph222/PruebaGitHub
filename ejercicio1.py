#variables
nombre=input("ingrese su nombre  ")
edad=int(input("ingrese su edad "))

# aplicar condicional
if edad >= 18:

    
    print(f"{nombre}, puedes conducir.")
    Mayor= True 
    
    
    else:
    print(f"{nombre}, no puedes conducir.")   
    Mayor=False
    
    #si dice que si pregunte
Licencia=input("¿tiene licencia? (si\no):")

if Licencia=="si" and Mayor==True:
    print("tu puedes conducir porque eres mayor y tienes licencia.")
else:
    print("no puedes conducir, no eres mayor de edad y no tienes licencia")
print ("HOLA ")