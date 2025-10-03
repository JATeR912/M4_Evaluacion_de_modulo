# Biblioteca Digital - Guía de Uso

Este programa permite gestionar una biblioteca de libros físicos y digitales. Puedes agregar, eliminar, buscar libros, marcar libros como prestados o devueltos, y listar todos los libros disponibles.

---

## Requisitos

- Python 3.x instalado en tu computadora.
- Archivos del proyecto:
  - `main.py`
  - `libro.py`
  - `biblioteca.py`
  - `fecha_actual_error.py`
  - `biblioteca.txt` (archivo con datos iniciales de libros)
  - `diagrama.drawio.png` (diagrama de clases que representa la estructura del sistema)

---

## ¿Cómo ejecutar el programa?

1. **Abre la terminal o consola** de tu sistema operativo.

2. **Navega a la carpeta donde están los archivos**. Por ejemplo:

```bash
cd ruta/al/directorio/del/proyecto
````

3. **Ejecuta el programa principal** con el siguiente comando:

```bash
python main.py
```

---

## Uso del programa

Al iniciar, verás un menú con opciones numeradas:

```
1. Agregar libro
2. Eliminar título
3. Listar libros disponibles
4. Buscar libro
5. Marcar libro como prestado
6. Marcar libro como devuelto
7. Salir
```

Solo escribe el número de la opción que deseas y presiona Enter.

---

### Agregar libro

* Te preguntará si es un libro digital (`s` para sí, `n` para no).
* Luego, ingresa título, autor y año de publicación.
* Si el año de publicación es mayor al actual, te avisará que no es válido.

---

### Otros comandos

* Para eliminar, buscar, prestar o devolver un libro, deberás ingresar el título del libro cuando se te solicite.
* Al listar, se mostrarán todos los libros existentes en la biblioteca.

---

## Notas

* Los cambios se guardan automáticamente en el archivo `biblioteca.txt` al salir del programa.
* Los títulos de libros no distinguen mayúsculas/minúsculas ni espacios al buscar o eliminar.

