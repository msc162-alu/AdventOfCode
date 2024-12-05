def leerArchivo(matriz):
    archivo = open("04.txt", "r")

    for linea in archivo:
        linea = linea.strip()
        l = []
        for i in linea:
            l.append(i)
        matriz.append(l)
    archivo.close()


matriz = []
word = "XMAS"
fin = 0

# directions = [N, NE, E, SE, S, SO, O, NO]
directions = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    
leerArchivo(matriz)

tamX = range(len(matriz))
tamY = range(len(matriz[0]))


for x in tamX:
    for y in tamY:
        if matriz[x][y] == word[0]:
            for d in directions:
                lastX = x
                lastY = y
                pal = ""
                pal += word[0]
                try:
                    for l in word[1:]:
                        lastX += d[0]
                        lastY += d[1]
                        if 0>lastX>=tamX or 0>lastY>=tamY:
                            break
                        pal += matriz[lastX][lastY]
                    if pal == word:
                        fin += 1
                except:
                    continue
    
print("Solucion primer ejercicio: " + str(fin))

fin = 0
directions2 = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
p1 = ['M', 'M', 'S', 'S']
p2 = ['M', 'S', 'M', 'S']
p3 = ['S', 'S', 'M', 'M']
p4 = ['S', 'M', 'S', 'M']


for x in tamX:
    for y in tamY:
        if matriz[x][y] == 'A':
            cross = []
            for d in directions2:
                lastX = x+d[0]
                lastY = y+d[1]
                if 0>lastX or lastX>=len(matriz) or 0>lastY or lastY>=len(matriz[0]):
                    break
                cross.append(matriz[lastX][lastY])
                if cross == p1 or cross == p2 or cross == p3 or cross == p4:
                    fin += 1

print("Solucion segundo ejercicio: " + str(fin))

                    