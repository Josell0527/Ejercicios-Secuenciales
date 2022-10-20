#Ejercicio1. Escribir un programa que pregunte al usuario su nombre, y luego lo salude
def ej1():
    nombre= ""
    nombre= input("Dime tu nombre, \n")
    print("Hola", nombre)
def ej2():
    base=0
    altura= 0 

    print ("Cálculo del perimetro de un rectángulo")
    base= (int) (input("Dime la base del rectángulo, \n"))
    altura= (int) (input("Dime la altura del rectángulo, \n"))
    print ("El perímetro del rectángulo es:", ((base*2) + (altura*2)))

    print ("Cálculo del área de un rectángulo")
    base= (int) (input("Dime la base del rectángulo, \n"))
    altura= (int) (input("Dime la altura del rectángulo, \n"))
    print ("El área del rectángulo es:", (base*altura))