def balanced(expression: str) -> bool:
    """
    Verifica si la expresión está balanceada para los símbolos (), [], {}.
    Si hay un error, muestra la posición exacta y el símbolo esperado.
    Retorna True si está balanceada, False en caso contrario.
    """

    # Diccionario que relaciona cada símbolo de cierre con su apertura correspondiente
    closing_to_opening = {')': '(', ']': '[', '}': '{'}

    # Diccionario que indica qué símbolo de cierre le corresponde a cada apertura
    opening_to_closing = {'(': ')', '[': ']', '{': '}'}

    # Lista que usaremos como una pila para almacenar los símbolos de apertura
    stack = []

    # Recorremos cada carácter de la expresión con su posición
    for position, character in enumerate(expression):
        
        # Si el carácter es un símbolo de apertura, lo guardamos en la pila junto con su posición
        if character in "([{":
            stack.append((character, position))
        
        # Si el carácter es un símbolo de cierre, verificamos si está correctamente emparejado
        elif character in ")]}":
            
            # Si la pila está vacía, significa que encontramos un cierre sin apertura previa
            if not stack:
                print(f"Error en la posición {position}: se encontró '{character}' pero no hay un símbolo de apertura que cerrar.")
                print("Posible solución: Revisa si falta un símbolo de apertura antes de este cierre.")
                return False

            # Sacamos el último símbolo de apertura de la pila para verificar si coincide con el cierre
            open_char, open_position = stack.pop()

            # Si el símbolo de apertura no coincide con el cierre, hay un error
            if closing_to_opening[character] != open_char:
                expected = opening_to_closing[open_char]  # Símbolo que debería haber cerrado
                print(f"Error en la posición {position}: se encontró '{character}', "
                      f"pero se esperaba '{expected}' para cerrar '{open_char}' "
                      f"abierto en la posición {open_position}.")
                print("Posible solución: Verifica que los símbolos de apertura y cierre coincidan correctamente.")
                return False

        # Si el carácter no es un símbolo de apertura ni de cierre, lo ignoramos
        else:
            continue

    # Al final, si la pila no está vacía, significa que faltan cierres para algunos símbolos
    if stack:
        while stack:
            open_char, open_position = stack.pop()
            print(f"Error: El símbolo de apertura '{open_char}' en la posición {open_position} "
                  f"no tiene su cierre correspondiente.")
            print("Posible solución: Agrega el cierre correspondiente al final de la expresión.")
        return False

    # Si no hubo errores y la pila está vacía, la expresión está correctamente balanceada
    return True


def main():
    try:
        limit = int(input("Ingrese el límite máximo de caracteres: "))  # Pedimos el límite al usuario
        expression = input("Ingresa la expresión a verificar: ")  # Pedimos la expresión

        # Verificar si la expresión excede el límite de caracteres
        if len(expression) > limit:
            print(f"Error: La expresión ingresada excede el límite de {limit} caracteres.")
            print("Posible solución: Intenta reducir la cantidad de caracteres en tu expresión.")
            print("La expresión es incorrecta.")  # Mensaje final
        else:
            # Llamamos a la función para verificar si la expresión es válida
            if balanced(expression):
                print("La expresión es correcta.")  # Mensaje de éxito si está balanceada
            else:
                print("La expresión es incorrecta.")  # Mensaje de error si no está balanceada

    except ValueError:
        print("Error: Ingrese un número válido para el límite de caracteres.")


# Si el script se ejecuta directamente, llamamos a la función main()
if __name__ == "__main__":
    main()
