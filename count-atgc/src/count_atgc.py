'''
NAME: count_atgc
       

VERSION: 2
        

AUTHOR: Santiago Orozco
        

DESCRIPTION: Es un programa que al darle un archivo de secuencia de nucleótidos, regresa la cuenta del número de A, T, G, y C
        

CATEGORY: Herramienta que cuenta los nucleótidos de una secuencia
        

USAGE

    % python count-atgc.py
    % python count-atgc.py -n A
    % python count-atgc.py -n T
    % python count-atgc.py -n G
    % python count-atgc.py -n C
    

ARGUMENTS: archivo.txt: Archivo que contiene una secuencia de nucleótidos A, T, G y C


METHOD
    Primero se inicializan los contadores  para cada nucleótido (A, T, C y G). 
    Después, abre el archivo 'archivo.txt' e itera sobre cada línea del archivo. Cada línea se convierte a minúsculas para contar sin importar que sea mayúsculas y minúsculas.
    Aumenta el contador correspondiente según la letra del nucleótido encontrado ('A', 'T', 'C' o 'G').
    Al final imprime los resultados de los contadores para cada letra de nucleótido.


SEE ALSO


        
'''

# ===========================================================================
# =                           libreria
# ===========================================================================

import argparse
import argparse

# ===========================================================================
# =                            main
# ===========================================================================

# Aceptar argumentos desde línea de comandos

parser = argparse.ArgumentParser (description = "Lee archivo de entrada")
# Argumentos posicionales
parser.add_argument("-i","--input_file", type=str, help ="Nombre del archivo con la secuencia de nucleótidos")
# Argumentos opcionales
parser.add_argument("-n", "--nucleotides", type=str, choices=["a","t", "g", "c"], help="El (los) nucleotido(s) especifico(s) que se quieren imprimir")

#  Inicializar args
args = parser.parse_args()

# Inicializamos los contadores para cada letra
contador_a = 0
contador_t = 0
contador_c = 0
contador_g = 0

# Abrimos el archivo en modo lectura
with open(args.input_file, 'r') as f:
    # Iteramos sobre cada línea del archivo
    for linea in f:
        # Convertimos la línea a minúsculas para contar sin distinción de mayúsculas/minúsculas
        linea = linea.lower()
        # Iteramos sobre cada caracter de la línea
        for caracter in linea:
            # Incrementamos el contador correspondiente si el caracter es una de las letras a contar
            if caracter == 'a':
                contador_a += 1
            elif caracter == 't':
                contador_t += 1
            elif caracter == 'c':
                contador_c += 1
            elif caracter == 'g':
                contador_g += 1

# Imprimimos los resultados de los contadores
if args.nucleotides == "a":
       print(f'Letra A: {contador_a}')
if args.nucleotides == "t":
       print(f'Letra T: {contador_t}')
if args.nucleotides == "c": 
       print(f'Letra C: {contador_c}')
if args.nucleotides == "g":
       print(f'Letra G: {contador_g}')
else: 
       print(f'Letra A: {contador_a}')
       print(f'Letra T: {contador_t}')
       print(f'Letra C: {contador_c}')
       print(f'Letra G: {contador_g}')

# Te dejo una versión de código más simple, aún no hemos visto métodos en clase, pero son una cosa maravillosa que permite que puedas hacer un monton de cosas 
# En este caso usé el método count:
with open(args.input_file, 'r') as f:
    ADN = f.read().upper()
# Obtenemos la frecuencia de aparicion de cad aletra.
print(f"El total por base es: A:{ADN.count('A')} C:{ADN.count('C')} T:{ADN.count('T')} G:{ADN.count('G')}")

