

# 📥 Cómo descargar

Tienes dos formas de obtener el código:

## ✅ Opción 1: Clonar el repositorio (recomendado)

Necesitas tener Git instalado en tu PC. Si ya lo tienes, abre la terminal o consola y ejecuta:

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
```

🔄 **IMPORTANTE:** Si instalaste Git mientras tenías Visual Studio Code abierto, ciérralo y vuelve a abrirlo para que detecte Git correctamente.

## 📝 Opción 2: Copiar y pegar el código

Si no sabes clonar un repositorio o tienes problemas, también puedes copiar el código manualmente y pegarlo en un archivo `.py`.

## 💡 Consejo

Intenta clonar el repositorio tú mismo

## 🚀 Mejoras implementadas

Esta versión mejora el ejemplo básico de una calculadora en varios aspectos:

### ✅ 1. Código más limpio y mantenible
* Se evita usar múltiples `if` y `elif` para las operaciones.
* En su lugar, se usa un **diccionario** que asocia cada opción del menú con una función. Esto facilita añadir o quitar operaciones de forma rápida.

### ✅ 2. Uso de funciones bien definidas
* Cada operación (`sumar`, `restar`, etc.) está separada en su propia **función con nombre descriptivo**.
* Esto hace que el código sea más **modular y reutilizable**.

### ✅ 3. Tipado en parámetros y retorno
* Las funciones usan **anotaciones de tipo** (`a: float -> float`) para indicar qué tipo de datos se espera.
* Esto **documenta el código automáticamente** y ayuda a evitar errores.

### ✅ 4. Control de errores
* La división ahora comprueba si el divisor es cero y devuelve un mensaje de error personalizado.

### ✅ 5. Presentación del menú
* El menú se genera automáticamente recorriendo el diccionario de operaciones, lo que evita repetir texto y hace más fácil mantenerlo actualizado.
