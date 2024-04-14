import builtwith
import whois
import urllib3
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import re

# Creació de un DataFrame per guardar els productes
# df_productos_dia = pd.DataFrame(columns=['Nombre', 'Marca', 'Precio', 'Supermercado', 'URL'])

# Url de Dia
# url_superMerca = 'https://www.supermercadosmas.com/'
# url_superMerca_map = 'https://www.dia.es/sitemap.xml'

# Funció per obtenir les dades d'un producte de Dia
def datosProducto(urlProducto,df_productos):
    # Desactivar advertencias de SSL
    urllib3.disable_warnings()
    # Realitzar la petició GET
    http = urllib3.PoolManager()
    response = http.request('GET', urlProducto)
    soup = BeautifulSoup(response.data, 'html.parser')

    #Try per si no troba el producte a la pàgina
    try:
        #Troba l'element que conté el preu del producte
        precio_elemento = soup.find('p', class_='buy-box__active-price')
        if precio_elemento:
            # Extreu el preu del text i el formateja
            precio = precio_elemento.text.strip().replace('\xa0€', ' €').replace(',', '.')
        else:
            precio = 'Precio no disponible'

        # Troba l'element que conté el nom del producte
        nombre_elemento = soup.find('h1', class_='product-title')
        if nombre_elemento:
            nombre = nombre_elemento.text.strip()
        else:
            nombre = 'Nombre no disponible'

        # Troba l'element que conté la marca del producte
        marca_elemento = soup.find('p', class_='manufacturer-info__name')
        if marca_elemento:
            marca = marca_elemento.text.strip()
        else:
            marca = 'Marca no disponible'

        # Afegir les dades al DataFrame
        df_productos.loc[len(df_productos)] = [nombre, marca, precio, 'Supermercados Mas', urlProducto]
        print('Producto:', nombre, 'Marca:', marca, 'Precio:', precio)
    except AttributeError:
        print('Error en producto:', urlProducto)

# Funció per obtenir les dades dels productes de Dia
def crawl_sitemap_Dia(url,df_productos):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    
    if response.status == 200:
        soup = BeautifulSoup(response.data, 'html.parser')
        
        # Obtenir totes les URL del sitemap
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