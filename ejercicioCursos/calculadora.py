while True:
 def num():
    global num1
    global num2
    num1 = int(input("Ingresa el número uno"))
    num2 = int(input("Ingresa el número uno"))

 def sumar():
    num()
    suma = num1 + num2
    print(f"El resultado entre {num1} y {num2} es {suma}")


 def restar():
    num()
    resta = num1 - num2
    print(f"El resultado entre {num1} y {num2} es {resta}")

 def multiplicar():
    num()
    mul = num1 * num2
    print(f"El resultado entre {num1} y {num2} es {mul}")

 def división():
    num()
    div = num1 / num2
    print(f"El resultado entre {num1} y {num2} es {div}")

 
 print("Escoge una opción")
 str(print("Sumar"))
 str(print("Dividir"))
 str(print("Multiplicar"))
 str(print("División"))
 opc = str(input())
 
 if opc == "Sumar" or opc =="sumar":
    sumar()
 elif opc == "Restar" or opc == "restar":
    restar()
 elif opc == "Multiplicar" or opc == "multiplicar":
    multiplicar()
 elif opc == "Dividir" or opc == "dividir":
    división()
 elif opc == "Salir" or opc == "salir":
    print("Hasta luego")
    break
 else:
    print("Opción incorrecta")


