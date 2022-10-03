#Ejercicio 7.Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
min= 0
horas= 0

min= (int)(input("Dime los minutos \n"))
print(f"Los {min} minutos son {int(min/60)} horas y {min%60} minutos")