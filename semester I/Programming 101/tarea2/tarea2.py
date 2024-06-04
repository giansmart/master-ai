import datetime

def pregunta_1(inicio:int, ultimo:int, divisor:int = 7) -> float:
    """
    Calcula el promedio de los numeros que son multiplos de un divisor dado dentro del rango especificado por inicio y ultimo.
    Args:
    inicio (int): Numero de inicio del rango (inclusive).
    ultimo (int): Numero final del rango (inclusive).
    divisor (int, opcional): Divisor para encontrar multiplos. Por defecto
    es 7. Returns:
    float: El promedio de los multiplos encontrados, o 0 si no hay multiplos """

    promedio = 0
    suma = 0
    count_divisores = 0
    for i in range(inicio, ultimo + 1):
        if i % divisor == 0:
            suma += i
            count_divisores += 1
    if suma > 0:
        promedio = suma / count_divisores

    return promedio

#print(pregunta_1(inicio = 1, ultimo = 7, divisor = 7))
#print(pregunta_1(inicio = -10, ultimo = 10, divisor = 2))
#print(pregunta_1(inicio = 14, ultimo = 40, divisor = 5))

def pregunta_2(fecha_str: str) -> int:
    """
    Determina la diferencia absoluta en dias entre la fecha actual y la fecha ingresada
    Parametros:
    fecha(str): es la fecha en formato YYYY-MM-DD
    Retorna:
    int : Diferencia absoluta en dias
    """
    fecha_hoy = datetime.date.today() #.strftime('%Y-%m-%d')
    fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
    diferencia_dias = abs((fecha - fecha_hoy).days)
    return diferencia_dias

#print(pregunta_2("2024-04-30"))
#print(pregunta_2("2024-05-08"))

def pregunta_3(numeros: list, valor_minimo: float) -> bool:
    """
    Verifica que todos los numeros en una lista sean mayores que un valor
    minimo dado.
    Lanza una excepcion si alguno no lo es o si el elemento no es un
    numero.
    Args:
    lista (list): Lista de elementos , esperando numeros , a verificar.
    minimo (float): Valor minimo que cada numero debe superar.
    Raises:
    ValueError: Si algun numero es menor o igual al valor minimo. TypeError: Si un elemento en la lista no es un numero.
    Returns:
    bool: True si todos los numeros son validos, False si la lista esta vacia.
    """
    if len(numeros) == 0:
        return False

    for num in numeros:
        if not isinstance(num, (float, int)):
            raise TypeError("LA LISTA DEBE CONTENER SOLO NUMEROS")
        if num <= valor_minimo:
            raise ValueError("NO TODOS LOS NUMEROS SON MAYORES QUE EL VALOR MINIMO")
    return True

#print(pregunta_3([10, 20, 30, 40, 50], 5))
#print(pregunta_3([10, 20, 30, 40, 50], 50))
#print(pregunta_3([10, 20, 30, 40, 50, "a"], 5))
#print(pregunta_3([], 5))

def pregunta_4(archivo_entrada: str, archivo_salida: str) -> float | None:
    def es_primo(numero: int) -> bool:
        """ Retorna True si el numero es primo, False en caso contrario """
        i = 2
        while i * i <= numero :
            if numero % i == 0:
                return False
            i += 1
        return True



    try:
        INPUT = open(archivo_entrada, "r")

    except FileNotFoundError:
        #OUTPUT.close()
        return None

    OUTPUT = open(archivo_salida, "w+")
    suma = 0
    lineas = INPUT.readlines()
    for LINE in lineas:
        suma += int(LINE.strip())

    for i in range(2, suma):
        if es_primo(i):
            OUTPUT.write("{}\n".format(i))

    OUTPUT.close()
    return suma