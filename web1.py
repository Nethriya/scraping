import requests
from bs4 import BeautifulSoup
url="https://kaashiv.com/"
page=requests.get(url)
soup=BeautifulSoup(page.content,"html.parser")
result=(soup.find(id="hero").text)
print(result)