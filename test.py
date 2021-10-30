from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime, timezone, timedelta 

from fake_useragent import UserAgent
import random
import requests
#K
from selenium.common.exceptions import NoSuchElementException 

start_time = time.time()#開始時間
tz = timezone(timedelta(hours=+8))
# 取得現在時間、指定時區、轉為 ISO 格式
a = datetime.now(tz)
#開始時間
print("開始時間：",datetime.strftime(a,"%Y-%m-%d %H:%M:%S"))





#user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"

#kdown_1028
ua = UserAgent()
user_agent = ua.chrome

ips = [['80.59.199.212', '8080'],
     ['103.124.2.229', '3128']]
     #,['103.23.60.103', '8080']]



k = random.choice(ips)
proxies = k[0]+':'+k[1]
#kup_1028
print(proxies)
driverPath = '../../chromedriver'
opt = webdriver.ChromeOptions()
opt.add_argument('--user-agent=%s' % user_agent)
#k3_1028
# opt.add_argument('--proxy-server=https://' + proxies)
opt.add_argument(f'--proxy-server={proxies}')
opt.add_argument("--no-sandbox")
opt.add_argument("--disable-dev-shm-usage")
opt.add_argument("--headless")
#k1_1028
browser = webdriver.Chrome(driverPath,chrome_options=opt)
browser.implicitly_wait(10)   
browser.set_window_size(800, 700)
url = 'https://www.zeczec.com/categories?type=0'

browser.get(url)
time.sleep(2)
if browser.current_url == '' :
     print("ERROR !! no 200 !!")

# print(browser.page_source)
# print(browser.get_cookies())

try:
     # page = browser.find_element_by_class_name("button.button-s.dn.dib-ns")
     page = browser.find_elements_by_css_selector("a.button.button-s.dn.dib-ns")
     # page = browser.find_elements_by_xpath("//*[@class = 'button button-s dn dib-ns']")
     print(page)
     
except Exception as e:
     print(e)
# ls
page_inf = []
title_href_inf = []
date_time = []

for item in page:
     if item:
          # print(item.text)

          page_inf.append(item.text)
     else :
          print("there is no items")


print("page_inf",page_inf)


pages = int(page_inf[-1])

for page in range(18,19):
     url = 'https://www.zeczec.com/categories?page=x&type=0'
     url1 = url.replace('x',str(page))
     try:
          browser.get(url1)
          title_href = browser.find_elements_by_xpath('//body/div/div/div/div/a')
          print(f"第{page}頁共有{len(title_href)}筆專案要抓")
          #專案網址
          for item in title_href:
               if item:
                    title_href_inf.append(item.get_attribute('href'))
               else: 
                    print("NO item")
     except Exception as e:
          print(e) #可看到錯誤是什麼
          # error_url.append(url1)
          continue
     finally :
          print(title_href_inf)
          time.sleep(1) 
     
     now = datetime.now() #載入現在時間點
     now = now.strftime("%Y/%m/%d %H:%M:%S") #調整時間格式
     date_time.append(now)#時間戳記
     
     eighteen = browser.find_elements_by_class_name('lh-copy.ws-normal.button.green.mt3.w-100.tc') #18禁button位置
     print(eighteen)
     for item in eighteen:
          if "我已滿 18 歲並同意上述條款" in item.text:
               eighteen[0].click() #點擊按鈕
          else : 
               print("no 18")
     title = browser.find_elements_by_css_selector("h2.f4.mt2.mb1")#專案
     for item in title:
          if item:
               title_inf.append(item.text)
               print(item.text)

          else :
               print("OMG")




time.sleep(5) 
browser.close()


