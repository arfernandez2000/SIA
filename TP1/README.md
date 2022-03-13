# Rompecabezas de 8 numeros

<span style="color:blue">
## Integrantes:
* Ariadna Fernandez Truglia
* Florencia Chao
* Faustino Maggioni Duffy
</span>.

### Descripcion del proplema:
* El Rompecabezas de 8 numeros presenta una grilla con con 9 celdas, 8 ocupadas con los numeros del 1 al 8 y la otra vacia. El objetivo, o por lo menos el de nuestro programa es dejar los 8 numeros ordenados de menor a mayor con la ultima celda libre.

### Requerimientos previos:
* Python 3
* Las librerias utilizadas estan en requeriments.txt, instalar usando pip

### Configuracion y ejecucion:
* Crear archivo config.json con parametros deseados. Aclarar "method" ("A_STAR", "GLOBAL_H", "LOCAL_H", "BPP", "BPA", "BPPV"), si el metodo es alguno de los primeros tres, en "informed" colocar un 1 y si no, un 0. Aclarar "heuristic" ("rowcol", "tile", "linear") si es que "informed" esta seteado en 1. Setear tambien "map" con un txt que contenga una secuencia en cualquier orden de los numeros 0 a 8.
* Ejecutar con '$ py 8puzzle.py'