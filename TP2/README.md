# El Problema de la Mochila

## Integrantes:
* [Ariadna Fernandez Truglia](https://github.com/arfernandez2000)
* [Florencia Chao](https://github.com/florchao)
* [Faustino Maggioni Duffy](https://github.com/maggioniduffy)

## Descripcion del proplema:
* El Problema de la Mochila presenta una mochila con cierta capacidad y N elementos con cuales cargarla. Cada elemento tiene un beneficio y un peso asociado y se intenta maximizar el beneficio sin que el peso sobrepase la capacidad de la mochila.

## Requerimientos previos:
* Python 3
* Matplotlib
    * Instalacion: 
    1. `python -m pip install -U pip`
    2. `python -m pip install -U matplotlib`

## Configuracion y ejecucion:
Crear archivo config.json en la carpeta donde se encuentra el archivo main.py, con los parametros deseados. Aclarar "P" (tamaño), "file" (un archivo txt con los datos de la mochila*), "mutatrion_prob" (probabilidad de que algun gen de un individuo cambie).

En "selection" especificar "method" (metodo de seleccion para los P individuos de una nueva generacion), "truncated_k" (para elegir cuantos individuos con peor fitness descartar), "boltzman_k" (constante utilizada en el metodo de seleccionde boltzman) y "T0" y "Tc" que son las temperaturas iniciales y mininmas, respectivamente, que utiliza ,la funcion de temperatura en el metodo boltzman.

En "crossover" definir "points" que son los puntos que se utilizan para separar los genes de los individuos y cruzarlos. Si es 0, sera una cruza uniforme. Si es 1, sera una simple. Y si es > 1, sera una cruza multiple.

Por ultimo en "stop" definimos las condiciones de corte. La primera, "unchanged_generations", indica despues de cuantas generaciones sin cambios cortar el algoritmo genetico. La segunda, "max_generations", indica cuantas generaciones en total pueden ser creadas por el algoritmo.

* Ejecutar con '$ python3 main.py' o '$py main.py'
#### Ejemplos de configuración:
  
  ```
  {
    "P": 100,
    "file": "source/Mochila100Elementos.txt",
    "mutation_prob": 0.001,
    "selection": {
        "method": "boltzman", 
        "truncated_k": 0,
        "boltzman_k" : 1,
        "T0" : 100,
        "Tc" : 70
    },
    "crossover": {
        "points": 0
    },
    "stop": {
        "unchanged_generations": 50,
        "max_generations": 500
    }
  }
  ```
 
  ```
  {
    "P": 100,
    "file": "source/Mochila100Elementos.txt",
    "mutation_prob": 0.005,
    "selection": {
        "method": "boltzman", 
        "truncated_k": 5,
        "boltzman_k" : 5,
        "T0" : 150,
        "Tc" : 70
    },
    "crossover": {
        "points": 5
    },
    "stop": {
        "unchanged_generations": 20,
        "max_generations": 500
    }
  }
  ```