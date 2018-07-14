
def main():
    print("Ingrese Cantidad de filas ")
    rows = int(input())
    print("Ingrese Cantidad de Columnas ")
    columns = int(input())
    print("Filas: ", rows, "Columnas: ", columns)
    create_matrix(rows, columns)
    matriz = create_matrix(rows, columns)



    #top = create_matrix(rows-1, columns)
    #left = create_matrix(rows, columns-1)

    top = []
    left = []
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
            top.append(lista)

    print(top)

    print("Ingresar los valores de cada columna")
    while j < columns:
        print("Ingrese el estado de la columna ", j)
        estado = input()
        if (estado.find(' ')):
            lista = estado.split(' ')
            j = j + 1
            print(lista)
            left.append(lista)

    print(left)

    print("printing the top matrix ")
    print_matrix_top(top,rows)

    print("printing the left matrix ")
    print_matrix_left(left,columns)

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

             verificar_estado(matriz,i,columns,top[i],"fila")



        #--Perfecto--

             sum = 0
             size = len(top[i])
             # Suma los numeros del array y los espacios necesarios entre si
             for k in range(0, size):
                sum = sum + int(top[i][k])
             sum = sum + len(top[i]) - 1
             #print(sum)


             if sum == columns:
                #print(sum)
                agregar_cuadrados_perfectos_fila(matriz, top, i, size)

        #--Cuadrados Mutuos--
             tamano_bloque=len(bloques)
             tamano_array=len(top[i])
             #print("tamaño del array",tamano_array)
             #print("tamaño ", tamano_bloque)
             #Si el tamaño del bloque es del largo de la columna y el array es un solo numero
             if tamano_bloque == 1 and tamano_array==1 and float(top[i][0])>(bloques[0][1]-bloques[0][0]+1)/2 :
                #print(" bloque[0]",bloques[0][0]," bloque[1]",bloques[0][1])
                cuadrados_mutuos_filas(matriz, top, bloques[0][0], bloques[0][1], i)


        #--Completar primero--

        #Si en el primer bloque de la fila/columna se encuentra la primera posicion rellenada (■)
        # entonces se debe rellenar los cuadros para completar el primer numero del array

             if(len(bloques)>0):
                primera_pos=bloques[0][0]
                if matriz[i][primera_pos]== 1:
                    numero=int(top[i][0])
                    completar_primer_numero(matriz,numero,i,primera_pos)










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
                     if inicio == final:
                         aux= [inicio]
                         bloques.append(aux)

                     if inicio != final:
                         aux = [inicio, final]
                         bloques.append(aux)

                     check = False
                     largo = 0
                     #aux=[inicio,final]
                     #bloques.append(aux)
                     #print(bloques)
                    # se procede a guardar los diferentes bloques para su posterior verificacion y a resetear el inicio y el final
                     #print(inicio, " ", final)
             print("j=", j, " ", bloques)

             #--Verificar Estado

             #verificar_estado(matriz, i, rows, top[i], "columna")


             #--Perfect
             # Revisa que la suma de los numeros del array mas los espacios intermedios sea iguales
             # a la la fila o columna correspondiente
             # si es asi entonces se colorea toda la fila/columna de acuerdo al orden del array con sus espacios entre
             #cada bloque
             sum=0
             size=len(left[j])
             #Suma los numeros del array y los espacios necesarios entre si
             for k in range(0, size):
                sum = sum + int(left[j][k])
             sum = sum + len(left[j])-1

             if  sum == rows:
                 agregar_cuadrados_perfectos_columna(matriz,left,j,size,rows)



             #--Cuadrados Mutuos
             #Por ahora solo se realiza el cuadrado mutuo cuando el array es de tamaño 1 (Un solo numero)
             tamano_bloque=len(bloques)
             tamano_array=len(left[j])
             if tamano_bloque ==1 and tamano_array == 1 and float(left[j][0]) > (bloques[0][1] - bloques[0][0] + 1) / 2:
                cuadrados_mutuos_columnas(matriz, left, bloques[0][0], bloques[0][1], j)

             #if float(left[j][0])>(largo/2):
             #  cuadrados_mutuos_columnas(matriz,left,inicio,final,j)






         print_matrix(matriz, rows, columns)

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

def print_matrix_top(top,rows):
    for i in range(0,rows):
        for j in range(0,len(top[i])):
            print(top[i][j], " ", end='')
        print("")

def print_matrix_left(left,columns):
    for i in range(0,columns):
        for j in range(0,len(left[i])):
            print(left[i][j], " ", end='')
        print("")

def enter_data(matrix, rows, columns):
    for i in range(rows):
        for j in range(columns):
            print("Ingrese datos de TOP", i, "-", j)
            matrix[i][j] = input()
            if matrix[i][j] == '':
                matrix[i][j] = 0

def cuadrados_mutuos_filas(matriz,top,inicio,final,i):
    #si existe un solo numero en el array entonces se puede realizar los cuadrados mutuos
    if len(top[i]) == 1:
        #print("tiene largo 1 ",top[i])
        rango_inicial=final+1-int(top[i][0])
        rango_final=inicio+int(top[i][0])-1
        agregar_cuadrados_filas(matriz,rango_inicial,rango_final,i)
        #print("Rango inicial",rango_inicial," Rango final",rango_final)
    #else: #Si existe mas de un numero en el array entonces se debe verificar si se puede ingresar en el bloque inicial o final del numero del array inicial o final respectivamente
     #   print("entra else")

def agregar_cuadrados_filas(matriz,rango_inicial,rango_final,i):
    for j in range(rango_inicial,rango_final+1):
        matriz[i][j]= 1

def cuadrados_mutuos_columnas(matriz,top,inicio,final,j):
    #si existe un solo numero en el array entonces se puede realizar los cuadrados mutuos
    if len(top[j]) == 1:
        #print("tiene largo 1 ",top[i])
        rango_inicial=final+1-int(top[j][0])
        rango_final=inicio+int(top[j][0])-1
        agregar_cuadrados_columnas(matriz,rango_inicial,rango_final,j)
        #print("Rango inicial",rango_inicial," Rango final",rango_final)
    else: #Si existe mas de un numero en el array entonces se debe verificar si se puede ingresar en el bloque inicial o final del numero del array inicial o final respectivamente
        print("entra else")

def agregar_cuadrados_columnas(matriz,rango_inicial,rango_final,j):
    for i in range(rango_inicial , rango_final+1):
        matriz[i][j]= 1

def agregar_cuadrados_perfectos_columna(matriz,left,j,size,rows):
    count=0
    #print(size)
    for i in range(0 , len(left[j])):
        #print("first",int(left[j][i]))
        for n in range(0 , int(left[j][i])):
           #print(count)
           matriz[count][j]= 1
           count += 1

        #print("second", count)
        if count<rows:
            matriz[count][j] = -1
            count += 1

def agregar_cuadrados_perfectos_fila(matriz,top,i,size):
    count = 0
    # print(size)
    for j in range(0, len(top[i])):
        #print("first", int(top[i][j]))
        for n in range(0, int(top[i][j])):
            #print(count)
            matriz[i][count] = 1
            count += 1

        #print("second", count)
        if count < len(matriz[j]):
            matriz[i][count] = -1
            count += 1

def completar_primer_numero(matriz,num,fila,posini):
    for i in range(posini,num):
        matriz[fila][i]=1;

def verificar_estado(matriz,i,columns,array_principal,identificador):

    #Si el identificador es fila se debe realizar la operacion segun la logica de la fila
    if identificador == "fila":
        count=0
        numero=int(array_principal[0])

        #Si se encuentra un cero en el array
        if numero == 0:
          delimitar_casillas(matriz,i,i,columns,0,"fila")

       # for j in range(0,columns):
       #     if matriz[i][j] == 1:
       #        ++count
    #Si el identificador es columna se debe ralizar la operacion segun la logica de la columna
    if identificador == "columna":
        numero = int(array_principal[0])
        if numero == 0:
          delimitar_casillas(matriz,i,i,columns,0,"columna")
        print("asdf")

def delimitar_casillas(matriz,indice_constante,rango_inicial,rango_final,numero_array,identificador):
    if identificador == "fila":
        for j in range(rango_inicial,rango_final):
            if j!= rango_inicial and matriz[indice_constante][j] == 1:
                break
            matriz[indice_constante][j]=-1
    if identificador == "columna":
        print("asdf")






if __name__ == "__main__":
    main()