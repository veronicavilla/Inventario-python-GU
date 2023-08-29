productoTerminadoUno={
    'referencia':5087,
    'marca':"Americanino",
    'descripcion':"chompa de acampar",
    'color':"naranjado",
    'costoDeFabricacion':100000,
    'disponibleEnBodega': True,
    'costoDeVenta':850000,
    'puntosDeVenta':['cc mayorca','terminal norte','puerta del norte','centro de la moda']
}

productoTerminadoDos={
    'referencia':5088,
    'marca':"Americanino",
    'descripcion':"camiseta polo",
    'color':"azul oscuro",
    'costoDeFabricacion':30000,
    'disponibleEnBodega': True,
    'costoDeVenta':150000,
    'puntosDeVenta':['cc mayorca','terminal norte','puerta del norte','centro de la moda']
}

#creando una lista de diccionarios
productos=[productoTerminadoUno, productoTerminadoDos]

#Recorriendo una lista con ciclo for
'''for i in range(10):
      print("estoy repitiendo")'''

'''for contador in range(1, 10, 2):
    print(contador)'''

for producto in productos: #for each
    for puntoDeVenta in producto["PuntosDeVenta"]:
        print(puntoDeVenta)