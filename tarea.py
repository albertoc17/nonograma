import rules


def main():

    print("Ingrese Cantidad de filas ")
    rows = int(input())
    print("Ingrese Cantidad de Columnas ")
    columns = int(input())
    print("Filas: ", rows, "Columnas: ", columns)
    create_matrix(rows, columns)
    matriz = create_matrix(rows, columns)

    left = []
    top = []
    i = 0
    j = 0
    print("Ingresar los valores de cada fila")
    while i < rows:
        print("Ingrese el estado de la fila ", i+1)
        estado = input()
        if estado.find(' '):
            lista = estado.split(' ')
            i = i+1
            print(lista)
            left.append(lista)
            print("hola")
    print(left)
    print("Ingresar los valores de cada columna")
    while j < columns:
        print("Ingrese el estado de la columna ", j)
        estado = input()
        if estado.find(' '):
            lista = estado.split(' ')
            j = j + 1
            print(lista)
            top.append(lista)

    print_matrix(matriz, rows, columns)

    # Resolucion del Problema

    unavez = 0
    # Loop del problema mientras no encuentre solucion no debe parar su ejecucion
    while unavez == 0:
        print(" ")
        print("-------------------------------------")
        print("Loop Filas")

        # Recorrido por FILAS
        for i in range(0, rows):
            bloques = []
            largo = 0
            inicio = -1
            final = -1
            check = False
            for j in range(0, columns):
                # Calculo de bloques seguidos
                # Se calcula todos los bloques de cada fila para su posterior uso en cada una
                # de las reglas anteriores
                # Marca el inicio de cuadrados vacios
                if matriz[i][j] != -1 and not check:
                    inicio = j
                    check = True
                # Suma los bloques en blanco seguidos
                if matriz[i][j] != -1 and check:
                    largo = largo + 1
                # Demarca el final de los bloques en blancos seguidos
                if (matriz[i][j] == -1 or j == columns-1) and inicio != -1:

                    if matriz[i][j] == -1 and j != columns-1:
                        final = j-1
                    if matriz[i][j] == -1 and j == columns-1:
                        final = j-1
                    if matriz[i][j] != -1 and j == columns-1:
                        final = j

                    # print("inicio= ", inicio, "final= ", final, " ",)
                    aux = []
                    if inicio == final and inicio != -1:
                        aux = [inicio]
                        bloques.append(aux)
                        inicio = -1

                    if inicio != final and inicio != - 1:
                        aux = [inicio, final]
                        bloques.append(aux)
                        inicio = -1
                    check = False
                    largo = 0
            print("i=", i, " ", bloques)
            # Verificacion Estado
            rules.verificar_estado(matriz, i, columns, left[i], "fila")
            # Perfecto
            sum = 0
            size = len(left[i])
            # Suma los numeros del array y los espacios necesarios entre si
            for k in range(0, size):
               sum = sum + int(left[i][k])
            sum = sum + len(left[i]) - 1
            # print(sum)

            if sum == columns:
                # print(sum)
                rules.agregar_cuadrados_perfectos_fila(matriz, left, i, size)

        # Cuadrados Mutuos
            tamano_bloque = len(bloques)
            tamano_array = len(left[i])
            # print("tamaño del array",tamano_array)
            # print("tamaño ", tamano_bloque)
            # Si el tamaño del bloque es del largo de la columna y el array es un solo numero
            if len(bloques) > 0:
                if len(bloques[0]) > 1:
                    if tamano_bloque == 1 and tamano_array == 1 and float(left[i][0]) > (bloques[0][1]-bloques[0][0]+1)/2:
                        # print(" bloque[0]",bloques[0][0]," bloque[1]",bloques[0][1])
                        rules.cuadrados_mutuos_filas(matriz, left, bloques[0][0], bloques[0][1], i)

        # Completar primero

        # Si en el primer bloque de la fila/columna se encuentra la primera posicion rellenada (■)
        # entonces se debe rellenar los cuadros para completar el primer numero del array
        # y por ultimo marcar siguiente posicion con una X si es posible

            if len(bloques) > 0:
                primera_pos = bloques[0][0]
                numero = int(left[i][0])
                if matriz[i][primera_pos] == 1 and numero > 1:
                    print(numero)
                    rules.completar_primer_numero(matriz, numero, i, primera_pos, "fila")

        print_matrix(matriz, rows, columns)
        input()

        # Recorrido por COLUMNAS
        print("Loop Columnas")
        for j in range(0, columns):
            bloques = []
            largo = 0
            inicio = -1
            final = -1
            check = False
            for i in range(0, rows):
                # Calculo de bloques seguidos---
                # Marca el inicio de cuadrados vacios
                if matriz[i][j] != -1 and not check:
                    inicio = i
                    check = True
                # suma los bloques en blanco seguidos
                if matriz[i][j] != -1 and check:
                    largo = largo + 1
                # Demarca el final de los bloques en blancos seguidos
                if (matriz[i][j] == -1 or i == rows - 1) and inicio != -1:
                    if matriz[i][j] == -1 and i != rows-1:
                        final = i - 1
                    if matriz[i][j] == -1 and i == rows-1:
                        final = i - 1
                    if matriz[i][j] != -1 and i == rows-1:
                        final = i

                    aux = []
                    if inicio == final and inicio != -1:
                        aux = [inicio]
                        bloques.append(aux)
                        inicio = -1

                    if inicio != final and inicio != -1:
                        aux = [inicio, final]
                        bloques.append(aux)
                        inicio = -1

                    check = False
                    largo = 0
                    # aux=[inicio,final]
                    # bloques.append(aux)
                    # print(bloques)
                    # se procede a guardar los diferentes bloques para su posterior
                    # verificacion y a resetear el inicio y el final
                    # print(inicio, " ", final)
            print("j=", j, " ", bloques)

            # Verificar Estado
            rules.verificar_estado(matriz, j, rows, top[j], "columna")
            # verificar_estado(matriz, i, rows, left[i], "columna")
            # Perfect
            # Revisa que la suma de los numeros del array mas los espacios intermedios sea iguales
            # a la la fila o columna correspondiente
            # si es asi entonces se colorea toda la fila/columna de acuerdo al orden del array con sus espacios entre
            # cada bloque
            sum = 0
            size = len(top[j])
            # Suma los numeros del array y los espacios necesarios entre si
            for k in range(0, size):
                sum = sum + int(top[j][k])
            sum = sum + len(top[j])-1

            if sum == rows:
                rules.agregar_cuadrados_perfectos_columna(matriz, top, j, size, rows)

            # Cuadrados Mutuos
            # Por ahora solo se realiza el cuadrado mutuo cuando el array es de tamaño 1 (Un solo numero)
            tamano_bloque = len(bloques)
            tamano_array = len(top[j])

            if len(bloques) > 0:
                if len(bloques[0]) > 1:
                    if tamano_bloque == 1 and tamano_array == 1 and float(top[j][0]) > (bloques[0][1] - bloques[0][0] + 1) / 2:
                        rules.cuadrados_mutuos_columnas(matriz, top, bloques[0][0], bloques[0][1], j)

            # Completar primero
            # Si en el primer bloque de la fila/columna se encuentra la primera posicion rellenada (■)
            # entonces se debe rellenar los cuadros para completar el primer numero del array

            if len(bloques) > 0:
                primera_pos = bloques[0][0]
                print("primera_pos ", primera_pos)
                if matriz[primera_pos][j] == 1:
                    numero = int(top[j][0])
                    rules.completar_primer_numero(matriz, numero, j, primera_pos, "columna")

        print_matrix(matriz, rows, columns)
        input()
        # unavez = unavez + 1


def create_matrix(rows, columns):
    matriz = [0] * rows
    for i in range(rows):
        matriz[i] = [0] * columns
    return matriz


def print_matrix(matriz, rows, columns):
    for i in range(rows):
        for j in range(columns):
            if matriz[i][j] == 1:
                print("■ ", end='')
            if matriz[i][j] == -1:
                print("☒ ", end='')
            if matriz[i][j] == 0:
                print("□ ", end='')
        print("")


def enter_data(matrix, rows, columns):
    for i in range(rows):
        for j in range(columns):
            print("Ingrese datos de left", i, "-", j)
            matrix[i][j] = input()
            if matrix[i][j] == '':
                matrix[i][j] = 0


if __name__ == "__main__":
    main()
