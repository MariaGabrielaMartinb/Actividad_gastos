Gastos = [20, 15, 50, 10, 5, 80, 12] #lista de gastos semanal
total = 0 #variable para almacenar el total de gastos, 0 porq aun no hemos sumado nada
for gasto in Gastos: #recorremos la lista de gastos
    total = total + gasto #sumamos cada gasto al total
print("El total de gastos es:", total)

Media = int(total / len(Gastos)) #divide el total entre el numero de gastos
print("La media de gastos es:", Media)

for gasto in Gastos: #recorre toda la lista de gastos
    if gasto > 20: #comprueba si el gastos es mayor que 20
        print("Gasto mayor que 20:", gasto) #imprimimos los gastos mayores que 20

presupuesto = 100 #Limite de presupuesto
if total > presupuesto: #verificamos si el total es mayor a los 100
    print("Has superado el presupuesto semanal") 
else: #si no es mayor a 100
    print("Aun te queda presupuesto semanal")    

