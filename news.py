from bs4 import BeautifulSoup
import requests as req
import sqlsaver
from sqlsaver import *
resp = req.get("https://rsue.ru/universitet/novosti/")

soup = BeautifulSoup(resp.text, features="html.parser")

dates = soup.find_all("div", id="news-date")
date = []
for a in dates:
    f = a.get_text()
    date.append(f)
titles = soup.find_all("div", id="news-title")
title = []
for a in titles:
    f = a.get_text()
    title.append(f)
texts = soup.find_all("div", id = "news-anons-text")
text = []
for a in texts:
    f = a.get_text()
    text.append(f)
for t in title:
    t = t.replace('\n', ' ')
    t = t.replace('\r', ' ')
    t = t.strip()
for t in text:
    t = t.replace('\n', ' ')
    t = t.replace('\r', ' ')
    t = t.replace('\t', ' ')
    t = t.strip()
print(title)
print(text)
sqlsaver.fill_news(title, text)
