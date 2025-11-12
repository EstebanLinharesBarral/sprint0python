cuenta = {
    "nombre": "Esteban",
    "saldo": 1500.00
}

resp = "0"

while resp != "4":
    print("\n1. Consultar saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    val = False
    while not val:
        resp = input("\nEscoja una opción:\n")
        if resp == "1" or resp == "2" or resp == "3" or resp == "4":
            val = True
            
    if resp == "1":
        print(f"Su saldo es de: {cuenta["saldo"]}")
    
    if resp == "2":
        val = False
        while not val:
            ingreso = input("Añada la cantidad a ingresar\n")
            try:
                ingreso = float(ingreso)
                val = True
            except:
                print("La cantidad añadida no es una cantidad válida")
        cuenta["saldo"] = cuenta["saldo"] + ingreso
        print(f"Tu nuevo saldo es: {cuenta['saldo']}")

    if resp == "3":
        val = False
        retiro = cuenta["saldo"]+1
        while not val or retiro > cuenta["saldo"]:
            val = False
            retiro = input("Añada la cantidad a retirar\n")
            try:
                retiro = float(retiro)
                val = True
            except:
                print("La cantidad añadida no es una cantidad válida")

            if val:
                if retiro <= cuenta["saldo"]:
                    cuenta["saldo"] = cuenta["saldo"] - retiro
                else:
                    print("No hay suficiente saldo para retirar esa cantidad")
                
        if val and retiro <= cuenta["saldo"]:
            print(f"Tu nuevo saldo es: {cuenta['saldo']}")

    if resp == "4":
        print("FIN DEL PROGRAMA")