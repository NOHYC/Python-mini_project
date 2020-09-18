
import urllib.request
from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver

def text_cf(part1_s):
    part1_ss= part1_s.replace("      ","")
    part1_sss= part1_ss.replace("<p>","")
    part1_ssss = part1_sss.replace("</p>","")
    part1_s4 = part1_ssss.replace('''<span class="tex-font-style-tt">''',"")
    part1_s5 = part1_s4.replace('''<span class="tex-font-style-it">''',"")
    part1_s6 = part1_s5.replace('''<span class="tex-font-style-bf">''',"")
    part1_s7 = part1_s6.replace('''<div class="input-specification">''',"")
    part1_s8 = part1_s7.replace('''<div class="section-title">''',"")
    part1_s9 = part1_s8.replace('</div>',"")
    part1_s10 = part1_s9.replace('</span>',"")
    part1_s11 = part1_s10.replace("\le","<= ")
    part1_s12 = part1_s11.replace('<ul>',"")
    part1_s13 = part1_s12.replace('</ul>',"")
    part1_s14 = part1_s13.replace('<li>',"")
    part1_s15 = part1_s14.replace('</li>',"")
    part1_s16 = part1_s15.replace('<div>',"")
    part1_s17 = part1_s16.replace("\ldots","......")
    part1_s18 = part1_s17.replace("\\ne"," != ")
    part1_s19 = part1_s18.replace("i-th","i_th ")
    part1_s20 = part1_s19.replace("\\to"," -> ")
    part1_s21 = part1_s20.replace('''<div class="output-specification">''',"")
    part1_s22 = part1_s21.replace("\,",",")
    part1_s23 = part1_s22.replace("\dots","...")
    part1_s24 = part1_s23.replace("\cdot","*")
    return part1_s24

def code_Se(res,string):
    import re
    part1 = res.select(string)
    part1_s = re.sub("[$]?","",str(part1))
    return part1_s

#pageContent > div.problemindexholder > div > div > div:nth-child(2)
url = "https://codeforces.com/problemset/problem/1393/B"

readl = urllib.request.urlopen(url).read().decode('utf-8')
res = BeautifulSoup(readl,'html.parser')


part1 = code_Se(res,'#pageContent > div.problemindexholder > div > div > div:nth-child(2)')
part2 =code_Se(res,'''#pageContent > div.problemindexholder > div > div > div.input-specification''')
part3 = code_Se(res,'''#pageContent > div.problemindexholder > div > div > div.output-specification''')
sentance = part1+part2+part3
sss = text_cf(sentance)

time.sleep(1)


############## 번역 접속 부분
driver = webdriver.Chrome("C:/chromedrive/chromedriver.exe")
kakao_url = "https://translate.kakao.com/"
driver.get(kakao_url)
html =driver.page_source
time.sleep(2)

input_text = driver.find_element_by_css_selector("div.box_tf>div.tf_translation")
input_text.clear()
input_text.send_keys(sss)

time.sleep(3)

html1 = driver.page_source
soup1 = BeautifulSoup(html1,"html.parser")
result = soup1.select("p.desc_translation")[0].text

print(result)