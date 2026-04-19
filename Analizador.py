#importaciones
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

#scraping

url = "https://books.toscrape.com"
respuesta = requests.get(url)
soup = BeautifulSoup(respuesta.text, 'html.parser')

titulos = []
precios = []

libros = soup.find_all('article', class_='product_pod')

for libro in libros:
    titulo = libro.h3.a['title']
    precio = libro.find('p', class_='price_color').text

    titulos.append(titulo)
    precios.append(precio)

#DataFrame

datos = {'titulo': titulos, 'precio': precios}

df = pd.DataFrame(datos)
df.to_csv('lista_de_libros.csv', index = False)

print("'lista_de_libros.csv', fue creado con exito.")

#Archivo CSV

lec = pd.read_csv('lista_de_libros.csv')
lec['precio'] = lec['precio'].str.replace('[^0-9.]', '', regex=True).astype(float)

print(lec)
print(lec.describe())

#grafica

lec_sorted = lec.sort_values('precio', ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(lec_sorted['titulo'], lec_sorted['precio'], color='steelblue')
plt.title('Análisis de Precios de Libros', fontsize=16)
plt.xlabel('Libro', fontsize=12)
plt.ylabel('Precio (£)', fontsize=12)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
