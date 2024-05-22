"""
calculate_codon_frequency.py: Script para calcular la frecuencia de los codones en una secuencia de ADN.

Este script lee una secuencia de ADN desde un archivo dado y calcula la frecuencia de los codones presentes.
La secuencia de ADN debe estar en un archivo de texto y solo contener los caracteres 'A', 'C', 'G' o 'T'.
Adicionalmete, se puede seleccionar el marco de lectura, que puede ser -3, -2, -1, 1, 2, o 3. 

Uso:
    python calculate_codon_frequency.py <path_to_dna_file> [--normalize]

Argumentos:
    <path_to_dna_file> : Ruta al archivo de texto que contiene la secuencia de ADN.
    --normalize        : Opción para normalizar el contenido de AT excluyendo 'N's del c
"""

import argparse
import sys
sys.path.append("/Users/soroz/Desktop/python-class/dna_analysis/utils")
sys.path.append("/Users/soroz/Desktop/python-class/dna_analysis/operations")
from codon_frequency import calculate_codon_frequency
from file_io import read_dna_sequence

def main():

    parser = argparse.ArgumentParser(description="Calcula la frecuencia de codones en una secuencia de ADN.")
    parser.add_argument("file", type=str, help="Archivo de ADN del cual leer la secuencia.")
    parser.add_argument("-f", "--frame", type=int, default=1, help="Marco de lectura, por default es 1.")

    args = parser.parse_args()
    file_path = args.file
    reading_frame = args.frame

    try:
        # Leer la secuencia del archivo especificado utilizando la función proporcionada por file_io.py
        sequence = read_dna_sequence(file_path)
        
        # Calcular la frecuencia utilizando la función proporcionada por acodon_frequency.py
        codon_frequency = calculate_codon_frequency(sequence, reading_frame)
        
        # Mostrar el resultado al usuario
        print("La frecuencia de los codones es:")
        for clave, valor in codon_frequency.items():
            print(clave, ":", valor)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()