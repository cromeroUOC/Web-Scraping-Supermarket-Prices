
import pandas as pd
from Consum import crawl_sitemap_Consum
from Dia import crawl_sitemap_Dia
from Supermercadosmas import crawl_sitemap_SupermercadosMas


url_consum = 'https://tienda.consum.es'
url_consum_map = 'https://tienda.consum.es/sitemap_product_es.xml'

url_Dia = 'https://www.supermercadosmas.com/'
url_Dia_map = 'https://www.dia.es/sitemap.xml'

url_SupermercadosMas_1 = 'https://www.supermercadosmas.com/pub/media/sitemap-1-1.xml'
url_SupermercadosMas_2 = 'https://www.supermercadosmas.com/pub/media/sitemap-1-2.xml'


def main():
    # Crear un DataFrame para guardar los productos
    df_productos = pd.DataFrame(columns=['Nombre', 'Marca', 'Precio', 'Supermercado', 'URL'])
    # Llamamos a la función de cada supermercado:
    # Supermercados Mas
    crawl_sitemap_SupermercadosMas(url_SupermercadosMas_1, df_productos)
    crawl_sitemap_Dia(url_Dia_map, df_productos)
    crawl_sitemap_Consum(url_consum_map, df_productos)

    # Guardar los datos en un archivo csv
    df_productos.to_csv('productos.csv', index=False)


if __name__ == "__main__":
    main()