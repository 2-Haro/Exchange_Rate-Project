from bs4 import BeautifulSoup as BS
import requests as req

url = "https://finance.naver.com/marketindex/exchangeList.naver"
# 절대 경로(도메인): https://finance.naver.com
# 상대 경로: /marketindex/exchangeList.naver
res = req.get(url)
soup = BS(res.text, "html.parser")

tds = soup.find_all("td")

names = [] # 통화명 저장 리스트
for td in soup.select("td.tit"): # select 메소드로 td 태그 내의 class="tit"를 가진 td 태그를 찾아서 
  names.append(td.get_text(strip=True)) # 통화명 저장 리스트에 append

prices = [] # 매매기준율 저장 리스트
for td in soup.select("td.sale"): # select 메소드로 class="sale"를 가진 td 태그를 찾아서
  prices.append(td.get_text(strip=True)) # 매매기준율 저장 리스트에 append

print(names)
print(prices)