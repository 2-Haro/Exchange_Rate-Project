import requests as req

res = req.get("https://finance.naver.com/marketindex/?tabSel=exchange#tab_section")

html = res.text # html: HTML 문서
pos = html.find("미국 USD")
print(pos)

print("\n------------------------------------------------------------------------------------------------------------------------------------------\n")

res = req.get("https://finance.naver.com/marketindex/?tabSel=exchange#tab_section")

html = res.text # html: HTML 문서
s = html.split('<span class="value">')[1].split("</span>")[0]
print(s)