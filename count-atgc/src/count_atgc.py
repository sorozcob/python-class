'''
NAME: count_atgc
       

VERSION: 1
        

AUTHOR: Santiago Orozco
        

DESCRIPTION: Es un programa que al darle un archivo de secuencia de nucleótidos, regresa la cuenta del número de A, T, G, y C
        

CATEGORY: Herramienta que cuenta los nucleótidos de una secuencia
        

USAGE

    % python count_atgc.py
    

ARGUMENTS: archivo.txt: Archivo que contiene una secuencia de nucleótidos A, T, G y C


METHOD
    Primero se inicializan los contadores  para cada nucleótido (A, T, C y G). 
    Después, abre el archivo 'archivo.txt' e itera sobre cada línea del archivo. Cada línea se convierte a minúsculas para contar sin importar que sea mayúsculas y minúsculas.
    Aumenta el contador correspondiente según la letra del nucleótido encontrado ('A', 'T', 'C' o 'G').
    Al final imprime los resultados de los contadores para cada letra de nucleótido.


SEE ALSO


        
'''

# ===========================================================================
# =                            main
# ===========================================================================


# Inicializamos los contadores para cada letra
contador_a = 0
contador_t = 0
contador_c = 0
contador_g = 0

# Abrimos el archivo en modo lectura
with open('archivo.txt', 'r') as f:
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
print(f'Letra A: {contador_a}')
print(f'Letra T: {contador_t}')
print(f'Letra C: {contador_c}')
print(f'Letra G: {contador_g}')