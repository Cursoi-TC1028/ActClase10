![Tec de Monterrey](../../images/logotecmty.png)
# Calculadora

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Escribe una función que reciba como parámetro 2 números enteros y una clave que es una letra.

La clave representa una operación aritmética de acuerdo con la siguiente tabla:

Clave Significado

s        Suma
r        Resta
m       Multiplicación
d        División

La función debe aplicar la operación aritmética a los 2 valores recibidos y regresar como valor de retorno el resultado de dicha operación.

Nota que dentro de la función no mostrarás nada, solo regresarás el valor usando return.

 

Escribe ahora una función main en la que pidas al usuario teclear 2 valores numéricos y una clave (s, r, m, d), después llama la función con los parámetros correspondientes y luego muestra el resultado de la operación que regresó la función.

**Entrada**
<br>introducir valor 1: 5
<br>introducir valor 2: 6
<br>introducir clave  (s, r, m, d): s

**Salida**
<br>resultado: 11

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
