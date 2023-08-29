#MENU DE OPCIONES
#1. Ingresar un producto en bodega
#2. GVerificar los productos en bodega
#3. Buscar un producto en la bodega
#4. Editar un producto en la bodega
#5. Retirar un producto en la bodega

#producto: nombre, codigo,  descripcion, foto, precio, cantidadEnBodega, fechaEntradaBodega

opcion=0
print("TIENDA EL GANGAZO")
print("♥♥♥♥♥♥♥♥♥♥♥♥")
print("1. Ingresar un producto en bodega")
print("2. Verificar los productos en bodega")
print("3. Buscar un producto en la bodega")
print("4. Editar un producto en la bodega")
print("5. Retirar un producto en la bodega")
print("6. SALIR")
print("♥♥♥♥♥♥♥♥♥♥♥♥")

productos = [] #la lista va por fuera porque solo necesito un campo vacio

while(opcion != 6):
    producto = {} #el diccionario es por dentro del ciclo, para que cada vez entre y se almacene un producto
    opcion=int(input("Digita la opcion deseada: "))
    if opcion==1:
        producto["nombre"] = input("Digita el nombre del producto: ")
        producto["codigo"] = int(input("Digita la referencia del producto: ")) 
        producto["descripcion"] = input("Digita la descripcion del producto: ")
        producto["foto"] = input("Digita la URL del producto: ")
        producto["precio"] = float(input("Digita el precio del producto: ")) 
        producto["cantidadEnBodega"] = int(input("Digita la cantidad existente en bodega: ")) 
        producto["fechaEntradaBodega"] = input("Digita la fecha de entrada del producto: ")
        productos.append(producto)
    elif opcion == 2:
        for productoSeleccionado in productos:
            print(f"codigo= {productoSeleccionado['codigo']}")
            print(f"nombre= {productoSeleccionado['nombre']}")
            print(f"descripcion= {productoSeleccionado['descripcion']}")
            print(f"foto= {productoSeleccionado['foto']}")
            print(f"precio= {productoSeleccionado['precio']}")
            print(f"cantidadEnBodega {productoSeleccionado['cantidadEnBodega']}")
            print(f"fechaEntradaBodega: {productoSeleccionado['fechaEntradaBodega']}\n")
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    elif opcion == 6:
        pass
    else:
        print("opción invalida vuelva a intentar")