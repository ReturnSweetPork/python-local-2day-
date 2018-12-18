import requests
from bs4 import BeautifulSoup

url = "https://sports.news.nate.com/abrsoccer/schedule"
res = requests.get(url).text

soup = BeautifulSoup(res, 'html.parser')


soccers = soup.select("tbody tr")

for soccer in soccers:
    print(soccer.text)











