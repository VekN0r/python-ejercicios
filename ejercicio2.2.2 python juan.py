print("Bienvenido al mundo de la programación")
nom = str(input("Para comenzar, ingresa tu nombre:"))
print(f"Bienvenido {nom}")

x = int and float(input(f"Ingresa un dato númerico para resolver la ecuacion: ")) 
print(f"El resultado es el siguiente: {(x ** 2 + (3 * x) + 1) / 4 }")

#etapa 4
while True:
 respuesta = str(input("¿Desea conservar su nombre de arriba?"))

 if respuesta == "Si" or respuesta == "si":
    print("Continuaras con tu primer nombre ingresado")
    break
    
 else:
    if respuesta == "No" or respuesta == "no":
        nom = str(input("Ingresa tu nombre y apellido: "))
    
rut = str(input("Ingrese su rut: "))
correo = str(input("Ingrese su correo: "))
telefono = str(input("Ingrese su número telefonico: "))
telefono = telefono.replace("+56", "")

print(f"NOMBRE:\t\t {nom.upper()}\nRUT:\t\t {rut.upper()}\nCORREO:\t\t {correo.upper()}\nTELEFONO:\t {telefono.upper()}")