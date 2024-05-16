'''
NAME: count_atgc
       

VERSION: 3
        

AUTHOR: Santiago Orozco
        

DESCRIPTION: Es un programa que al darle un archivo de secuencia de nucleótidos por línea de comando, regresa la cuenta del número de A, T, G, y C
        

CATEGORY: Herramienta que cuenta los nucleótidos de una secuencia
        

USAGE

    % python count-atgc.py <archivo.txt>
    % python count-atgc.py <archivo.txt> -n A
    % python count-atgc.py <archivo.txt> -n T
    % python count-atgc.py <archivo.txt> -n G
    % python count-atgc.py <archivo.txt> -n C
    % python count-atgc.py <archivo.txt> -nucleotides A T G C
    % python count-atgc.py <archivo.txt> -h

ARGUMENTS: 
usage: count_atgc.py [-h] -n {A,T,G,C} input_file

positional arguments:
  input_file            Nombre del archivo con la secuencia de nucleótidos

options:
  -h, --help            show this help message and exit
  -n {A,T,G,C}, --nucleotide {A,T,G,C}
                        Escoge que nucleótido quieres imprimir 



METHOD
    Se importa la librería argparse. Se toma un archivo desde línea de comandos en formato string.
    Solo acepta archivos con los caracteres a, t, g y c en mayúsculas o minúsculas.
    Se podrá especificar qué nucleótido específico se imprimirá.
    Lee el archivo y cuenta cuantas veces aparece la letra A, T, G y C en el archivo, usando la función count.
    Aumenta el contador correspondiente según la letra del nucleótido encontrado ('A', 'T', 'C' o 'G').
    Cada caracter se convierte a mayúsculas, para contar sin importar que sea mayúsculas y minúsculas.
    Imprime el número de repeticiones de cada nucleótido o del nucleótido especificado.


SEE ALSO

        
'''

# ===========================================================================
# =                           libreria
# ===========================================================================

import argparse
import os #Módulo estándar que proporciona una interfaz para interactuar con el sistema operativo en el que se está ejecutando 


# ===========================================================================
# =                            Command Line Options
# ===========================================================================

# Aceptar argumentos desde línea de comandos
parser = argparse.ArgumentParser (description = "Lee archivo de entrada")

# Argumentos posicionales
parser.add_argument("input_file", 
                    type=str, 
                    help ="Nombre del archivo con la secuencia de nucleótidos")

# Argumentos opcionales
parser.add_argument("-n", "--nucleotides", 
                    type=str, 
                    default = "atgc", 
                    choices=["a","t", "g", "c", "A", "T", "G", "C"], 
                    help="El (los) nucleotido(s) especifico(s) que se quieren imprimir")

#  Inicializar args
args = parser.parse_args()


# ===========================================================================
# =                            functions
# ===========================================================================

def errortesting (file):
    # En este caso usé el método count:
    try:
        with open(file, 'r') as f:
            ADN = f.read().upper()
    except IOError:
        print("No se encontró el archivo :'(")
    if os.path.getsize(file) == 0: # Comprobar si el archivo está vacío, si cierto, cerrar el programa
        #path es un submódulo que proporciona funciones para manipular rutas de archivos y directorios
        #getsize es una función que devuelve el tamaño en bytes de un archivo
        print("El archivo está vacío")
        exit()
    '''
    if ADN != "A" and ADN != "a" and ADN != "T" and ADN != "t" and ADN != "G" and ADN != "g" and ADN != "C" and ADN != "c" and ADN != " " and ADN != "\n":
        print("Sequence contains")
        for caracter in ADN:
                if caracter != "A" and caracter != "a" and caracter != "T" and caracter != "t" and caracter != "G" and caracter != "g" and caracter != "C" and caracter != "c" and ADN != " " and ADN != "\n":
                    print(caracter) 
        print(", is (are) invalid character(s)")
        exit()
    '''
    return(ADN)

def frecuencia (ADN, nucleotido):
    # Obtenemos la frecuencia de aparicion de cada letra.
    if nucleotido == "A" or nucleotido == "a":
        print(f"El total de As es: {ADN.count('A')}")
    if nucleotido == "T" or nucleotido == "t":
        print(f"El total de Ts es: {ADN.count('T')}")
    if nucleotido == "G" or nucleotido == "g":
        print(f"El total de Gs es: {ADN.count('G')}")
    if nucleotido == "C" or nucleotido == "c":
        print(f"El total de Cs es: {ADN.count('C')}")


# ===========================================================================
# =                            main
# ===========================================================================

ADN = errortesting(args.input_file)
frecuencia(ADN, args.nucleotides)
if args.nucleotides == "atgc" :
    print(f"El total por base es: A:{ADN.count('A')} T:{ADN.count('T')} G:{ADN.count('G')} C:{ADN.count('C')}")


'''
###
from itertools import combinations

cadena = "ABC"
longitud_combinacion = 2

# Obtener todas las combinaciones de longitud 2 de los caracteres de la cadena
combinaciones = list(combinations(cadena, longitud_combinacion))

# Imprimir las combinaciones obtenidas
for combinacion in combinaciones:
     print(''.join(combinacion))
'''