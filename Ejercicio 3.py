#Ejercicio 3. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
cateto1=0
cateto2=0
hipotenusa=0


print("Calculadora de hipotenusa \n")
cateto1= (int)(input("Dime la longitud de un cateto \n"))
cateto2= (int)(input("Dime la longitud de otro cateto \n"))
print("La hipotenusa es:", ((cateto1**2)+(cateto2**2))**(0.5))
