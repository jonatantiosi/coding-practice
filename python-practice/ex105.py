'''
105 — Web Scraping com BeautifulSoup
Tarefa: crie um script que faça o scraping de uma página web local
(por exemplo, http://127.0.0.1:3333/), encontre todos os parágrafos <p> e
imprima o conteúdo de cada um.
Conceitos: requests, BeautifulSoup, scraping, parsing HTML.
'''
import requests
from bs4 import BeautifulSoup

url = 'http://localhost:3333/'
reponse = requests.get(url)
bytes_html = reponse.content
parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='utf8')

paragrafos = parsed_html.find_all('p')

for p in paragrafos:
    print(p.text.strip())
