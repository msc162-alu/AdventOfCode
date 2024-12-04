def leerArchivo(der, izq):
    archivo = open("01.txt", "r")

    for linea in archivo.readlines():
        linea = linea.strip()
        izq.append(int(linea.split()[0]))
        der.append(int(linea.split()[1]))

    archivo.close()

def main():
    izq = []
    der = []

    leerArchivo(der, izq)

    fin = 0
    
    while len(izq) > 0:

        minI = izq[0]
        minD = der[0]

        for i in range(len(izq)):
            if izq[i] <= minI:
                minI = izq[i]

        for i in range(len(der)):
            if der[i] <= minD:
                minD = der[i]
        
        fin += abs(minI - minD)

        izq.remove(minI)
        der.remove(minD)
    
    print("Solucion primer ejercicio: ", fin)   

    # Ejercicio 2

    fin = 0

    exist = []
    howMany = []

    leerArchivo(der, izq)
    
    for i in range(len(izq)):

        if izq[i] in exist:
            fin += howMany[exist.index(izq[i])]
            continue

        count = 0
        for j in range(len(der)):
            if izq[i] == der[j]:
                count += 1
        exist.append(izq[i])
        howMany.append(count * izq[i])
        fin += count * izq[i]
            

    
    print("La suma es: ", fin)   





if __name__=="__main__":
    main()