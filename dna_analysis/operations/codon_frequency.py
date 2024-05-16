"""
codon_frequency.py: Módulo para calcular la frecuencia de codones en secuencias de ADN.

Este módulo proporciona funciones para determinar la frecuencia de los codones presentes 
en una secuencia de DNA dada. Este módulo puede ser útil en contextos en donde se necesita 
saber qué aminoácidos codifica una secuencia de DNA, y saber más sobre las características 
del péptido

Funciones:
- calculate_codon_frecuency(sequence, reading_frame): Devuelve la frecuencia de los codones 
presentes en la secuencia proporcionada.
"""

def calculate_codon_frequency(sequence, reading_frame):
    """
    Calcula la frecuencia de codones en una secuencia de ADN.

    Args:
        sequence (str): La secuencia de ADN a analizar.
        normalize (int): Puede ser -3, -2, -1, 1, 2 o 3. , determina cómo se van a leer y contar 
            los codones.

    Returns:
        dic_codon: es un diccionario que asocia el triplete del codón en la clave con su frecuencia

    Raises:
        ValueError: Si la secuencia está vacía o contiene caracteres no válidos. O si se ingresan 
            marcos de lectura sin sentido en reading_frame
    """

    # Validación básica de la secuencia
    if not sequence:
        raise ValueError("La secuencia proporcionada está vacía.")
    
    sequence = sequence.upper()
    if any(c not in 'ACGT' for c in sequence):
        raise ValueError("La secuencia contiene caracteres no válidos.")

    if reading_frame not in [1, 2, 3, -1, -2, -3]:
        raise ValueError("El marco de lectura debe ser 1, 2, 3, -1, -2 o -3.")
    
    dic_codon = {}

    # Ajustar la secuencia según el marco de lectura
    if reading_frame < 0:
        sequence = sequence[::-1].translate(str.maketrans("ATGC", "TACG"))
        reading_frame = abs(reading_frame)

    # Obtener la secuencia del marco de lectura especificado
    sequence = sequence[reading_frame - 1:] # Slicing, extraer una porción de una secuencia utilizando la sintaxis [inicio:fin:paso]

    # Dividir la secuencia en codones y contarlos
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i + 3] # Slicing
        if len(codon) == 3:
            dic_codon[codon] = dic_codon.get(codon, 0) + 1

    return dic_codon
    

if __name__ == "__main__":
    # Prueba de funcionalidad.
    test_sequence = "ATGACTGAT"
    print(f"Contenido de AT en la secuencia de prueba: {calculate_codon_frequency(test_sequence, 1)}%")