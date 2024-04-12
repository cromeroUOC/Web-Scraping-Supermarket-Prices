import builtwith
import whois
import urllib3
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# url_consum = 'https://tienda.consum.es'
# url_consum_map = 'https://tienda.consum.es/sitemap_product_es.xml'

# Crear un DataFrame para guardar los productos, variable global para poder acceder a ella desde las funciones
# df_productos_Consum = pd.DataFrame(columns=['Nombre', 'Marca', 'Precio', 'Supermercado', 'URL'])

def datosProducto(driver, df_productos, urlProducto):

    try:
        
        # Navega a la página
        driver.get(urlProducto)

        # Espera hasta que el elemento que contiene el precio sea visible
        precio = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "infoproduct-content--price"))
        )

        nombre = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "u-title-3"))
        )
        
        marca = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "infoproduct-content--brand"))
        )
        
        # Agrega los datos a la variable global
        df_productos.loc[len(df_productos)] = [nombre.text, marca.text, precio.text, 'Consum', urlProducto]
        print(df_productos)
    except Exception as e:
        print("Error al obtener los datos del producto:", e)
        driver.quit()
        driver = webdriver.Chrome(ChromeDriverManager().install())


def crawl_sitemap_Consum(url, df_productos):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    
    if response.status == 200:
        soup = BeautifulSoup(response.data, 'html.parser')
        
        # Encontrar todos los tags <url>
        urls = soup.find_all('url')
        
        # Inicializar el navegador
        driver = webdriver.Chrome(ChromeDriverManager().install())

        for url in urls:
            loc = url.find('loc').text 
            print(loc)
            datosProducto(driver, df_productos, loc) 

        # Cerrar el navegador
        driver.quit()

    else:
        print("Failed to fetch sitemap:", response.status)


# if __name__ == '__main__':
#     crawl_sitemap(url_consum_map, df_productos_Consum)
#     #Cerrar el navegador
#     driver.quit()
#     # Guardar los datos en un archivo CSV
#     df_productos.to_csv('productos_supermercadosmas.csv', index=False)
