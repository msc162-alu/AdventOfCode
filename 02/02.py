import copy

def recorre(rep):
    ok = True

    if rep[0]>rep[1]:
        case = 1
    else:
        case = 0

    for i in range(len(rep)-1):
        if case == 0 and rep[i]>rep[i+1]:
            ok = False
            break
        if case == 1 and rep[i]<rep[i+1]:
            ok = False
            break
        if abs(rep[i]-rep[i+1])<1 or abs(rep[i]-rep[i+1])>3:
            ok = False
            break

    return ok

def main():
    
    rep = []
    fin = 0
    fin2 = 0
    archivo = open("02.txt", "r")
    for linea in archivo.readlines():
        linea = linea.strip()
        for value in linea.split():
            rep.append(int(value))

        ok = recorre(rep)

        if ok:
            fin += 1
        else:   # Ejecicio 2
            for i in range(len(rep)):
                rep2 = copy.deepcopy(rep)
                rep2.pop(i)
                ok2 = recorre(rep2)
                if ok2:
                    fin2 += 1
                    break
        
        rep.clear()

    fin2 += fin
    print("*******")
    print("Solucion primer ejercicio: " + str(fin))
    print("Solucion segundo ejercicio: " + str(fin2))
    
    archivo.close()



    return fin

if __name__=="__main__":
    main()