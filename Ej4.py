lista_compra = []
resp = "0"

while resp != "5":
    print("\n1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Ver lista")
    print("4. Vaciar lista")
    print("5. Salir")

    val = False
    while not val:
        resp = input("\nEscoja una opción:\n")
        if resp == "1" or resp == "2" or resp == "3" or resp == "4" or resp == "5":
            val = True

    producto = ""        
    if resp == "1":
        producto = input("Introduzca un prodcuto para añadirlo a la lista.\n")
        lista_compra.append(producto.lower())
    
    if resp == "2":
        producto = input("Introduzca el producto de su lista que desea eliminar.\n")
        if producto.lower() in lista_compra:
            lista_compra.remove(producto.lower())
        else:
            print("El producto no existe en la lista")

    if resp == "3":
        lista_compra.sort()
        for p in lista_compra:
            print(p)

    if resp == "4":
        lista_compra.clear()

    if resp == "5":
        print("FIN DEL PROGRAMA")