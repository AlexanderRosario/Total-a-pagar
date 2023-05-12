# Readme.md

## Descripción General

El código proporcionado es un script de Python diseñado para calcular el salario de los empleados basándose en un archivo de texto que contiene las horas de trabajo de cada empleado. El script lee el archivo, extrae y procesa la información para determinar las horas trabajadas y luego calcula el salario basándose en las tarifas establecidas para diferentes períodos del día y de la semana.

## Arquitectura

La solución está escrita en Python y consta de una función principal llamada `calcular_pago(file)`. Esta función toma como argumento la ruta de un archivo de texto que contiene los registros de las horas de trabajo de los empleados.

El código comienza por leer el archivo de texto, dividiendo cada línea en el nombre del empleado y su horario de trabajo. El horario de trabajo se procesa aún más para determinar el día de la semana y las horas de inicio y finalización.

Luego, utilizando esta información, el código calcula la duración total del trabajo en horas y multiplica esta duración por la tarifa correspondiente según el horario y el día de la semana.

Finalmente, la función devuelve un diccionario que mapea los nombres de los empleados a sus salarios calculados.

## Enfoque y Metodología

El enfoque tomado en este script es principalmente procedural, con un enfoque en el procesamiento de texto y la manipulación de datos.

La primera parte del código se enfoca en la lectura y el procesamiento de la entrada del archivo de texto. Para hacerlo, se utilizan las funciones de string incorporadas en Python para dividir y manipular el texto de entrada.

La segunda parte del código se centra en calcular las horas trabajadas y el salario correspondiente. Aquí, se utilizan las estructuras de control de flujo y las operaciones matemáticas para determinar el salario basado en las tarifas predefinidas.

### Puntos a considerar

Aunque el programa funciona correctamente, no se tuvieron en cuenta algunos posibles errores.

¿Qué sucede si un empleado trabaja hasta el siguiente segmento de trabajo? Por ejemplo, si inicia a las 08:00 y concluye a las 11:00.

Asume que el horario de trabajo es dentro del mismo día y no cruza la medianoche.


## Cómo Ejecutar el Programa Localmente

Para ejecutar este script de Python localmente, siga estos pasos:

1. Asegúrese de tener Python instalado en su computadora. Si no lo tiene, puede descargarlo desde el [sitio oficial de Python](https://www.python.org/).

2. Descargue el script de Python y asegúrese de tener un archivo de texto con la información de las horas de trabajo de los empleados en el mismo directorio. Asegúrese de que el archivo de texto esté en el formato correcto.

3. Abra una terminal o un prompt de comando.

4. Navegue hasta el directorio donde descargó el script y el archivo de texto.

5. Ejecute el script con el comando `python <nombre del script>.py`.

Después de ejecutar el script, debería ver los salarios calculados para cada empleado en su terminal o prompt de comando.

