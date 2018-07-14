
def main():
    print("Ingrese Cantidad de filas ")
    rows = int(input())
    print("Ingrese Cantidad de Columnas ")
    columns = int(input())
    print("Filas: ", rows, "Columnas: ", columns)
    create_matrix(rows, columns)
    matriz = create_matrix(rows, columns)



    #left = create_matrix(rows-1, columns)
    #top = create_matrix(rows, columns-1)

    left = []
    top = []
    i = 0
    j = 0
    print("Ingresar los valores de cada fila")
    while i<rows:
        print("Ingrese el estado de la fila ",i+1)
        estado=input()
        if estado.find(' '):
            lista=estado.split(' ')
            i=i+1
            print(lista)
            left.append(lista)

    print(left)

    print("Ingresar los valores de cada columna")
    while j < columns:
        print("Ingrese el estado de la columna ", j)
        estado = input()
        if (estado.find(' ')):
            lista = estado.split(' ')
            j = j + 1
            print(lista)
            top.append(lista)

    print(top)

    print("printing the lefft matrix ")
    print_matrix_left(left,rows)

    print("printing the leftp matrix ")
    print_matrix_top(top,columns)

    print_matrix(matriz,rows,columns)

    ##Resolucion del Problema##

    unavez=0;
    #Loop del problema mientras no encuentre solucion no debe parar su ejecucion
    while unavez==0:
         print(" ")
         print("-------------------------------------")
         print("Loop Filas")


        #---Recorrido por FILAS----------
         for i in range(0, rows):
             bloques = []
             largo=0
             inicio = -1
             final=-1
             check=False
             for j in range(0, columns):

        #Calculo de bloques seguidos
        #Se calcula todos los bloques de cada fila para su posterior uso en cada una de las reglas anteriores

                #Marca el inicio de cuadrados vacios
                if matriz[i][j] != -1 and check!= True:
                    inicio=j
                    check=True
                #Suma los bloques en blanco seguidos
                if matriz[i][j] != -1 and check==True:
                    largo=largo+1
                #Demarca el final de los bloques en blancos seguidos
                if (matriz[i][j] == -1 or j == columns-1) and inicio!=-1:

                    if matriz[i][j] == -1 and j!= columns-1:
                        final=j-1
                    if matriz[i][j] == -1 and j == columns-1:
                        final=j-1
                    if matriz[i][j] != -1 and j == columns-1:
                        final=j


                    #print("inicio= ", inicio, "final= ", final, " ",)
                    aux = []
                    if inicio == final and inicio !=-1:
                        aux = [inicio]
                        bloques.append(aux)
                        inicio=-1


                    if inicio != final and inicio !=-1:
                        aux = [inicio,final]
                        bloques.append(aux)
                        inicio=-1
                    check = False
                    largo = 0



             print("i=",i," ", bloques)




        #--Verificacion Estado--

             verificar_estado(matriz,i,columns,left[i],"fila")



        #--Perfecto--

             sum = 0
             size = len(left[i])
             # Suma los numeros del array y los espacios necesarios entre si
             for k in range(0, size):
                sum = sum + int(left[i][k])
             sum = sum + len(left[i]) - 1
             #print(sum)


             if sum == columns:
                #print(sum)
                agregar_cuadrados_perfectos_fila(matriz, left, i, size)

        #--Cuadrados Mutuos--
             tamano_bloque=len(bloques)
             tamano_array=len(left[i])
             #print("tamaño del array",tamano_array)
             #print("tamaño ", tamano_bloque)
             #Si el tamaño del bloque es del largo de la columna y el array es un solo numero
             if len(bloques)>0:
                if len(bloques[0])>1:
                    if tamano_bloque == 1 and tamano_array==1 and float(left[i][0])>(bloques[0][1]-bloques[0][0]+1)/2 :
                        #print(" bloque[0]",bloques[0][0]," bloque[1]",bloques[0][1])
                        cuadrados_mutuos_filas(matriz, left, bloques[0][0], bloques[0][1], i)


        #--Completar primero--

        #Si en el primer bloque de la fila/columna se encuentra la primera posicion rellenada (■)
        # entonces se debe rellenar los cuadros para completar el primer numero del array

             if(len(bloques)>0):
               primera_pos=bloques[0][0]
               if matriz[i][primera_pos]== 1:
                   numero=int(left[i][0])
                   completar_primer_numero(matriz,numero,i,primera_pos,"fila")

         print_matrix(matriz, rows, columns)
         input()



         #--------Recorrido por COLUMNAS-----------
         print("Loop Columnas")
         for j in range(0, columns):
             bloques = []
             largo = 0
             inicio = -1
             final = -1
             check = False

             for i in range(0, rows):


                #Calculo de bloques seguidos---
                # Marca el inicio de cuadrados vacios
                 if matriz[i][j] != -1 and check != True:
                     inicio = i
                     check = True
                 # Suma los bloques en blanco seguidos
                 if matriz[i][j] != -1 and check == True:
                     largo = largo + 1
                 # Demarca el final de los bloques en blancos seguidos
                 if ( matriz[i][j] == -1 or i == rows - 1 ) and inicio != -1:
                     if matriz[i][j] == -1 and i != rows-1:
                         final = i - 1
                     if matriz[i][j] == -1 and i == rows-1:
                         final= i -1
                     if matriz[i][j] != -1 and i == rows-1:
                         final = i

                     aux=[]
                     if inicio == final and inicio!=-1:
                         aux= [inicio]
                         bloques.append(aux)
                         inicio=-1

                     if inicio != final and inicio !=-1:
                         aux = [inicio, final]
                         bloques.append(aux)
                         inicio=-1

                     check = False
                     largo = 0
                     #aux=[inicio,final]
                     #bloques.append(aux)
                     #print(bloques)
                    # se procede a guardar los diferentes bloques para su posterior verificacion y a resetear el inicio y el final
                     #print(inicio, " ", final)
             print("j=", j, " ", bloques)

             #--Verificar Estado
             verificar_estado(matriz, j, rows, top[j], "columna")
             #verificar_estado(matriz, i, rows, left[i], "columna")


             #--Perfect
             # Revisa que la suma de los numeros del array mas los espacios intermedios sea iguales
             # a la la fila o columna correspondiente
             # si es asi entonces se colorea toda la fila/columna de acuerdo al orden del array con sus espacios entre
             #cada bloque
             sum=0
             size=len(top[j])
             #Suma los numeros del array y los espacios necesarios entre si
             for k in range(0, size):
                sum = sum + int(top[j][k])
             sum = sum + len(top[j])-1

             if  sum == rows:
                 agregar_cuadrados_perfectos_columna(matriz,top,j,size,rows)



             #--Cuadrados Mutuos
             #Por ahora solo se realiza el cuadrado mutuo cuando el array es de tamaño 1 (Un solo numero)
             tamano_bloque=len(bloques)
             tamano_array=len(top[j])

             if len(bloques)>0:
                if len(bloques[0])>1 :
                    if tamano_bloque ==1 and tamano_array == 1 and float(top[j][0]) > (bloques[0][1] - bloques[0][0] + 1) / 2:
                        cuadrados_mutuos_columnas(matriz, top, bloques[0][0], bloques[0][1], j)



            # --Completar primero--

            # Si en el primer bloque de la fila/columna se encuentra la primera posicion rellenada (■)
            # entonces se debe rellenar los cuadros para completar el primer numero del array

             if len(bloques) > 0:
                 primera_pos = bloques[0][0]
                 print("primera_pos ",primera_pos)
                 if matriz[primera_pos][j] == 1:
                     numero = int(top[j][0])
                     completar_primer_numero(matriz, numero, j, primera_pos, "columna")




         print_matrix(matriz, rows, columns)
         input()
         #unavez = unavez + 1



def create_matrix(rows, columns):
    matriz = [0] * rows
    for i in range(rows):
        matriz[i] = [0] * columns
    return matriz

def print_matrix(matriz,rows,columns):
    for i in range(rows):
        for j in range(columns):
            if matriz[i][j] == 1 :
                print("■ ", end='')
            if matriz[i][j] == -1 :
                print("☒ ", end='')
            if matriz[i][j] == 0:
                print("□ ", end='')

        print("")

def print_matrix_left(left,rows):
    for i in range(0,rows):
        for j in range(0,len(left[i])):
            print(left[i][j], " ", end='')
        print("")

def print_matrix_top(top,columns):
    for i in range(0,columns):
        for j in range(0,len(top[i])):
            print(top[i][j], " ", end='')
        print("")

def enter_data(matrix, rows, columns):
    for i in range(rows):
        for j in range(columns):
            print("Ingrese datos de left", i, "-", j)
            matrix[i][j] = input()
            if matrix[i][j] == '':
                matrix[i][j] = 0

def cuadrados_mutuos_filas(matriz,left,inicio,final,i):
    #si existe un solo numero en el array entonces se puede realizar los cuadrados mutuos
    if len(left[i]) == 1:
        #print("tiene largo 1 ",left[i])
        rango_inicial=final+1-int(left[i][0])
        rango_final=inicio+int(left[i][0])-1
        agregar_cuadrados_filas(matriz,rango_inicial,rango_final,i)
        #print("Rango inicial",rango_inicial," Rango final",rango_final)
    #else: #Si existe mas de un numero en el array entonces se debe verificar si se puede ingresar en el bloque inicial o final del numero del array inicial o final respectivamente
     #   print("entra else")

def agregar_cuadrados_filas(matriz,rango_inicial,rango_final,i):
    for j in range(rango_inicial,rango_final+1):
        matriz[i][j]= 1

def cuadrados_mutuos_columnas(matriz,left,inicio,final,j):
    #si existe un solo numero en el array entonces se puede realizar los cuadrados mutuos
    if len(left[j]) == 1:
        #print("tiene largo 1 ",left[i])
        rango_inicial=final+1-int(left[j][0])
        rango_final=inicio+int(left[j][0])-1
        agregar_cuadrados_columnas(matriz,rango_inicial,rango_final,j)
        #print("Rango inicial",rango_inicial," Rango final",rango_final)
    else: #Si existe mas de un numero en el array entonces se debe verificar si se puede ingresar en el bloque inicial o final del numero del array inicial o final respectivamente
        print("entra else")

def agregar_cuadrados_columnas(matriz,rango_inicial,rango_final,j):
    for i in range(rango_inicial , rango_final+1):
        matriz[i][j]= 1

def agregar_cuadrados_perfectos_columna(matriz,top,j,size,rows):
    count=0
    #print(size)
    for i in range(0 , len(top[j])):
        #print("first",int(top[j][i]))
        for n in range(0 , int(top[j][i])):
           #print(count)
           matriz[count][j]= 1
           count += 1

        #print("second", count)
        if count<rows:
            matriz[count][j] = -1
            count += 1

def agregar_cuadrados_perfectos_fila(matriz,left,i,size):
    count = 0
    # print(size)
    for j in range(0, len(left[i])):
        #print("first", int(left[i][j]))
        for n in range(0, int(left[i][j])):
            #print(count)
            matriz[i][count] = 1
            count += 1

        #print("second", count)
        if count < len(matriz[j]):
            matriz[i][count] = -1
            count += 1

def completar_primer_numero(matriz,num,fila,posini,identificador):
    if identificador == "fila":
        for i in range(posini,num):
            matriz[fila][i]=1;
    if identificador == "columna":
        for i in range(posini,num):
            matriz[i][fila]=1;

def verificar_estado(matriz,indice_constante,largo,array_principal,identificador):

    #Si el identificador es fila se debe realizar la operacion segun la logica de la fila
    if identificador == "fila":
        numero=int(array_principal[0])
        print("indice_constante",indice_constante,"anumero",numero)

        #Si en el array el numero es un 0 se marca todas las casillas con X
        if numero == 0:
          delimitar_casillas(matriz,indice_constante,0,largo,0,"fila")

        #Se cuentan los cuadrados coloreados para verificar si la solucion se encuentra lista
        contador_cuadrado=0
        for j in range(0,largo):
            if matriz[indice_constante][j] == 1:
               contador_cuadrado+=1

        contador_numero_array=0
        for j in range(0,len(array_principal)):
            if array_principal[j]!=" ":
                contador_numero_array=contador_numero_array+int(array_principal[j])

        if contador_numero_array == contador_cuadrado:
            print("contador_cuadrados", contador_cuadrado, " contador_numero", contador_numero_array)
            delimitar_casillas(matriz,indice_constante,0,largo,numero,"fila")


    #Si el identificador es columna se debe ralizar la operacion segun la logica de la columna
    if identificador == "columna":
        numero = int(array_principal[0])
        if numero == 0:
          delimitar_casillas(matriz,indice_constante,0,largo,0,"columna")

        #Se cuentan los cuadrados coloreados para verificar si la solucion se encuentra lista

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
            delimitar_casillas(matriz, indice_constante, 0, largo, numero, "columna")

#Delimita las casillas entre el [rango_inicial, rango_final] marcandolas con una X mientras no
#se encuentren coloreadas
def delimitar_casillas(matriz,indice_constante,rango_inicial,rango_final,numero_array,identificador):
  #Si el identificador es fila se debe realizar la operacion segun cierta logica
    if identificador == "fila":
        if numero_array == 0:
            for j in range(rango_inicial,rango_final):
                if j!= rango_inicial and matriz[indice_constante][j] == 1:
                    j=rango_final+1
                matriz[indice_constante][j]=-1
        if numero_array !=0:

            for j in range(rango_inicial,rango_final):
                if matriz[indice_constante][j] != 1:
                    print("entra")
                    matriz[indice_constante][j] = -1

 #Si el identificador es columna se debe realizar la operacion segun cierta logica
    if identificador == "columna":
        if numero_array ==0:
            for i in range(rango_inicial,rango_final):
                if i!= rango_inicial and matriz[i][indice_constante] == 1:
                    break
                matriz[i][indice_constante]=-1
        if numero_array !=0:

            for i in range(rango_inicial,rango_final):
                if matriz[i][indice_constante] != 1:
                    print("entra")
                    matriz[i][indice_constante] = -1





if __name__ == "__main__":
    main()