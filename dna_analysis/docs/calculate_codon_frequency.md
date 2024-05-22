# Count ATGC

Fecha: 04/04/2024

**Participantes**:

- [Santiago Orozco] < [santiago@lcg.unam.mx] >

## Descripción del Problema

Este programa toma un archivo de texto con una secuencia de nucleótidos desde la lína de comandos y cuenta las ocurrencias de los distintos codones de la secuencia. Además se le puede ingresar un marco de lectura específico (-3, -2, -1, 1, 2, 3), por default será 1.



## Especificación de Requisitos

Requisitos funcionales
- Se necesitan las funciones de la librería argparse.
- Aceptará un archivo desde línea de comandos.
- Se podrá especificar el marco de lectura
- Lee un archivo dado en formato string, solo acepta archivos con los caracteres a, t, g y c en mayúsculas o minúsculas.
- Cuenta cuantas veces aparece un codon en la secuencia
- Imprime el número de repeticiones de cada codon
  
Requisitos no funcionales

- El script deberá estar escrito en Python.
- El script es de tipo CLI
- El tiempo de respuesta debe ser rápido, incluso con archivos de gran tamaño.


## Análisis y Diseño


```
Función principal:
    Inicializar los contadores para cada letra
    Abrir el archivo en modo lectura 
    Procesar la secuencia respecto si el marco de lectura es negativo
    Iterar sobre cada línea del archivo
    Convertir la línea a minúsculas para contar sin distinción de mayúsculas/minúsculas
    Iterar sobre cada 3 caracter de la línea 
    Crea un diccionario que asocia la cadena del codon y un contador
    Incrementar el contador
    Imprimir los resultados de los contadores

```



#### Caso de uso: 

```
         +----------------+
         |   Usuario      |
         +-------+--------+
                 |
                 | 1. Proporciona archivo o datos de entrada
                 v
         +-------+--------+
         |  Diccionario   |
         |  de cada codon |
         |  con su        |
         |  contador      |
         +----------------+
```

- **Actor**: Usuario
- **Descripción**: El usuario proporciona un archivo de entrada con una secuencia de nucleótidos. El programa cuenta el número de repeticiones de cada codón.
- **Flujo principal**:

	1. Abre y lee el archivo llamado "archivo.txt" 
	2. Se recorre el arcivo por cada 3 caracteres
	3. Se utiliza la función count para contadar el codón que aparece
        4. Imprime el codón y su número de repetición 
	
- **Flujos alternativos**: [Casos que salen del uso común del programa]
        - Si el archivo es inexistente
                1. El programa manda un mensaje de error

	- Si el archivo está vacío
		1. El programa manda un mensaje de error

        - Si el archivo contiene caracteres inválidos
                1. El programa manda un mensaje de error

        - Argumentos inválidos de -n (distintos a ATGC)
                1. El programa manda un mensaje de error 
