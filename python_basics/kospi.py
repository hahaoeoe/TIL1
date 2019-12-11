import requests
from bs4 import BeautifulSoup

#response = requests.get('https://finance.naver.com/sise/').text
#soup = BeautifulSoup(response, 'html.parser')
#kospi = soup.select_one('#KOSPI_now').text

#print(kospi)

response = requests.get('https://finance.naver.com/marketindex/').text
soup = BeautifulSoup(response, 'html.parser')
usd = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text

print(usd)

