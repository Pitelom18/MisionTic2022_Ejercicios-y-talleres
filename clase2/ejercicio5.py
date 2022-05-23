""" Estás interesado en comprarte un nuevo PC y en la tienda de tu barrio cuesta 660€ con todos los accesorios incluídos. Sin embargo, el vendedor te descuenta el 10% por pronto pago ¿Cuánto tienes que pagar en total por el ordenador con todos los accesorios? """

#datos de entrada

precio_inicialEuros = 660
descuento_aplicado = 10/100*precio_inicialEuros

#procesamiento de datos

precio_final = round(precio_inicialEuros - descuento_aplicado,2)

#salida de datos

print("El precio final del ordenador es: ", (precio_final), "Euros")