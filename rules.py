def cuadrados_mutuos_filas(matriz, left, inicio, final, i):
    # si existe un solo numero en el array entonces se puede realizar los cuadrados mutuos
    if len(left[i]) == 1:
        # print("tiene largo 1 ",left[i])
        rango_inicial = final+1-int(left[i][0])
        rango_final = inicio+int(left[i][0])-1
        agregar_cuadrados_filas(matriz, rango_inicial, rango_final, i)
        # print("Rango inicial",rango_inicial," Rango final",rango_final)
    # else: #Si existe mas de un numero en el array entonces se debe verificar si se
    # puede ingresar en el bloque inicial o final del numero del array inicial o final respectivamente
    # print("entra else")


def agregar_cuadrados_filas(matriz, rango_inicial, rango_final, i):
    for j in range(rango_inicial, rango_final+1):
        matriz[i][j] = 1


def cuadrados_mutuos_columnas(matriz, left, inicio, final, j):
    # si existe un solo numero en el array entonces se puede realizar los cuadrados mutuos
    if len(left[j]) == 1:
        # print("tiene largo 1 ",left[i])
        rango_inicial = final+1-int(left[j][0])
        rango_final = inicio+int(left[j][0])-1
        agregar_cuadrados_columnas(matriz, rango_inicial, rango_final, j)
        # print("Rango inicial",rango_inicial," Rango final",rango_final)
    else:   # Si existe mas de un numero en el array entonces se debe verificar
            # si se puede ingresar en el bloque inicial o final del numero del array inicial o final respectivamente
        print("entra else")


def agregar_cuadrados_columnas(matriz, rango_inicial, rango_final, j):
    for i in range(rango_inicial, rango_final+1):
        matriz[i][j] = 1


def agregar_cuadrados_perfectos_columna(matriz, top, j, size, rows):
    count = 0
    # print(size)
    for i in range(0, len(top[j])):
        # print("first",int(top[j][i]))
        for n in range(0, int(top[j][i])):
            # print(count)
            matriz[count][j] = 1
            count += 1
        # print("second", count)
        if count < rows:
            matriz[count][j] = -1
            count += 1


def agregar_cuadrados_perfectos_fila(matriz, left, i, size):
    count = 0
    # print(size)
    for j in range(0, len(left[i])):
        # print("first", int(left[i][j]))
        for n in range(0, int(left[i][j])):
            # print(count)
            matriz[i][count] = 1
            count += 1

        # print("second", count)
        if count < len(matriz[j]):
            matriz[i][count] = -1
            count += 1


def completar_primer_numero(matriz, num, fila, posini, identificador):
    if identificador == "fila":
        for i in range(posini, posini+num):
            matriz[fila][i] = 1

    if identificador == "columna":
        if num > 1:
            for i in range(posini, posini+num):
                matriz[i][fila] = 1


def verificar_estado(matriz, indice_constante, largo, array_principal, identificador):

    if identificador == "fila":
        numero = int(array_principal[0])

        # Si en el array el numero es un 0 se marca todas las casillas con X
        if numero == 0:
            marcar_casillas(matriz, indice_constante, 0, largo, 0, "fila")

        # Se cuentan los cuadrados coloreados para verificar si la solucion se encuentra lista
        contador_cuadrado = 0
        for j in range(0, largo):
            if matriz[indice_constante][j] == 1:
                contador_cuadrado += 1

        contador_numero_array = 0
        for j in range(0, len(array_principal)):
            if array_principal[j] != " ":
                contador_numero_array = contador_numero_array + int(array_principal[j])
        if contador_numero_array == contador_cuadrado:
            print("contador_cuadrados", contador_cuadrado, " contador_numero", contador_numero_array)
            marcar_casillas(matriz, indice_constante, 0, largo, numero, "fila")

    # Si el identificador es columna se debe ralizar la operacion segun la logica de la columna
    if identificador == "columna":
        numero = int(array_principal[0])
        if numero == 0:
            marcar_casillas(matriz, indice_constante, 0, largo, 0, "columna")

    # Se cuentan los cuadrados coloreados para verificar si la solucion se encuentra lista

        contador_cuadrado = 0
        for j in range(0, largo):
            if matriz[j][indice_constante] == 1:
                contador_cuadrado += 1
        contador_numero_array = 0
        for j in range(0, len(array_principal)):
            if array_principal[j] != " ":
                contador_numero_array = contador_numero_array + int(array_principal[j])

        if contador_numero_array == contador_cuadrado:
            print("contador_cuadrados", contador_cuadrado, " contador_numero", contador_numero_array)
            marcar_casillas(matriz, indice_constante, 0, largo, numero, "columna")
# Marca las casillas vacias con X


def marcar_casillas(matriz, indice_constante, rango_inicial, rango_final, numero_array, identificador):

    # si el identificador es fila se debe realizar la operacion segun cierta logica
    if numero_array == 0:
        if identificador == "fila":
            # Se marcan las casillas de la fila con X
            for j in range(rango_inicial, rango_final):
                if j != rango_inicial and matriz[indice_constante][j] == 1:
                    j = rango_final+1
                matriz[indice_constante][j] = -1
        if identificador == "columna":
            # Se marcan las casillas de las columnas con X
            for i in range(rango_inicial, rango_final):
                if i != rango_inicial and matriz[i][indice_constante] == 1:
                    break
                matriz[i][indice_constante] = -1
    # Si el numero del array es distinto de cero significa que se marcan
    # las casillas en el rango indicado
    if numero_array != 0:
        if identificador == "fila":
            # Se marcan las casillas de la fin
            for j in range(rango_inicial, rango_final):
                if matriz[indice_constante][j] != 1:
                    matriz[indice_constante][j] = -1

        if identificador == "columna":
            for i in range(rango_inicial, rango_final):
                if matriz[i][indice_constante] != 1:
                    matriz[i][indice_constante] = -1
