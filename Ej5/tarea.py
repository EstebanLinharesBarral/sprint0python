class Tarea:
    def __init__(self, titulo, descripcion, completada = False):
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__completada = completada

    # Getters
    def get_titulo(self):
        return self.__titulo

    def get_descripcion(self):
        return self.__descripcion

    def get_completada(self):
        return self.__completada

    # Setters
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def set_completada(self, completada):
        self.__completada = completada

    def mostrar_info(self):
        comp = ""
        if self.__completada:
            comp = "Completada"
        else:
            comp = "Pendiente"

        cadena = f"{self.__titulo} - {comp}"
        return cadena

    def marcar_completada(self):
        self.__completada = True

    def editar(self, nuevo_titulo, nueva_descripcion):
        self.__titulo = nuevo_titulo
        self.__descripcion = nueva_descripcion