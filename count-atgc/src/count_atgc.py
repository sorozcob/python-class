'''
NAME: count_atgc
       

VERSION: 2
        

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

# ===========================================================================
# =                            main
# ===========================================================================

# Aceptar argumentos desde línea de comandos

parser = argparse.ArgumentParser (description = "Lee archivo de entrada")
# Argumentos posicionales
parser.add_argument("input_file", type=str, help ="Nombre del archivo con la secuencia de nucleótidos")
# Argumentos opcionales
parser.add_argument("-n", "--nucleotides", type=str, choices=["A","T", "G", "C"], help="El (los) nucleotido(s) especifico(s) que se quieren imprimir")

#  Inicializar args
args = parser.parse_args()

# En este caso usé el método count:
with open(args.input_file, 'r') as f:
    ADN = f.read().upper
# Obtenemos la frecuencia de aparicion de cada letra.
if args.nucleotides == "A":
    print("")
print(f"El total por base es: A:{ADN.count('A')} T:{ADN.count('T')} G:{ADN.count('G')} C:{ADN.count('C')}")

