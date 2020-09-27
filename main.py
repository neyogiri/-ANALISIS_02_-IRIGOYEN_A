import pandas as pd  
import pylab as pl  
import csv
import numpy as np  

#Opción 3 del proyecto:
#Valor total de importaciones y exportaciones. Si Synergy Logistics
#quisiera enfocarse en los países que le generan el 80% del valor de las
#exportaciones e importaciones ¿en qué grupo de países debería enfocar sus
#esfuerzos?
#buscar en el archivo csv los 10 lugares más requeridos 
datos=pd.read_csv('synergy_logistics_database.csv')
#Se guarda en una varibale el conteo de los datos en la columna correspondiente a los países
conteo_datos= datos.groupby('destination')['direction'].count()
#Se ordena de mayor a menor
lista=(conteo_datos.sort_values(ascending=False))
#Nueva variable con los primeros 10 países que más aportan a la compañía
lista_exp=(lista[0:10])
#Se imprime en pantalla
print('Estos son los paises que más valor generan a la compañía:',lista_exp)


#opción 2 del proyecto:
#Medio de transporte utilizado. ¿Cuáles son los 3 medios de transporte
#más importantes para Synergy logistics considerando el valor de las
#importaciones y exportaciones? ¿Cuál es medio de transporte que podrían
#reducir? 

#Crea variable para guardar los datos de la columna transporte
conteo_transporte= datos.groupby('transport_mode')['direction'].count()
#Se ordena de mayor a menor
lista_transporte=(conteo_transporte.sort_values(ascending=False))
#Se imprimen los primeros 3
lista_2=(lista_transporte[0:3])
#Se muestra en pantalla el resultado
print('Los 3 primeros medios de trasportes más utilizados son:',lista_2)
