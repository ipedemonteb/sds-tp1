# TP1 - Simulación de Sistemas

El presente trabajo implementa y analiza el Cell Index Method para detectar vecinos en sistemas de partículas bidimensionales, desarrollado en el marco de la materia Simulación de Sistemas del Instituto Tecnológico de Buenos Aires. El objetivo es comparar su desempeño contra la solución de fuerza bruta, evaluar el impacto de distintos parámetros y generar visualizaciones de las configuraciones resultantes.

Las funcionalidades incluidas son las siguientes:

- <b>Método de Cell Index</b>: Construye una grilla MxM para acelerar la detección de partículas vecinas con y sin condiciones periódicas de contorno.
- <b>Referencia de Fuerza Bruta</b>: Calcula los vecinos sin optimizaciones para validar resultados y medir diferencias de performance.
- <b>Análisis de Desempeño</b>: Ejecuta experimentos variando M y N, midiendo tiempos de ejecución y generando curvas comparativas.
- <b>Visualización</b>: Produce archivos de simulación y grafica la configuración de partículas, destacando vecinos y la partícula foco.
- <b>Generación de Datos</b>: Registra en disco el estado estático, dinámico y las listas de vecinos para su posterior análisis.

<details>
  <summary>Contenidos</summary>
  <ol>
    <li><a href="#instalación">Instalación</a></li>
    <li><a href="#instrucciones">Instrucciones</a></li>
    <li><a href="#manual-de-usuario">Manual de Usuario</a></li>
    <li><a href="#integrantes">Integrantes</a></li>
  </ol>
</details>

## Instalación

Clonar el repositorio:

- HTTPS:
  ```sh
  git clone https://github.com/martinAleB/sds-tp1.git
  ```
- SSH:
  ```sh
  git clone git@github.com:martinAleB/sds-tp1.git
  ```

Desde la raíz del proyecto puede crearse un entorno virtual y activar las dependencias necesarias:

```sh
python3 -m venv .venv
source .venv/bin/activate  # Linux / macOS
# .venv\Scripts\activate  # Windows PowerShell
pip install matplotlib
```

> **Requisito**: Python 3.10 (o superior) con `pip` disponible.

<p align="right">(<a href="#tp1---simulación-de-sistemas">Volver</a>)</p>

## Instrucciones

Todos los comandos deben ejecutarse desde la raíz del repositorio con el entorno virtual (si se creó) ya activado. Los scripts principales son:

- `Simulation.py`: genera partículas aleatorias y calcula vecinos con Cell Index Method.
- `Visualizer.py`: grafica los resultados guardados para una simulación específica.
- `Performance_M_Variation.py`: analiza el impacto de M manteniendo fija la cantidad de partículas.
- `Performance_N_Variation.py`: compara Cell Index Method contra fuerza bruta variando N.
- `Test.py`: valida que ambos enfoques produzcan exactamente los mismos vecinos.

<p align="right">(<a href="#tp1---simulación-de-sistemas">Volver</a>)</p>

## Manual de Usuario

A continuación se detallan los comandos y parámetros de cada script. En todos los casos se asume que el comando se ejecuta desde el directorio raíz del proyecto.

### Simulación principal

```sh
python3 Simulation.py
```

El script solicitará los siguientes parámetros por consola:
- `N`: cantidad de partículas a generar.
- `L`: longitud del lado de la grilla cuadrada.
- `r_c`: radio de interacción para considerar vecinos.
- `r`: radio de cada partícula.
- `M`: cantidad de celdas por eje (debe cumplir `M ≤ L / (r_c + 2r)`).
- `periodic`: `1` para activar contorno periódico, `0` para contorno abierto.

Al finalizar, se crean archivos bajo `data/` con el estado estático (`timestamp.txt`), dinámico (`timestamp-0.txt`) y las listas de vecinos (`timestamp-output.txt`). La partícula elegida como foco se marca en verde y sus vecinos en azul.

### Visualización de resultados

```sh
python3 Visualizer.py
```

Al ejecutarlo, se debe ingresar la `timestamp` generada por una corrida previa. El script lee los archivos correspondientes dentro de `data/` y muestra un gráfico con las posiciones de las partículas coloreadas según su rol (foco, vecinos, resto).

### Performance variando M

```sh
python3 Performance_M_Variation.py
```

El script fija `N`, `L`, `r` y `r_c`, solicita si se desean condiciones periódicas y recorre todos los valores válidos de `M`, midiendo el tiempo de ejecución del Cell Index Method. Finalmente grafica la curva de tiempos en función de `M`.

### Performance variando N

```sh
python3 Performance_N_Variation.py
```

Tras elegir si se ejecuta con contorno periódico, genera conjuntos de partículas para distintos valores de `N`, compara los tiempos de Cell Index Method y fuerza bruta, y grafica ambas curvas para visualizar la mejora del algoritmo.

### Pruebas de correctitud

```sh
python3 Test.py
```

Ejecuta ambos algoritmos para un mismo conjunto de partículas, ordena los resultados y verifica que las listas de vecinos coincidan elemento por elemento, reportando éxito en modo contorno abierto y periódico.

<p align="right">(<a href="#tp1---simulación-de-sistemas">Volver</a>)</p>

## Integrantes

Martín Alejandro Barnatán (64463) - mbarnatan@itba.edu.ar

Ignacio Martín Maruottolo Quiroga (64611) - imaruottoloquiroga@itba.edu.ar

Ignacio Pedemonte Berthoud (64908) - ipedemonteberthoud@itba.edu.ar

<p align="right">(<a href="#tp1---simulación-de-sistemas">Volver</a>)</p>
