import requests
from bs4 import BeautifulSoup

url = "http://www.kita.net/exchangeRate_info/exchangeRate_info_list.jsp"
res = requests.get(url).text

soup = BeautifulSoup(res, 'html.parser')

hhs = soup.select("tbody tr")
print(len(hhs))
for hh in hhs:
    print(hh.select_one("td:nth-of-type(1)").text)
    print(hh.select_one("th:nth-of-type(1)").text)





