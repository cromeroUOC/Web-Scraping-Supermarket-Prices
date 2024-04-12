import builtwith
import whois
import urllib3
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import re

# # Crear un DataFrame para guardar los productos, variable global para poder acceder a ella desde las funciones
# df_productos_dia = pd.DataFrame(columns=['Nombre', 'Marca', 'Precio', 'Supermercado', 'URL'])

# url_superMerca = 'https://www.supermercadosmas.com/'
# url_superMerca_map = 'https://www.dia.es/sitemap.xml'

# Función para obtener los datos de un producto

def datosProducto(urlProducto,df_productos):
    # Desactiva los warnings de certificados SSL
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    response = http.request('GET', urlProducto)
    soup = BeautifulSoup(response.data, 'html.parser')

    #Try para evitar errores en la ejecución, algunas url no tienen ya productos
    try:
        #Encuentra el elemento que contiene el precio activo
        precio_elemento = soup.find('p', class_='buy-box__active-price')
        if precio_elemento:
            # Extrae el texto y limpia el precio, quitando espacios y caracteres no deseados
            precio = precio_elemento.text.strip().replace('\xa0€', ' €').replace(',', '.')
        else:
            precio = 'Precio no disponible'

        # Encuentra el elemento que contiene el nombre del producto usando el nuevo selector
        nombre_elemento = soup.find('h1', class_='product-title')
        if nombre_elemento:
            nombre = nombre_elemento.text.strip()
        else:
            nombre = 'Nombre no disponible'

        # Encuentra el elemento que contiene la marca del producto
        marca_elemento = soup.find('p', class_='manufacturer-info__name')
        if marca_elemento:
            marca = marca_elemento.text.strip()
        else:
            marca = 'Marca no disponible'

        # # Añadir a la lista de productos
        df_productos.loc[len(df_productos)] = [nombre, marca, precio, 'Supermercados Mas', urlProducto]
        print('Producto:', nombre, 'Marca:', marca, 'Precio:', precio)
    except AttributeError:
        print('Error en producto:', urlProducto)

def crawl_sitemap_Dia(url,df_productos):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    
    if response.status == 200:
        soup = BeautifulSoup(response.data, 'html.parser')
        
        # Encontrar todos los tags <url>
        urls = soup.find_all('url')
        
        for url in urls:
            loc = url.find('loc').text 
            datosProducto(loc,df_productos) 
    else:
        print("Failed to fetch sitemap:", response.status)


# if __name__ == '__main__':
#     crawl_sitemap(url_superMerca_map,df_productos_dia)

#     # Guardar los datos en un archivo CSV
#     df_productos.to_csv('productos_supermercadosmas.csv', index=False)