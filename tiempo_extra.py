# PARTE 2: actividades a partir de "Extra time".
import ast
import operator

from main import sumar_dos_numeros


def leer_numero(mensaje):
    
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada invalida. Escriba un numero, por ejemplo 8 o 2.5.")


def mostrar_resultado(resultado):
    
    if isinstance(resultado, float) and resultado.is_integer():
        resultado = int(resultado)
    print("Resultado:", resultado)


def evaluar_expresion(expresion):
    
    operaciones = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Mod: operator.mod,
    }

    
    if len(expresion) > 200:
        raise ValueError("Use una expresion de hasta 200 caracteres.")

    def resolver(nodo):
        # Si el nodo es un numero, lo devolvemos.
        if isinstance(nodo, ast.Constant) and type(nodo.value) in (int, float):
            return nodo.value

        
        if isinstance(nodo, ast.BinOp) and type(nodo.op) in operaciones:
            izquierda = resolver(nodo.left)
            derecha = resolver(nodo.right)
            return operaciones[type(nodo.op)](izquierda, derecha)

        
        if isinstance(nodo, ast.UnaryOp) and isinstance(nodo.op, (ast.UAdd, ast.USub)):
            valor = resolver(nodo.operand)
            return -valor if isinstance(nodo.op, ast.USub) else valor

   
        raise ValueError("Use solo numeros, parentesis y los operadores + - * / %.")

   

    arbol = ast.parse(expresion, mode="eval")
    return resolver(arbol.body)


def menu_operaciones():
  
    while True:
        print("\nTIEMPO EXTRA")
        print("1. Sumar dos numeros")
        print("2. Restar el segundo numero al primero")
        print("3. Multiplicar dos numeros")
        print("4. Dividir el primero entre el segundo")
        print("5. Calcular el modulo o residuo")
        print("6. Sumar tres numeros")
        print("7. Combinar operaciones con tres o mas numeros")
        print("0. Salir")
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "0":
            print("Programa finalizado.")
            break

        if opcion not in ("1", "2", "3", "4", "5", "6", "7"):
            print("Opcion invalida. Seleccione un numero del 0 al 7.")
            continue

        try:
            if opcion == "7":
                expresion = input("Escriba una expresion, por ejemplo 2 + 4 - 3: ")
                resultado = evaluar_expresion(expresion)
            else:
                primero = leer_numero("Primer numero: ")
                segundo = leer_numero("Segundo numero: ")

                if opcion == "1":
                    resultado = primero + segundo
                elif opcion == "2":
                    resultado = primero - segundo
                elif opcion == "3":
                    resultado = primero * segundo
                elif opcion == "4":
                    resultado = primero / segundo
                elif opcion == "5":
                    resultado = primero % segundo
                else:
                    tercero = leer_numero("Tercer numero: ")
                    resultado = primero + segundo + tercero

            mostrar_resultado(resultado)
        except ZeroDivisionError:
          
            print("Error: no se puede dividir ni calcular modulo entre cero.")
        except (ValueError, SyntaxError, RecursionError, OverflowError) as error:
            print("Expresion invalida:", error)


if __name__ == "__main__":
    try:
      
        print("PARTE 1: escriba dos numeros, uno por linea.")
        sumar_dos_numeros()
        menu_operaciones()
    except ValueError:
        print("Entrada invalida en la suma inicial. Reinicie e ingrese numeros.")
    except EOFError:
        # Si termina la entrada, cerramos sin mostrar un error tecnico.
        pass
