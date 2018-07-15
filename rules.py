def create_block(matriz, bloques, i, j, k, var_check, var_inicio, size):
    # Calculo de bloques seguidos
    # Se calcula todos los bloques de cada fila para su posterior uso en cada una
    # de las reglas anteriores
    # Marca el inicio de cuadrados vacios

    final = -1
    if matriz[i][j] != -1 and not var_check[0]:
        var_inicio[0] = k
        var_check[0] = True

    # Demarca el final de los bloques en blancos seguidos
    if (matriz[i][j] == -1 or k == size - 1) and var_inicio[0] != -1:

        if matriz[i][j] == -1 and k != size - 1:
            final = k - 1
        if matriz[i][j] == -1 and k == size - 1:
            final = k - 1
        if matriz[i][j] != -1 and k == size - 1:
            final = k

        # print("inicio= ", inicio, "final= ", final, " ",)
        aux = []
        if var_inicio[0] == final and var_inicio[0] != -1:
            aux = [var_inicio[0], var_inicio[0]]
            bloques.append(aux)
            var_inicio[0] = -1

        if var_inicio[0] != final and var_inicio[0] != - 1:
            aux = [var_inicio[0], final]
            bloques.append(aux)
            var_inicio[0] = -1
        var_check[0] = False


def cuadrados_mutuos_filas(matriz, left, inicio, final, i):
    # si existe un solo numero en el array entonces se puede realizar los cuadrados mutuos
    if len(left[i]) == 1:
        # print("tiene largo 1 ",left[i])
        rango_inicial = final+1-int(left[i][0])
        rango_final = inicio+int(left[i][0])-1
        for j in range(rango_inicial, rango_final + 1):
            matriz[i][j] = 1
        # print("Rango inicial",rango_inicial," Rango final",rango_final)
    # else: #Si existe mas de un numero en el array entonces se debe verificar si se
    # puede ingresar en el bloque inicial o final del numero del array inicial o final respectivamente
    # print("entra else")


def cuadrados_mutuos_columnas(matriz, left, inicio, final, j):
    # si existe un solo numero en el array entonces se puede realizar los cuadrados mutuos
    if len(left[j]) == 1:
        # print("tiene largo 1 ",left[i])
        rango_inicial = final+1-int(left[j][0])
        rango_final = inicio+int(left[j][0])-1
        for i in range(rango_inicial, rango_final + 1):
            matriz[i][j] = 1
        # print("Rango inicial",rango_inicial," Rango final",rango_final)
    else:   # Si existe mas de un numero en el array entonces se debe verificar
            # si se puede ingresar en el bloque inicial o final del numero del array inicial o final respectivamente
        print("entra else")


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


def completar_primer_numero(matriz, num, fila, posini, identificador, size):
    if identificador == "fila":
        if num != 1:
            for i in range(posini, posini+num):
                matriz[fila][i] = 1
            if i+1 < size:
                matriz[fila][i+1] = -1
        if num == 1 and posini+1 < size:
            matriz[fila][posini+1] = -1

    if identificador == "columna":
        if num != 1:
            for i in range(posini, posini+num):
                matriz[i][fila] = 1
            if i+1 < size:
                matriz[i+1][fila] = -1
        if num == 1 and posini+1 < size:
            matriz[posini+1][fila] = -1

def completar_ultimo(matriz, num, fila, posini, identificador):
    if identificador == "fila":
        while num > 0:
            matriz[fila][posini] = 1
            num -= 1
            posini -= 1
        matriz[fila][posini] = -1

    if identificador == "columna":
        while num > 0:
            matriz[posini][fila] = 1
            num -= 1
            posini -= 1
        matriz[posini][fila] = -1


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


def interseccion_cuadrados_multiples(matriz, array, size, const, id):
    list_left = [-1] * size
    list_right = [-1] * size
    iter = 0
    # Se crea la lista izquierda
    for i in range(0, len(array)):
        cont = 0
        num = int(array[i])
        while cont < num:
            list_left[iter] = i
            cont += 1
            iter += 1
        iter += 1
    # Se crea la lista derecha
    iter = size-1
    for i in range(len(array)-1, -1, -1):
        cont = 0
        num = int(array[i])
        while cont < num:
            list_right[iter] = i
            cont += 1
            iter -= 1
        iter -= 1

    # Se intersectan estas listas buscando igualdades en sus numeros
    for i in range(0, size):
        if list_right[i] == list_left[i] and list_right[i] != -1:
            if id == "filas":
                matriz[const][i] = 1
            if id == "columna":
                matriz[i][const] = 1


