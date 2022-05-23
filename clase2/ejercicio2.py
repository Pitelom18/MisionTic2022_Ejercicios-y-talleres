 #Peso del producto empacado: 100g
# Precio del producto empacado: 5.95
#Peso en gramos de un kilo: 1000g

#datos de entrada
peso_g = 100
precio_euros_100g = 5.95
peso_K_en_g = 1000

#procesar los datos

producto_gramo = round(precio_euros_100g,2)/peso_g
precio_kilo = producto_gramo * peso_K_en_g

print(round(precio_kilo,2))

