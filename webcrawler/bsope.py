import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.python123.io/ws/demo.html")
demo = r.text
soup=BeautifulSoup(demo,"html.parser")
print("=====================")
print(soup.prettify())
print("=====================")
print(soup.title)
print(soup.a)
print(soup.a.name)