from bs4 import BeautifulSoup as BS
import requests as req

url = "https://naver.com"
res = req.get(url)
soup = BS(res.text, "html.parser") # HTML 외에도 XML과 같은 다른 문서들도 인식할 수 있으므로 HTML을 parsing 한다는 것을 명시

print(soup.title) # <title>NAVER</title>
print(soup.title.string) # NAVER

print("\n------------------------------------------------------------------------------------------------------------------------------------------\n")

url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res = req.get(url)
soup = BS(res.text, "html.parser")

tds = soup.find_all("td")
print(tds) # 제대로 출력되지 않음
# iframe 태그(다른 HTML 문서를 가져와서 보여줌)를 사용해서 하나의 네이버 금융 페이지가 여러 페이지로 나뉘어 있기 때문

print("\n------------------------------------------------------------------------------------------------------------------------------------------\n")

url = "https://finance.naver.com/marketindex/exchangeList.naver"
# 절대 경로(도메인): https://finance.naver.com
# 상대 경로: /marketindex/exchangeList.naver
res = req.get(url)
soup = BS(res.text, "html.parser")

tds = soup.find_all("td")

for td in tds:
  if len(td.find_all("a")) == 0:  # find_all 함수는 리스트를 반환해주기 때문에 1) a 태그가 없는 요소 출력 X 2) a 태그가 있는 요소 출력
    continue
  print(td.get_text(strip=True)) # get_text(strip=True) -> 공백을 제거한 상태로 텍스트를 가져온다
  print(td.string) # 공백 포함
  for s in td.strings: # 제너레이터 패턴 # 공백 포함
    print(s)
  for s in td.stripped_strings: # 제너레이터 패턴 # 공백 제거
    print(s)

print("\n------------------------------------------------------------------------------------------------------------------------------------------\n")

url = "https://finance.naver.com/marketindex/exchangeList.naver"
# 절대 경로(도메인): https://finance.naver.com
# 상대 경로: /marketindex/exchangeList.naver
res = req.get(url)
soup = BS(res.text, "html.parser")

tds = soup.find_all("td")

names = [] # 통화명 저장 리스트
for td in tds:
  if len(td.find_all("a")) == 0:  # find_all 함수는 리스트를 반환해주기 때문에 1) a 태그가 없는 요소 출력 X 2) a 태그가 있는 요소 출력
    continue
  names.append(td.get_text(strip=True)) # 통화명을 리스트에 저장

prices = [] # 매매기준율 저장 리스트
for td in tds:
  if "class" in td.attrs: # td 태그 내에 "class" attribute가 없는 경우가 있으므로, "class" attribute를 가진 경우만 탐색(오류 발생 방지)
    if "sale" in td.attrs["class"]: # td 태그 내의 "class" attribute(attrs)의 값이 "sale"이면, prices 리스트에 append
  # <td class="sale"></td>
      prices.append(td.get_text(strip=True))

print(names)
print(prices)