from clases import Reporte
reporte = Reporte()
while True:
    print("\n\nMenu")
    print("Teclee una opcion")
    print("1) Inventario")
    print("2) Compras")
    print("3) Reportes y Graficas")
    print("4) Salir")
    opc = 0
    try:
        
        opc = int(input("- "))
    except Exception:
         opc = 0
    if opc is 1:
        print("\n\n\nInserte un texto a buscar")
        print("NL para nuevo libro")
        print("NP para nueva pelicula")
        print("NM para nuevo disco")
        clave = str(input("Clave entera o codigo: "))
        if clave == "NL":
            reporte.altas("NL")
        elif clave == "NP":
            reporte.altas("NP")
        elif clave == "NM":
            reporte.altas("NM")
        else:
            try:

                clave = int(clave)
                print("\n\n")
                reporte.imprimir(clave)
            except Exception:
                print("Introduzca un valor adecuado")
    elif opc is 2:
        total = []
        tipos = []
        while True:
            print("\n\n\nInserte la clave del producto a comprar")
            print("-1 para terminar de comprar")
            clave = ""
            try:
                clave = int(input("clave: "))
                tem = reporte.ventas(clave)
                temp = []
                if len(tem) > 0:
                    total.append(tem[0])
                    tipos.append(tem[1])
                    print("Producto agregado al carrito")
                else:
                    print("Producto inexistente")
                if clave is -1:
                    break
            except Exception:
                print("Introduzca una clave valida")

        cadenas = []
        costo = 0.0
        counter = 0
        for producto in total:
            cadena = "Clave: " + str(producto[0])
            cadena += " | Titulo: " + str(producto[1])
            if tipos[counter] == 1:
                cadena += " | Autor: " + str(producto[7])
            elif tipos[counter] == 2:
                cadena += " | Productor: " + str(producto[7])
            elif tipos[counter] == 3:
                cadena += " | Interprete: " + str(producto[7])
            cadena += " | Precio: " + str(producto[3])
            cadenas.append(cadena)
            cadena = ""
            costo += float(producto[3])
            counter += 1
        for c in cadenas:
            print(c)
        print("\nCantidad de productos adquiridos: ", len(total))
        print("\nTotal: ", costo)
    elif opc is 3:
        print("\n\n\nInserte el reporte a revisar")
        print("1) para registros de Libros")
        print("2) para registros de Peliculas")
        print("3) para registros de Musica")
        print("4) para registros generales")
        opc = int(input(""))
        if opc == 1:
            reporte.rlibros()
        if opc == 2:
            reporte.rpeliculas()
        if opc == 3:
            reporte.rmusica()
        if opc == 4:
            reporte.rgeneral()

    elif opc is 4:
        break
    elif opc is 0:
        print("Teclee una opcion valida")
