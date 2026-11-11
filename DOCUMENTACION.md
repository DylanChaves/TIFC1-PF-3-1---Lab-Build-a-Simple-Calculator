# Laboratorio: calculadora sencilla en Python

**Estudiante:** Dylan Sánchez Chávez  
**Repositorio:** TIFC1-PF-3-1---Lab-Build-a-Simple-Calculator

## 1. Objetivo

Desarrollar una calculadora de consola que lea dos números, los sume e imprima el resultado. Después de esta tarea obligatoria, ofrecer las funciones adicionales descritas en el README original.

## 2. Archivos

| Archivo | Función |
| --- | --- |
| `main.py` | Código comentado de la calculadora. |
| `test.py` | Dos pruebas originales del laboratorio, conservadas sin cambios. |
| `README.md` | Instrucciones originales del laboratorio, conservadas sin cambios. |
| `DOCUMENTACION.md` | Explicación del funcionamiento, ejecución y validación. |

## 3. Requisitos y ejecución en Visual Studio Code

Se necesita Python 3. No se requieren paquetes externos para ejecutar la calculadora.

1. Descargue o clone el repositorio y abra su carpeta en Visual Studio Code.
2. Abra una terminal desde **Terminal > Nueva terminal**.
3. Ejecute `python main.py`. En Windows también puede usar `py main.py` si ese es el comando disponible.
4. Escriba el primer número y presione Enter. Escriba el segundo y presione Enter. Estas dos entradas iniciales no muestran preguntas para mantener sencilla la salida que recibe el evaluador.
5. Observe la suma y seleccione una opción del menú. Escriba `0` para salir.

Use punto para los decimales, por ejemplo `2.5`.

## 4. Desarrollo y explicación del código

### Lectura de datos

`input()` recibe texto desde la consola. `leer_numero()` usa `float()` para convertirlo en un número y permitir valores enteros, negativos y decimales. Un ciclo `while` repite la solicitud si la conversión falla. `math.isfinite()` rechaza entradas como `nan` e `inf`.

### Suma obligatoria

`main()` solicita dos números y los suma con `+`. `mostrar_resultado()` imprime el resultado y elimina el `.0` cuando el valor es entero: con entradas `1` y `6`, la salida del resultado es `7`.

### Menú de operaciones

El menú se muestra después de la suma inicial, tal como exige el README. Un ciclo permite realizar varias operaciones sin reiniciar el programa. El diccionario `OPERACIONES` relaciona cada símbolo con una función del módulo estándar `operator`.

| Opción | Operación | Ejemplo | Resultado |
| --- | --- | --- | --- |
| 1 | Suma | 8 + 2 | 10 |
| 2 | Resta | 8 - 2 | 6 |
| 3 | Multiplicación | 8 * 2 | 16 |
| 4 | División | 9 / 2 | 4.5 |
| 5 | Módulo o residuo | 10 % 3 | 1 |
| 6 | Suma de tres números | 1 + 2 + 3 | 6 |
| 7 | Operaciones combinadas | 2 + 4 - 3 | 3 |
| 0 | Salida | Finaliza la interacción | — |

### Operaciones combinadas

`evaluar_expresion()` usa `ast.parse()` para convertir el texto en una estructura de operaciones. La función interna `resolver()` recorre esa estructura y admite únicamente números, signos positivos o negativos, paréntesis y los operadores `+`, `-`, `*`, `/` y `%`.

Se respeta la prioridad matemática: `4 * 5 + 1 / 3` produce aproximadamente `20.333333333333332`. Los paréntesis permiten cambiar el orden: `(2 + 4) * -3` produce `-18`.

No se utiliza `eval()`; se rechazan nombres de variables, llamadas a funciones, potencias y otros elementos ajenos a las operaciones permitidas. La expresión tiene un límite de 200 caracteres.

### Manejo de errores

Las entradas numéricas incorrectas se vuelven a solicitar. Las opciones inexistentes muestran un aviso y regresan al menú. La división y el módulo entre cero muestran un mensaje sin cerrar el programa. Las expresiones inválidas y los resultados fuera de rango también se controlan.

Cuando se termina la entrada estándar, `EOFError` permite salir sin un traceback. Esto es necesario porque las pruebas originales proporcionan únicamente los dos números de la suma inicial.

La condición `if __name__ == "__main__":` inicia la calculadora cuando se ejecuta el archivo y permite importar sus funciones sin pedir datos.

## 5. Ejemplo de uso

Primero escriba `11` y luego `15`, cada uno en una línea. La calculadora imprime `26` y presenta el menú.

Para multiplicar, seleccione `3`, escriba `4` como primer número y `5` como segundo. El resultado es `20`. Después escriba `0` para terminar.

## 6. Validación realizada

Se ejecutaron correctamente las dos funciones de prueba incluidas en `test.py`:

| Prueba original | Entradas | Resultado esperado | Estado |
| --- | --- | --- | --- |
| `test_one_six` | 1 y 6 | 7 | Correcta |
| `test_eleven_fifteen` | 11 y 15 | 26 | Correcta |

Además, se realizaron 19 verificaciones adicionales: 12 ejecuciones de consola con números negativos, decimales, opciones del menú y errores; dos comprobaciones de prioridad y paréntesis; y cinco comprobaciones de rechazo de operaciones o expresiones no permitidas. Todas pasaron. Estas verificaciones adicionales se ejecutaron durante la preparación y no se añadieron a `test.py`.

Las pruebas originales se ejecutaron directamente con Python, porque `pytest` no estaba instalado en el entorno de preparación. Para repetirlas sin instalar dependencias, desde la carpeta del proyecto ejecute:

```bash
python -c "import test; test.test_one_six(); test.test_eleven_fifteen(); print('2 pruebas correctas')"
```

Si dispone de `pytest`, también puede ejecutar `python -m pytest test.py`.

Estas comprobaciones son locales; no representan una calificación emitida por la plataforma educativa. Según el README, las funciones adicionales se califican manualmente.

## 7. Alcance y limitaciones

La calculadora funciona en consola y cubre la tarea obligatoria y todas las funciones opcionales enumeradas en el README. Usa números de punto flotante para las entradas individuales; por ello puede mostrar aproximaciones como `0.30000000000000004` al sumar `0.1` y `0.2`. No ofrece una interfaz gráfica ni guarda un historial.

## 8. Conclusión

El laboratorio aplica entrada y salida de datos, conversión de tipos, operadores aritméticos, condicionales, ciclos, funciones, diccionarios y manejo de excepciones. La suma inicial se conserva como primera tarea y el menú permite ampliar la calculadora después de mostrar ese resultado.
