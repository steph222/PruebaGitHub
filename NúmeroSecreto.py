
#defino mis variables nombre, apellido, y número 

Numero_Secreto= 8
nombre= input ("ingrese su nombre:  ")
apellido=input("ingresa tu apellido:")

edad=input("ingrese su edad : ")

#Ahora las condiciones 

N_del_usu= int(input("Adivina el número secreto (entre 1 y 50):"))

#verificar el 

if N_del_usu == Numero_Secreto:
    print(f"FELICIDADES{nombre}{apellido} Ganaste, adivinaste cual era nuestro número secreto")
else:
    print("Gracias por participar, vuelve a interlo luego.")




