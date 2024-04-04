# Nombre del Proyecto

Fecha: count_atgc

**Participantes**:

- [Santiago Orozco] < [santiago@lcg.unam.mx] >

## Descripción del Problema

Cuenta las ocurrencias de los símbolos 'A', 'C', 'G' y 'T' de una cadena de DNA que lee a través de un archivo



## Especificación de Requisitos


Requisitos funcionales

- Leer números de un archivo dado en formato string.
- Cuenta cuantas veces aparece la letra A, T, G y C en el archivo.
- Imprime el número de repeticiones de cada nucleótido

Requisitos no funcionales

- El script deberá estar escrito en Python.
- El tiempo de respuesta debe ser rápido, incluso con archivos de gran tamaño.


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
	2. Se recorre el arcivo línea por línea
	3. Se suma 1 al contador dependiendo del símbolo que aparece
        4. Imprime el número de repeticines por cada nucleótido
	
- **Flujos alternativos**: [Casos que salen del uso común del programa]
	- Si el archivo se llama de otra manera que no sea "archivo.txt" 
		1. El programa no se ejecuta

        
