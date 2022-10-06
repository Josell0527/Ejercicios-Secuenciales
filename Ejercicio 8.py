#Ejercicio 8. Un vendedor recibe un sueldo base mas un 10% extra por comisión de susventas, el vendedor desea saber cuanto dinero obtendrá por concepto de
#comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
venta1= 0
venta2= 0
venta3= 0
salario=0

venta1= (int)(input("Dime los dineros de la venta 1 \n"))
venta2= (int)(input("Dime los dineros de la venta 2 \n"))
venta3= (int)(input("Dime los dineros de la venta 3 \n"))
salario= (int)(input("Dime el salario: \n"))
print("Comisiones:", ((venta1+venta2+venta3)*1.1))
print("El salario total es de:", (((venta1+venta2+venta3)*1.1)+salario), "€")
