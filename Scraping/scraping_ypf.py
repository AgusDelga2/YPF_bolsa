from bs4 import BeautifulSoup
import requests

url = "https://es.investing.com/equities/ypf-sociedad"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

print(soup)