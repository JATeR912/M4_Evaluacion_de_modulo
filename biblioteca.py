from libro import Libro, LibroDigital
from datetime import datetime
import os
class Biblioteca:
    def __init__(self,archivo="biblioteca.txt"):
        self.archivo = archivo
        self.libros = []

    def agregar_libro(self,libro):
        self.libros.append(libro)
        print(f"Libro '{libro.get_titulo()}' agregado correctamente")

    def eliminar_libro(self,titulo):
        for libro in self.libros:
            if libro.get_titulo().strip().lower() == titulo.strip().lower():
                self.libros.remove(libro)
                print(f"Libro '{libro.get_titulo()}' eliminado correctamente")
                return
        raise ValueError(f"Libro '{titulo}' no encontrado")

    def listar_libros(self): #Listar todos los libros disponibles
        if not self.libros:
            print("No hay libros en la biblioteca.")
        for libro in self.libros:
            print(libro)

    def buscar_libro(self,titulo): #Buscar un libro por su título
        for libro in self.libros:
            if libro.get_titulo().strip().lower() == titulo.strip().lower():
                print(libro)
                return libro
        raise ValueError(f"Libro '{titulo}' no encontrado")

    def marcar_prestado(self,titulo): #Marcar un libro como prestado
        libro = self.buscar_libro(titulo)
        if libro.get_estado() == "Prestado":
            raise ValueError(f"Libro '{libro.get_titulo()}' ya está prestado")
        libro.set_estado("Prestado")
        print(f"Libro '{libro.get_titulo()}' marcado como prestado")

    def devolver_libro(self,titulo): #Marcar un libro como devuelto
        libro = self.buscar_libro(titulo)
        if libro.get_estado() == "Disponible":
            raise ValueError(f"Libro '{libro.get_titulo()}' ya está disponible")
        libro.set_estado("Disponible")
        print(f"Libro '{libro.get_titulo()}' ha sido devuelto")


    #Metodo comentado para posible futura implementacion sin uso en el menu
    #def filtrar_por_longitud(self): #Filtrar libros por longitud 
        #if not os.path.exists(self.archivo):
            #print(f"Archivo '{self.archivo}' no encontrado.")
            #return

        #with open(self.archivo, 'r', encoding='utf-8') as archivo:
            #for linea in archivo:
                #datos = [dato.strip() for dato in linea.strip().split(',')]

                #if len(datos) == 5:
                    #titulo, autor, anio, estado, formato = datos
                    #libro = LibroDigital(titulo, autor, anio, estado, formato)
                    #print(f"Libro '{titulo}' es un libro digital")
                #elif len(datos) == 4:
                    #titulo, autor, anio, estado = datos
                    #libro = Libro(titulo, autor, anio, estado)
                    #print(f"Libro '{titulo}' es un libro físico")
                #else:
                    #print(f"Error de datos: {linea}")
                    #continue

    def cargar_desde_archivo(self):#Cargar libros desde un archivo de texto
        if not os.path.exists(self.archivo):
            return
        try:
            self.libros.clear() 
            with open(self.archivo, "r", encoding="utf-8") as file:
                for linea in file:
                    datos = [dato.strip() for dato in linea.strip().split(",")]
                    if len(datos) == 5: # Libro digital
                        titulo, autor, anio_publicacion, estado, formato = datos
                        libro = LibroDigital(titulo, autor, int(anio_publicacion), estado, formato)
                    elif len(datos) == 4: # Libro físico
                        titulo, autor, anio_publicacion, estado = datos
                        libro = Libro(titulo, autor, int(anio_publicacion), estado)
                    else:
                        print(f"Línea ignorada por formato incorrecto: {linea}")
                        continue
                    self.libros.append(libro)
            print(f"\nSe cargaron {len(self.libros)} libros desde '{self.archivo}'.")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

    def guardar_en_archivo(self):#Guardar libros en un archivo de texto
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for libro in self.libros:
                    if isinstance(libro, LibroDigital):
                        f.write(f"{libro.get_titulo()}, {libro.get_autor()}, {libro.get_anio_publicacion()}, {libro.get_estado()}, {libro.get_formato()}\n")
                    else:
                        f.write(f"{libro.get_titulo()}, {libro.get_autor()}, {libro.get_anio_publicacion()}, {libro.get_estado()}\n")
            print(f"Datos guardados correctamente en '{self.archivo}'.")
        except Exception as e:
            print(f"Error al guardar en el archivo: {e}")