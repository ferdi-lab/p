import requests
from bs4 import BeautifulSoup
import re  # Para mejorar la detección de superficie y PIB

# URL de la página de Albania en Wikipedia
URL = "https://es.wikipedia.org/wiki/Albania"

def obtener_soup(url):
    """Realiza una solicitud a la URL y devuelve el objeto BeautifulSoup."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error si la petición falla
        return BeautifulSoup(response.text, 'html.parser')
    except requests.RequestException as e:
        print(f"Error al obtener la página: {e}")
        return None

def obtener_primer_parrafo(soup):
    """Obtiene el primer párrafo con contenido de la página."""
    if not soup:
        return "No se encontró un párrafo válido."
    
    for p in soup.find_all('p'):
        texto = p.text.strip()
        if texto:
            return texto
    return "No se encontró un párrafo válido."

def obtener_dato_infobox(soup, palabra_clave):
    """Busca un dato en la infobox basado en una palabra clave."""
    if not soup:
        return "No encontrada"
    
    infobox = soup.find('table', class_='infobox')
    if not infobox:
        return "No encontrada"

    for fila in infobox.find_all('tr'):
        encabezado = fila.find('th')
        contenido = fila.find('td')

        if encabezado and contenido:
            contenido_texto = contenido.text.strip()
            # Usamos regex para buscar km² o PIB en cualquier parte del texto
            if re.search(palabra_clave, contenido_texto, re.IGNORECASE):
                return contenido_texto

    return "No encontrada"

# Obtener el contenido de la página
soup = obtener_soup(URL)

# Extraer datos
primer_parrafo = obtener_primer_parrafo(soup)
superficie = obtener_dato_infobox(soup, r'km²')
pib = obtener_dato_infobox(soup, r'\b(billion|PIB|PBI)\b')  # Captura distintas formas de referirse al PIB

# Mostrar resultados
print("📌 Primer párrafo de Albania en Wikipedia:\n", primer_parrafo)
print("\n🌍 Superficie total de Albania:\n", superficie)
print("\n💰 PIB de Albania:\n", pib)