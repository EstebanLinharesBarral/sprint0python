from tarea import Tarea

def main():
    lista_tareas = []
    resp = ""

    def crear_tarea():
        titulo = input("\nPonle nombre a la tarea: ")
        definicion = input("\nDefine la tarea: ")
        lista_tareas.append(Tarea(titulo, definicion))
    
    def mostrar_todas():
        for t in lista_tareas:
            print(t.mostrar_info())

    def marcar_completada():
        titulo = input("\n¿Que tarea has completado?\n")
        comp = False

        for t in lista_tareas:
            if titulo == t.get_titulo():
                comp = True
                if(t.get_completada()):
                    print("La tarea ya está completada")
                else:
                    t.marcar_completada()
            
            if not comp:
                print("La tarea no está en la lista")

    def editar_tarea():
        titulo = input("\n¿Que tarea quieres editar?\n")
        comp = False

        for t in lista_tareas:
            if titulo == t.get_titulo():
                comp = True

                n_titulo = input("\nNuevo título: ")
                n_definicion = input("\nNueva definición: ")

                t.editar(n_titulo, n_definicion)
            
            if not comp:
                print("La tarea no está en la lista")

    def eliminar_tarea():
        titulo = input("\n¿Que tarea quieres eliminar?\n")
        comp = False

        for t in lista_tareas:
            if titulo == t.get_titulo():
                comp = True

                lista_tareas.remove(t)
            
            if not comp:
                print("La tarea no está en la lista")

        
    while resp != "6":
        print("\n1. Crear tarea")
        print("2. Mostrar todas")
        print("3. Marcar como completada")
        print("4. Editar tarea")
        print("5. Eliminar tarea")
        print("6. Salir")

        val = False
        while not val:
            resp = input("\nEscoja una opción:\n")
            if resp == "1" or resp == "2" or resp == "3" or resp == "4" or resp == "5" or resp == "6":
                val = True

        if resp == "1":
            crear_tarea()
        
        if resp == "2":
            mostrar_todas()

        if resp == "3":
            marcar_completada()
        
        if resp == "4":
            editar_tarea()

        if resp == "5":
            eliminar_tarea()

        if resp == "6":
            print("FIN DEL PROGRAMA")

main()