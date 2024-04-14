# Casos de prueba o escenarios

Introducción sobre el programa y los casos de prueba.
    
### Caso de prueba 1: Validación del input del usuario

- Descripción: Para este caso, se le proporciona al programa un path de un archivo inexistente, para observar si el programa lo maneja adecuadamente. 
- Datos de entrada: El archivo no existe
```{python}
python count-atcg.py the_file_does_not_exist.txt 
```
- Resultado esperado:
Mensaje de error

### Caso de prueba 2: Input Vacío

- Descripción: Sí el archivo existe, pero es un archivo vacío
- Datos de entrada: El archivo está vacío
```
python count-atcg.py empty_file.txt
```
- Resultado esperado: Mensaje de error


### Caso de prueba 3: Input con caracteres inválidos

- Descripción: Archivo con caracteres inválidos, diferentes a A,T,G,C en minúsculas o mayúsculas
- Datos de entrada: Archivo erroneo
```
python count-atgc.py invalid_file.txt
```
- Resultado esperado: Mensaje de error

### Caso de prueba 4: * Argumentos de -n diferentes de A, T, G, C

- Descripción: Argumentos inválidos de -n
- Datos de entrada: 
```
python count-atgc file.txt -n 
```
- Resultado esperado: Mensaje de error


