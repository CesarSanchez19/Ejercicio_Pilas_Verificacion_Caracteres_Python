# Verificación de Expresiones Balanceadas usando Pilas en Python

Este programa en Python verifica si una expresión que contiene los símbolos `()`, `[]` y `{}` está correctamente balanceada. En caso de error, muestra la posición exacta del problema y el símbolo esperado.

## Características
- Verifica si una expresión está correctamente balanceada.
- Muestra el error exacto con la posición y el símbolo esperado.
- Indica soluciones posibles para corregir la expresión.
- Permite establecer un límite máximo de caracteres para la entrada.

## Cómo funciona
1. Solicita al usuario el límite máximo de caracteres permitidos.
2. Solicita al usuario una expresión a evaluar.
3. Comprueba si la expresión cumple con las reglas de balanceo de paréntesis, corchetes y llaves.
4. Muestra un mensaje indicando si la expresión es correcta o incorrecta.

## Uso
Ejecutar el script y seguir las instrucciones en pantalla:
```bash
python script.py
```

### Ejemplo de entrada y salida
#### Entrada válida
```
Ingrese el límite máximo de caracteres: 50
Ingresa la expresión a verificar: {[(2+3)*5]}
La expresión es correcta.
```

#### Entrada inválida
```
Ingrese el límite máximo de caracteres: 50
Ingresa la expresión a verificar: {[(2+3]*5)}
Error en la posición 6: se encontró ']' pero se esperaba ')' para cerrar '(' abierto en la posición 3.
Posible solución: Verifica que los símbolos de apertura y cierre coincidan correctamente.
La expresión es incorrecta.
```

## Requisitos
- Python 3.x

## Autor
- **César David Sánchez Trejo**

Este proyecto es un ejercicio para aprender sobre pilas y validación de expresiones con estructuras de control en Python.
