import requests
from bs4 import BeautifulSoup

# URL de la página de Albania en Wikipedia
URL = "https://es.wikipedia.org/wiki/Albania"

# Obtener la página
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrar todos los párrafos
parrafos = soup.find_all('p')
superficie = soup.find_all()

# Buscar el primer párrafo con contenido
primer_parrafo = "No se encontró un párrafo válido."
for p in parrafos:
    texto = p.text.strip()
    if texto:  # Si el párrafo tiene contenido
        primer_parrafo = texto
        break

print("Primer párrafo de Albania en Wikipedia:")
print(primer_parrafo)

# Buscar la tabla de información (infobox)
infobox = soup.find('table', class_='infobox')

# Buscar la fila donde se menciona "km²" para encontrar la superficie total
superficie = "No encontrada"
if infobox:
    for fila in infobox.find_all('tr'):  # Recorremos las filas de la tabla
        encabezado = fila.find('th')  # Encuentra la cabecera de la fila
        contenido = fila.find('td')  # Encuentra el contenido de la fila
        
        if encabezado and contenido:
            encabezado_texto = encabezado.text.strip().lower()  # Convertimos a minúsculas
            contenido_texto = contenido.text.strip()  # Texto del contenido
            
            if "km²" in contenido_texto:
                superficie = contenido_texto
                break  # Detenemos el bucle al encontrar la superficie total válida

print("Superficie total de Albania en Wikipedia:")
print(superficie)

# Buscar la fila donde se menciona "billion" para localizar el dato del PIB
pib = "No encontrada"
if infobox:
    for fila in infobox.find_all('tr'):  # Recorremos las filas de la tabla
        encabezado = fila.find('th')  # Encuentra la cabecera de la fila
        contenido = fila.find('td')  # Encuentra el contenido de la fila
        
        if encabezado and contenido:
            encabezado_texto = encabezado.text.strip().lower()  # Convertimos a minúsculas
            contenido_texto = contenido.text.strip()  # Texto del contenido
            
            if "billion" in contenido_texto:
                pib = contenido_texto
                break  # Detenemos el bucle al encontrar el pib
print("El producto interior bruto de Albania en Wikipedia:")
print(pib)