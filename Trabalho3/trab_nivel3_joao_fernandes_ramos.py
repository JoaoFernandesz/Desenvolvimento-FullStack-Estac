
lista = list(map(int,input("\nInsira a lista de inteiros desejada separando por virgulas: ").strip().split(',')))[::]

def conjuntosDasPartes(lista):
    if lista:
        p = conjuntosDasPartes(lista[1:])
        return (p + [x + lista[:1] for x in p])
    else:
        return ([[]])

print('Os conjuntos das partes informadas na primeira célula de código estão na lista a seguir: ') 
conjuntosDasPartes(lista)