from typing import List , Dict, Any

# Ejercicio 1.1: Combinacion y Ordenacion de Listas
def combinar_y_ordenar(lista1: List[int], lista2: List[int]) -> List[int]:
    '''
    Descripción: Tienes dos listas de números enteros, lista1 y lista2. Combina
    ambas listas en una sola, elimina los duplicados y ordena la lista resultante en
    orden ascendente
    '''
    new_lista = lista1[:] + lista2 #combinar lista 1 y lista 2
    new_lista = list(set(new_lista)) # Elimina los elementos duplicados de la lista combinada y los ordena de manera ascendente
    return new_lista

#lista1 = [ 3 , 1 , 4 , 1 , 5 ]
#lista2 = [ 9 , 2 , 6 , 5 , 3 , 5 ]
#print (combinar_y_ordenar(lista1, lista2))


# Ejercicio 1.2: Rotacion de Lista
def rotar_lista(lista: List[int], n:int) -> List[int]:
    '''
    Escribe una función que rote una lista de números enteros hacia
    la derecha un número n de veces. Si n es negativo, rota la lista hacia la izquierda
    '''
    if n > 0 :
        n = n % len(lista)
        new_lista = lista [-n:] + lista[:-n]
    else:
        n = abs(n) % len(lista)
        new_lista = lista[n:] + lista[:n]
    return new_lista


#lista = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ]
#n = 3
#print(rotar_lista(lista,n))
#n = -2
#print(rotar_lista(lista,n))


# Ejercicio 1.3: Combinaciones Unicas de Sumatoria
def combinaciones_sumatorias(lista: List[int], target: int) -> List[List[int]]:
    '''
    Descripci´on: Dada una lista de n´umeros enteros y un n´umero objetivo target,
    escribe una funci´on que encuentre todas las combinaciones ´unicas de n´umeros
    en la lista que sumen el valor objetivo. Cada n´umero en la lista puede ser usado
    m´ultiples veces.
    '''
    lista.sort()
    resultado = []
    pila = [(0, 0, [])]

    while pila:
        suma_actual, inicio, combinacion = pila.pop(0)

        if suma_actual == target:
            resultado.append(combinacion)
            continue
        elif suma_actual > target:
            continue

        for i in range(inicio, len(lista)):
            nueva_combinacion = combinacion + [lista[i]]
            pila.append((suma_actual + lista[i], i, nueva_combinacion))
    return resultado

#lista = [2,3,6,7]
#target = 7
#print(combinaciones_sumatorias(lista, target))

# Ejercicio 2.1: Suma de Matrices
def suma_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        raise ValueError("Las matrices deben tener las mismas dimensiones.")

    filas = len(matriz1)
    columnas = len(matriz1[0])
    matriz_resultante = [[0 for _ in range(columnas)] for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            matriz_resultante[i][j] = matriz1[i][j] + matriz2[i][j]

    return matriz_resultante

#print(suma_matrices([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]))

# Ejercicio 2.2: Producto de Matrices
def producto_matrices(matriz1: List[List[int]], matriz2: List[List[int]]) -> List[List[int]]:
    if len(matriz1[0]) != len(matriz2):
        raise ValueError(
            "El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz")

    resultado = [[0 for _ in range(len(matriz2[0]))] for _ in range(len(matriz1))]

    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado
#print(producto_matrices([[1, 2], [3, 4]], [[5, 6],[7, 8]]))

# Ejercicio 2.3: Camino Minimo en una Matriz
def camino_minimo(matriz: List[List[int]], residual: int = 0, paths: List[int] = []) -> int:
    # extract the current step
    step = matriz[0][0]

    # check if there are paths for right or behind move
    size_right = len(matriz[0])
    size_below = len(matriz)

    # compute the new residual
    new_residual = step + residual

    # if we are on the lower right value, return the residual
    if size_right == 1 and size_below == 1:
        paths.append(new_residual)
        return

    # iterate over all the other paths
    if size_right > 1:
        right_matriz = [matriz[i][1:] for i in range(len(matriz))]
        camino_minimo(right_matriz, new_residual, paths)
    if size_below > 1:
        below_matriz = matriz[1:]
        camino_minimo(below_matriz, new_residual, paths)

    # print paths only for first iteration
    if residual == 0:
        # print(paths)
        return min(paths)

#matriz = [[1,3,1], [1,5,1], [4,2,1]]
#print(camino_minimo(matriz))

# Ejercicio 3.1: Contar Ocurrencias en una Lista
def contar_ocurrencias(lista: list) -> {}:
    dict = {}
    for el in lista:
        if el not in dict:
            dict[el] = 0
        dict[el] += 1
    return dict

#print(contar_ocurrencias(['a','b','a','c','b','a','d']))

# Ejercicio 3.2: Combinar Diccionarios
def combinar_diccionarios(dic1: Dict[Any, int], dic2: Dict[Any, int]) -> dict:
    new_dic = dic1.copy()

    for clave, valor in dic2.items():
        if clave in new_dic:
            new_dic[clave] += valor
        else:
            new_dic[clave] = valor

    return new_dic


# Ejemplo de uso
#dic1 = {'a': 1, 'b': 2, 'c': 3}
#dic2 = {'b': 3, 'c': 4, 'd': 5}
#print(combinar_diccionarios(dic1, dic2))


# Ejercicio 3.3: Calcular la frecuencia de palabras
def frecuencia_palabras(documentos: List[str]) -> {}:
    docs_dict = {}
    for doc in documentos:
        # asumiendo que el criterio para hacer el split es el espacio en blanco
        for palabra in doc.split(" "):
            if palabra not in docs_dict:
                docs_dict[palabra] = 0
            docs_dict[palabra] += 1
    return docs_dict

#documentos = [
#    "este es el primer documento",
#    "el segundo documento es mas largo",
#    "este es el tercer documento"
#]
#print(frecuencia_palabras(documentos))
