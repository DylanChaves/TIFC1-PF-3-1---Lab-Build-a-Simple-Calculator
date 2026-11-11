import ast
import math
import operator


# Relaciona cada símbolo con la operación matemática correspondiente.
OPERACIONES = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
}


def leer_numero(mensaje=""):
    # Repite la solicitud cuando la entrada no es un número válido.
    while True:
        try:
            numero = float(input(mensaje))
            if math.isfinite(numero):
                return numero
        except ValueError:
            pass
        print("Ingrese un número válido y finito. Use punto para los decimales.")


def mostrar_resultado(resultado):
    # Evita mostrar .0 cuando el resultado es un número entero.
    if isinstance(resultado, float) and resultado.is_integer():
        resultado = int(resultado)
    print(resultado)


def evaluar_expresion(expresion):
    # Analiza la expresión sin ejecutar código mediante eval().
    simbolos = {
        ast.Add: "+", ast.Sub: "-", ast.Mult: "*",
        ast.Div: "/", ast.Mod: "%",
    }

    def resolver(nodo):
        # Solo permite números, los cinco operadores y signos positivos o negativos.
        if isinstance(nodo, ast.Constant) and type(nodo.value) in (int, float):
            return nodo.value
        if isinstance(nodo, ast.BinOp) and type(nodo.op) in simbolos:
            operacion = OPERACIONES[simbolos[type(nodo.op)]]
            return operacion(resolver(nodo.left), resolver(nodo.right))
        if isinstance(nodo, ast.UnaryOp):
            if isinstance(nodo.op, ast.USub):
                return -resolver(nodo.operand)
            if isinstance(nodo.op, ast.UAdd):
                return resolver(nodo.operand)
        raise ValueError("Expresión no permitida.")

    # La estructura de Python conserva la prioridad matemática y los paréntesis.
    if len(expresion) > 200:
        raise ValueError("La expresión debe tener como máximo 200 caracteres.")
    arbol = ast.parse(expresion.strip(), mode="eval")
    resultado = resolver(arbol.body)
    if isinstance(resultado, float) and not math.isfinite(resultado):
        raise ValueError("El resultado no es finito.")
    return resultado


def menu():
    while True:
        print("\nOperaciones adicionales")
        print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Módulo")
        print("6. Sumar tres números\n7. Operaciones combinadas\n0. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "0":
            return
        if opcion not in ("1", "2", "3", "4", "5", "6", "7"):
            print("Opción inválida.")
            continue

        try:
            if opcion == "7":
                resultado = evaluar_expresion(input("Expresión: "))
            else:
                primero = leer_numero("Primer número: ")
                segundo = leer_numero("Segundo número: ")
                if opcion == "6":
                    tercero = leer_numero("Tercer número: ")
                    resultado = primero + segundo + tercero
                else:
                    simbolo = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "%"}[opcion]
                    resultado = OPERACIONES[simbolo](primero, segundo)
                if not math.isfinite(resultado):
                    raise ValueError("El resultado no es finito.")
            mostrar_resultado(resultado)
        except ZeroDivisionError:
            print("No se puede dividir ni calcular el módulo entre cero.")
        except (ValueError, SyntaxError, OverflowError, RecursionError):
            print("Entrada inválida o resultado fuera de rango.")


def main():
    try:
        # Primero cumple la tarea obligatoria, antes de mostrar cualquier menú.
        primero = leer_numero()
        segundo = leer_numero()
        resultado = primero + segundo
        if not math.isfinite(resultado):
            print("El resultado está fuera de rango.")
            return
        mostrar_resultado(resultado)

        # El evaluador solo entrega dos números; al terminar la entrada, se sale.
        menu()
    except EOFError:
        return


# Permite importar las funciones sin iniciar la interacción con el usuario.
if __name__ == "__main__":
    main()
