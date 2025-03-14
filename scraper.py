from bs4 import BeautifulSoup
import requests

to_scrape = requests.get('https://toscrape.com/')
soup = BeautifulSoup(to_scrape, "html.parset")
qwots = soup.findAll("span", attrs={"class" : "text"})

for qwote in qwots:
    print(qwote.text)