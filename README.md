# Generador de numeros rectangulares

En esta actividad realizaremos 2 generadores de numeros pseudoaleatorios, y una funcion que nos ayudaran a determinar:
1. Su periocidad
2. Que numeros no son generados, si es que no los hay

Utiliza el lenguaje de programacion con el que te sientas mas comodo.

## Periocidad
1. Crea una funcion llamado "periocidad" el cual recive como entrada un arreglo y "m"
2. Revisa el arreglo hasta encontrar una repeticion, es decir, dado el arreglo "[2, 3, 4, 9, 10, 16, 2, 3, 4]", el programa debera deternese hasta el indice 6, es decir la saegunda repeticion del numero "2"
3. Calcula el numero de periocidad, es decir el indice + 1
4. Si la periocidad no es completa: Crea otro arreglo el cual contenga los valores que no estan dentro de la secuencia entre el rango [1, m]

## Generador Congruencial Mixto
1. Crea una funcion llamado "mixto" el cual recive como entrada una semilla "Xo" y un limite
2. Utiliza los valores 5, 7 y 8 para a, c, y m respectivamente
3. Itera la funcion vista en clase y genera un arreglo de tamaño limite con los numeros obtenidos en la funcion
4. Devuelve el arreglo

## Generador Congruencial Multiplicativo
En esta funcion "multiplicado" debera tambien de tomar como entrada una semilla y un limite.

Sigue los mismos pasos de la actividad anterior para realizar este generador, pero esta vez utliza los valores 5 y 39 para a y m respectivamente

## Actividades
1. Utiliza semillas distintas y obten los valores aleatorios y la periocidad en cada generador

2. Determine el periodo de los siguientes generadores mixtos


| a  | c  | m   | Xo |
|----|----|-----|----|
| 8  | 16 | 100 | 15 |
| 50 | 17 | 64  | 13 |
| 9  | 13 | 32  | 8  |

3. Determine el periodo de los siguientes generadores multiplicativos


| a   | m    | Xo |
|-----|------|----|
| 203 | 10^5 | 17 |
| 221 | 10^3 | 3  |
| 5   | 64   | 7  |

4. Obtenga los parametros (a, c, m y Xo) de un Generador Mixto que asegure un periodo completo
5. Obtenga los parametros (a, m y Xo) de un Generador Multiplicativo que asegure un periodo completo

Escribe tus respuesta en un archivo llamado "resultados.md"
