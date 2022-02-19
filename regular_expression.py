import requests as req
import re

url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res = req.get(url)
body = res.text # body: HTML 문서

r = re.compile("미국 USD.*?value\">(.*?)</", re.DOTALL) # 정규표현식 준비 # DOT(.): 개행을 제외하기 때문에 re.DOTALL을 사용
                                                        # .*? -> 문자 패턴 중에서 가장 좁은 범위를 가져오도록 설정
captures = r.findall(body)

print(captures)

print("\n------------------------------------------------------------------------------------------------------------------------------------------\n")

url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res = req.get(url)
body = res.text # body: HTML 문서

r = re.compile("h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL) # 정규표현식 준비 # DOT(.): 개행을 제외하기 때문에 re.DOTALL을 사용
                                                                            # .*? -> 문자 패턴 중에서 가장 좁은 범위를 가져오도록 설정
captures = r.findall(body)

print(captures)

print("\n------------------------------------------------------------------------------------------------------------------------------------------\n")

url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res = req.get(url)
body = res.text # body: HTML 문서

r = re.compile("h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL) # 정규표현식 준비 # DOT(.): 개행을 제외하기 때문에 re.DOTALL을 사용
                                                                            # .*? -> 문자 패턴 중에서 가장 좁은 범위를 가져오도록 설정
captures = r.findall(body)

print("----------")
print("환율 계산기")
print("----------")
print()

for c in captures:
  print(c[0], ":", c[1])

print()
usd = float(captures[0][1].replace(",", ""))
won = input("달러로 바꾸길 원하는 금액(원)을 입력해주세요: ")
won = int(won)
dollar = won / usd
dollar = int(dollar)
print(f"{dollar} 달러로 환전되었습니다.")