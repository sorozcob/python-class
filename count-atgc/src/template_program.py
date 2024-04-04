'''
NAME: count_atgc
       

VERSION: 
        

AUTHOR: Santiago Orozco
        

DESCRIPTION: Es un programa que al darle un archivo de secuencia de nucleótidos, regresa la cuenta del número de A, T, G, y C
        

CATEGORY
        

USAGE

    % python count:atgc
    

ARGUMENTS: 


METHOD


SEE ALSO


        
'''


# ===========================================================================
# =                            imports
# ===========================================================================





# ===========================================================================
# =                            Command Line Options
# ===========================================================================






# ===========================================================================
# =                            functions
# ===========================================================================





# ===========================================================================
# =                            main
# ===========================================================================


# step 1.


# step 2.


# step 3.

def contar_letras(archivo):
    conteo = {'a': 0, 't': 0, 'c': 0, 'g': 0}

    with open(archivo, 'r') as f:
        for linea in f:
            for caracter in linea.lower():
                if caracter in conteo:
                    conteo[caracter] += 1

    return conteo

archivo = 'nombre_del_archivo.txt'  # Reemplaza con el nombre de tu archivo
resultado = contar_letras(archivo)
print(resultado)


