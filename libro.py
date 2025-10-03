class Libro:
    def __init__(self, titulo, autor, anio_publicacion, estado="Disponible"):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.estado = estado

    def __str__(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nAño de publicación: {self.anio_publicacion}\nEstado: {self.estado}"
    
    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_autor(self):
        return self.autor

    def set_autor(self, autor):
        self.autor = autor

    def get_anio_publicacion(self):
        return self.anio_publicacion

    def set_anio_publicacion(self, anio_publicacion):
        self.anio_publicacion = anio_publicacion

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado

class LibroDigital(Libro):
    def __init__(self, titulo, autor, anio_publicacion, estado="Disponible", formato="Digital"):
        super().__init__(titulo, autor, anio_publicacion, estado)
        self.formato = formato

    def __str__(self):
        return super().__str__() + f"\nFormato: {self.formato}"

    def get_formato(self):
            return self.formato

    def set_formato(self, formato):
        self.formato = formato