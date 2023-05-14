import requests
from bs4 import BeautifulSoup

beautyLink = []

resp = requests.get('https://www.shiseido.com.vn/vi/axe_suncare/')
soup = BeautifulSoup(resp.content, "html.parser")

links = soup.select('.product-tiles-holder > .product-tile-outer > .product-tile-inner > .product-tile > .tile-top-section > .product-image > a ')

for link in links:
    beautyLink.append(link['href'])