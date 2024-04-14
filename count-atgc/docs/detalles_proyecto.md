# Count ATGC

Fecha: 04/04/2024

**Participantes**:

- [Santiago Orozco] < [santiago@lcg.unam.mx] >

## Descripción del Problema

Este programa toma un archivo de texto con una secuencia de nucleótidos desde la lína de comandos y cuenta las ocurrencias de los símbolos 'A', 'C', 'G' y 'T'. Después imprime las ocurrencias. Se le puede especificar qué nucleótido quiere el usuario que se imprima.



## Especificación de Requisitos

Requisitos funcionales
- Se necesitan las funciones de la librería argparse.
- Aceptará un archivo desde línea de comandos.
- Se podrá especificar qué nucleótido específico se imprimirá.
- Lee un archivo dado en formato string, solo acepta archivos con los caracteres a, t, g y c en mayúsculas o minúsculas.
- Cuenta cuantas veces aparece la letra A, T, G y C en el archivo.
- Imprime el número de repeticiones de cada nucleótido o del nucleótido especificado.

Requisitos no funcionales

- El script deberá estar escrito en Python.
- El script es de tipo CLI
- El tiempo de respuesta debe ser rápido, incluso con archivos de gran tamaño.
- 

## Análisis y Diseño


```
Función principal:
    Inicializar los contadores para cada letra
    Abrir el archivo en modo lectura 
    Iterar sobre cada línea del archivo
    Convertir la línea a minúsculas para contar sin distinción de mayúsculas/minúsculas
    Iterar sobre cada caracter de la línea
    Incrementar el contador correspondiente si el caracter es una de las letras a contar
    Imprimir los resultados de los contadores

```



#### Caso de uso: 

```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona archivo o datos de entrada
                 v
         +-------+-------+
         |  Contador de  |
         |  repeticiones |
         |  para cada    |
         |  nucleótido   |
         +---------------+
```

- **Actor**: Usuario
- **Descripción**: El usuario proporciona un archivo de entrada con una secuencia de nucleótidos. El programa cuenta el número de repeticiones de cada nucleótido.
- **Flujo principal**:

	1. Abre y lee el archivo llamado "archivo.txt" 
	2. Se recorre el arcivo caracter por carecter 
	3. Se utiliza la función count para contadar el símbolo que aparece
        4. Imprime el número de repeticines por cada nucleótido
	
- **Flujos alternativos**: [Casos que salen del uso común del programa]
        - Si el archivo es inexistente
                1. El programa manda un mensaje de error

	- Si el archivo está vacío
		1. El programa manda un mensaje de error

        - Si el archivo contiene caracteres inválidos
                1. El programa manda un mensaje de error

        - Argumentos inválidos de -n (distintos a ATGC)
                1. El programa manda un mensaje de error 
