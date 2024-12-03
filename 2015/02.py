def leerArchivo(cajas):
    archivo = open("02.txt", "r")

    for linea in archivo.readlines():
        linea = linea.strip()
        cajas.append(linea)

    archivo.close()

cajas = []
leerArchivo(cajas)
fin = 0

for i in cajas:
    x = i.split("x")
    print(x)
    fin += (2*int(x[0])*int(x[1]))+(2*int(x[1])*int(x[2]))+(2*int(x[2])*int(x[0]))
    fin += min(int(x[0])*int(x[1]), int(x[1])*int(x[2]), int(x[2])*int(x[0]))	

print("Solucion primer ejercicio: " + str(fin))