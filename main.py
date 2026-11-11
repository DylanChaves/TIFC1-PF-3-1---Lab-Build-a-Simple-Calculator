# LAB 1 - PARTE 1: sumar dos numeros.
# No se muestran preguntas ni menus para respetar la evaluacion automatica.


def sumar_dos_numeros():
    # input() recibe texto; float() permite operar con enteros y decimales.
    primer_numero = float(input())
    segundo_numero = float(input())
    
    # El operador + suma los dos valores ingresados.
    resultado = primer_numero + segundo_numero

    # Un resultado entero se imprime sin .0 si es decimal se imprime con decimales.
    if resultado.is_integer():
        print(int(resultado))
    else:
        print(resultado)


# Este bloque se ejecuta al abrir main.py, pero no al importarlo desde otro archivo.
if __name__ == "__main__":
    sumar_dos_numeros()

    