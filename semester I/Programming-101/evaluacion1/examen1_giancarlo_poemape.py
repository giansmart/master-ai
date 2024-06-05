
def pregunta_1(grados, hora):
    calefaccion = ""
    if grados < 5:
        calefaccion = "Encender"
    elif grados > 20:
        calefaccion = "Apagar"
    elif 5 <= grados <= 20:
        if 18 <= hora <= 23 or 0 <= hora <= 6:
            calefaccion = "Encender"
    return calefaccion

#print(pregunta_1(grados=2, hora=12))
#print(pregunta_1(grados=22, hora=17))
#print(pregunta_1(grados=10, hora=20))

def pregunta_2(secuencia_genes: str):
    secuencia_n = [int(n) for n in secuencia_genes.split(" ")]
    salida = "Inestable"
    restas = []
    for i in range(len(secuencia_n)):
        if i > 0:
            restas.append(secuencia_n[i] - secuencia_n[i-1])

    dif_negativas = 0
    for num in restas:
        dif_negativas += 1
    if dif_negativas > 1:
        salida = "Estable"
    return salida

print(pregunta_2("1 2 3 4 5 4 3 2 1"))
print(pregunta_2("1 3 2 4 5 6"))

def pregunta_3(frecuencias: str):
    result = "Armonica"
    frecuencias_n = [ int(n) for n in frecuencias.split(" ") ]

    restas = []
    for indice in range(len(frecuencias_n)):
        if indice > 0:
            restas.append(frecuencias_n[indice] - frecuencias_n[indice-1])

    resta_ref = restas[0]
    for resta in restas:
        if resta != resta_ref:
            result = "No armonica"
            break
    return result

#print(pregunta_3("200 400 600 800"))
#print(pregunta_3("300 450 600 900"))
#print(pregunta_3("128 256 384 512"))

def pregunta_4(ventas, umbral):
    ventas_n = [int(n.strip()) for n in ventas.split(",")]
    #for venta in ventas_n:

    #return ventas_n

#print(pregunta_4("100 ,200 ,180 ,190 ,200 ,210 ,205 ,198 ,165 ,160 ,155 ,150 ,145 ,140 , 135 ,130 ,125 ,120 ,115 ,110 ,105 ,100 ,95 ,90 ,85 ,80 ,75 ,70 ,65 ,60", 10))