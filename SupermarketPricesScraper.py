import builtwith
import whois
import urllib3
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# Para conocer el tipo de tecnologia con la que se creó la web
# builtwith.parse('https://www.supermercadosmas.com/')

# Identificar propietario de la web
# print(whois.whois('https://www.supermercadosmas.com/'))

# Función para sacar las urls de todos los artículos del supermercado
def crawl_sitemap(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    
    # Comprobar si el request es correcto (200)
    if response.status == 200:
      
        soup = BeautifulSoup(response.data, 'html.parser')
        
        # Encontrar todos los tags url
        urls = soup.find_all('url')
        
        # Extraer todas las urls con priority 1.0 (son los artículos)
        for url in urls:
            priority = url.find('priority')
            if priority and priority.text == '1.0':
                loc = url.find('loc').text
                print(loc)
                
    else:
        print("Failed to fetch sitemap:", response.status)


crawl_sitemap("https://www.supermercadosmas.com/pub/media/sitemap-1-1.xml")
crawl_sitemap("https://www.supermercadosmas.com/pub/media/sitemap-1-2.xml")
