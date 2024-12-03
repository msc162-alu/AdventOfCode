def gestionMul(txt):
    fin = 0
    x = txt.split("mul(")

    for fragment in x:
        y = fragment.split(")")[0]
        if not y[0].isdigit():
            continue
        y = y.split(",")
        if len(y)!=2:
            continue

        n1 = ""
        try:
            n1 = int(y[0])
        except:
            continue

        n2 = ""
        for i in y[1]:
            if i.isdigit():
                n2 += i
            else:
                break
        if len(n2)!=len(y[1]):
            continue
        n2 = int(n2)

        if n1<=999 and n2<=999:
            fin += n1*n2

    return fin

def main():
    
    #txt = ""
    txt = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    '''archivo = open("03.txt", "r")
    for linea in archivo.readlines():
        linea = linea.strip()
        txt += linea
    archivo.close()'''

    fin = 0

    fin += gestionMul(txt)
        
    print("Solucion primer ejercicio: " + str(fin))

    fin = 0

    x = txt.split("don't")
    print(x)

    if not txt.startswith("don't"):
        fin += gestionMul(x[0])

    for fragment in x:
        y = fragment.split("do")
        if len(y)<2:
            continue
        for j in range(1,len(y)):
            fin += gestionMul(y[j])
        
    print("Solucion segundo ejercicio: " + str(fin))
    

    return fin

if __name__=="__main__":
    main()

