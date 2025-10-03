from libro import Libro, LibroDigital
from biblioteca import Biblioteca
from datetime import datetime
from fecha_actual_error import Limite_Fecha_Error

#metodo menu principal gestor_biblioteca
def menu():
    biblioteca=Biblioteca ()
    biblioteca.cargar_desde_archivo()
    while True:
        try:
            print("1. Agregar libro\n2. Eliminar libro\n3. Ver todos los libros\n4. Buscar libro\n5. Marcar libro como prestado\n6. Devolver libro\n7. Salir")
            opcion = input("Elige una opción: ")
            if opcion == "1":
                formato = input("¿Es un libro digital? (s/n): ")
                titulo = input("Ingrese el título del libro: ").strip().title()
                autor = input("Ingrese el autor del libro: ").strip().title()
                anio_publicacion = int(input("Ingrese el año de publicación del libro: "))
                estado = "Disponible"
                if anio_publicacion > datetime.now().year:
                    raise Limite_Fecha_Error("El año de publicación no puede ser en el futuro.")
                else:
                    print("Año de publicación válido.")
                if formato.lower() == "s":
                    biblioteca.agregar_libro(LibroDigital(titulo, autor, anio_publicacion))
                else:
                    biblioteca.agregar_libro(Libro(titulo, autor, anio_publicacion))  
            elif opcion == "2":
                biblioteca.listar_libros()
                titulo = input("Ingrese el título del libro a eliminar: ")
                biblioteca.eliminar_libro(titulo)
            elif opcion == "3":
                biblioteca.listar_libros()
            elif opcion == "4":
                titulo = input("Ingrese el título del libro a buscar: ")
                biblioteca.buscar_libro(titulo)
            elif opcion == "5":
                titulo = input("Ingrese el título del libro que se va a solicitar: ")
                biblioteca.marcar_prestado(titulo)
            elif opcion == "6":
                titulo = input("Ingrese el título del libro a devolver: ")
                biblioteca.devolver_libro(titulo)
            elif opcion == "7":
                biblioteca.guardar_en_archivo()
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida.")
        except ValueError as e:
            print(f"Error: {e}")
        except Limite_Fecha_Error as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    pass
menu()


