# DNA Analysis

DNA Analysis es un paquete que contiene dos módulos, calculate_at_content y calculate_codon_frequency, ambos útiles al tratar con secuencias de DNA. 
Este programa toma un archivo de texto con una secuencia de nucleótidos desde la lína de comandos (programa CLI) y cuenta las ocurrencias de los símbolos 'A', 'C', 'G' y 'T'. Después imprime las ocurrencias. Se le puede especificar qué nucleótido quiere el usuario que se imprima.

## Uso:

Este programa puede ser ejecutado desde línea de comandos. Por la siguiente instrucción:
```
    % python count-atgc.py <archivo.txt>
    % python count-atgc.py <archivo.txt> -n A
    % python count-atgc.py <archivo.txt> -n T
    % python count-atgc.py <archivo.txt> -n G
    % python count-atgc.py <archivo.txt> -n C
    % python count-atgc.py <archivo.txt> -nucleotides A T G C
    % python count-atgc.py <archivo.txt> -h
```
Donde: <archivo.txt> es un argumento posicional que represente el archivo de la secuencia de nucleótidos; -n o -nucleotides es un argumento opcional que sirve para especificar el nucleotido que se quiere imprimir; -h es un argumento opcional que despliega el mensaje de ayuda.

## Salida:

El output del programa es un mensaje en donde especifica el nucleótido y su ocurrencia, para cada nucleótido solicitado. Ej:
```
# Output por default
El total por base es: A:<Número de As> T:<Número de Ts> G:<Número de Gs> C:<Número de Cs>
# Con la opción -n N
El total de Ns es:<Número de Ns>
```

## Control de errores:

Si el archivo proporcionado no existe, el script generará un mensaje de error. 
Si el archivo está vacío, el script generará un error. 
Si el archivo contiene caracteres inváidos, el script generará un error

## Pruebas:

El script incluye un conjunto de pruebas. Puede ejecutar estas pruebas de la siguiente manera:
```
# Caso standar
python count_atgc.py file.txt
# Caso standar 2
python count_atgc.py file.txt -n A
# Archivo inexistente
python count_atgc.py the_file_does_not_exist.txt
# Archivo vacío
python count_atgc.py empty_file.txt
# Archivo inválido
python count_atgc.py invalid_file.txt
# Argumentos no definidos
python count_atgc.py file.txt -n J

```

## Datos:

El script está diseñado para operar en archivos de texto plano, con una secuencia de nucleótidos (A, T, G, C) tanto en minúsculas como en mayúsculas. No hay restricciones en el tamaño del archivo.

## Metadatos y documentación

Este README ofrece información de uso básico. Para obtener información más detallada sobre el diseño y la implementación del script, consulte <.\count-atgc\docs\detalles_proyecto.md> o <.\count-atgc\docs\test_cases.md>, .

## Código fuente

El código fuente está disponible en este repositorio en la ruta <.\count-atgc\src\count_atgc.py>. Se acoge con satisfacción cualquier contribución o sugerencia a través de solicitudes pull request.

## Términos de uso

Este script está disponible bajo la licencia MIT License. Consulte el archivo LICENSE para obtener más detalles.

## Como citar

Si utiliza este script en su trabajo, por favor cite: [https://github.com/sorozcob/python-class/tree/main/count-atgc].

## Contáctenos

Si tiene problemas o preguntas, por favor abra un problema en este repositorio o póngase en contacto con nosotros en: <santiago@lcg.unam.mx>
