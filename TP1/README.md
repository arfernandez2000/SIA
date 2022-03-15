# Rompecabezas de 8 numeros

## Integrantes:
* [Ariadna Fernandez Truglia](https://github.com/arfernandez2000)
* [Florencia Chao](https://github.com/florchao)
* [Faustino Maggioni Duffy](https://github.com/maggioniduffy)

## Descripcion del proplema:
* El Rompecabezas de 8 numeros presenta una grilla con con 9 celdas, 8 ocupadas con los numeros del 1 al 8 y la otra vacia. El objetivo, o por lo menos el de nuestro programa es dejar los 8 numeros ordenados de menor a mayor con la ultima celda libre.

## Requerimientos previos:
* Python 3

## Configuracion y ejecucion:
* Crear archivo config.json en la carpeta donde se encuentra el archivo 8puzzle.py, con parametros deseados. Aclarar "method" ("A_STAR", "GLOBAL_H", "LOCAL_H", "BPP", "BPA", "BPPV"), si el metodo es alguno de los primeros tres, en "informed" colocar un 1 y si no, un 0. Si es método informado, aclarar "heuristic" ("rowcol", "tile", "linear"). Setear tambien "map" con un txt que contenga una secuencia en cualquier orden de los numeros 0 a 8.
* Ejecutar con '$ py 8puzzle.py'
#### Ejemplos de configuración:
  
  ```
  {
    "method": "GLOBAL_H",
    "heuristic": "tile",
    "map": "maps/map1.txt",
    "informed": 1
  }
  ```
 
  ```
  {
    "method": "BPA",
    "map": "maps/map2.txt",
    "informed": 0
  }
  ```
  
  ```
  {
    "method": "A_STAR",
    "heuristic": "rowcol",
    "map": "maps/map3.txt",
    "informed": 1
  }
  ```
