
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
    #Mirar si existe el archivo de productos
    try:
        # Si el archivo existe, cargarlo en un DataFrame
        df_productos = pd.read_csv('../dataset/productos.csv')
        #Borrar archivo para volver a cargarlo
        df_productos.drop(df_productos.index, inplace=True)
    except:
        # Crear un DataFrame para guardar los productos
        df_productos = pd.DataFrame(columns=['Nombre', 'Marca', 'Precio', 'Supermercado', 'URL'])

    # Llamamos a la función de cada supermercado:
    try:
        crawl_sitemap_Consum(url_consum_map, df_productos)
    except:
        print('Error en Consum')
    try:    
        crawl_sitemap_SupermercadosMas(url_SupermercadosMas_1, df_productos)
        crawl_sitemap_SupermercadosMas(url_SupermercadosMas_2, df_productos)
    except:
        print('Error en SupermercadosMas')
    try:
        crawl_sitemap_Dia(url_Dia_map, df_productos)
    except:
        print('Error en Dia')

    # Guardar los datos en un archivo csv en la carpeta dataset fuera de la carpeta source
    df_productos.to_csv('../dataset/productos.csv', index=False)


if __name__ == "__main__":
    main()