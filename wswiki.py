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
