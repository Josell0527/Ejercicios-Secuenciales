#Ejercicio 20. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)después de pedirnos cuantas monedas 
#tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).
monedas2=0
monedas1=0
centimos50=0
centimos20=0
centimos10=0

monedas1= (int)(input("Dime las monedas de 1€: \n"))
monedas2= (int)(input("Dime las monedas de 2€: \n"))
centimos50= (int)(input("Dime los céntimos de 50: \n"))
centimos20= (int)(input("Dime los céntimos de 20: \n"))
centimos10= (int)(input("Dime los céntimos de 10: \n"))
print("Total:", (monedas1*1)+(monedas2*2), "euros", "y", ((centimos50*50)+(centimos20*20)+(centimos10*10)), "céntimos")