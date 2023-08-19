def soma_elementos( lista:list ) -> int:
    if len(lista) == 0:
        return 0
    return lista[0] + soma_elementos(lista[1:])