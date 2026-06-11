def obter_elemento(lista: list, indice:int):
    try:
       numero = lista[indice]
    except IndexError:
       return 'Posição inexistente'
    
    return numero



if __name__ == '__main__':
    lista = [1,23,234,65,23,123,125]
    print(obter_elemento(lista, 10))
