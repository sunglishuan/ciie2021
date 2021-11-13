from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime, timezone, timedelta 

from fake_useragent import UserAgent
import random
import requests
#K
from selenium.common.exceptions import NoSuchElementException 

date_time = []#時間戳記
title_inf = []#專案
title_href_inf = []#專案網址
category_inf = []#專案類別
name_inf = []#提案人
name_href_inf = []#提案人網址
name_int_inf = []#提案人介紹
name_web_inf = []#提案人網站平台
name_web_inf1 = []#提案人網站平台
name_web_inf2 = []#提案人網站平台
name_web_href_inf = []#提案人網站平台網址
name_web_href_inf1 = []#提案人網站平台網址
name_web_href_inf2 = []#提案人網站平台網址
fb_href_inf = []#fb網址
name_spon_inf = []#提案人贊助資訊與加入天數
name_spon_inf1 = []#提案人贊助資訊與加入天數
name_plan_url_inf = []#提案人發起計畫網頁
name_plan_title_inf = []#提案人發起計畫專案
name_plan_title_inf1 = []#提案人發起計畫專案
name_plan_title_inf2 = []#提案人發起計畫專案
name_plan_title_href_inf = []#提案人發起計畫專案網址
name_plan_title_href_inf1 = []#提案人發起計畫專案網址
name_plan_title_href_inf2 = []#提案人發起計畫專案網址
name_plan_day_inf = []#提案人發起計畫專案日期
name_plan_day_inf1 = []#提案人發起計畫專案日期
name_plan_day_inf2 = []#提案人發起計畫專案日期
price_target_inf = []#目標金額
price_inf = []#募得金額
price_rate_inf = []#金額達成率
people_inf = []#贊助人數
times_inf = []#募資時間
times_left_inf = []#剩餘時間
program_price_inf = []#募資方案
program_price_inf1 = []#募資方案
program_people_inf = []#方案贊助人數
program_people_inf1 = []#方案贊助人數
realization_time_inf = []#實現時間
realization_time_inf1 = []#實現時間
title_content_inf = []#專案內容
title_img_inf = []#專案圖片
title_img_inf1 = []#專案圖片
title_img_inf2 = []#專案圖片
title_img_inf3 = []#專案圖片
count_img_inf = []#專案圖片數
updates_inf = []#專案更新次數
faqs_inf = []#專案問答數
error_url = []#爬取網址
error_link = []#專案網站
error_name = []#提案人網站
error_name_plan = []#提案人發起計畫網頁
error_updates = []#專案更新
error_updates_content = []#專案更新內容
error_comments = []#專案留言
error_faqs = []#專案問答

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

ips = [['80.59.199.212', '8080']]
     #,['103.124.2.229', '3128']]
     #,['103.23.60.103', '8080']]



k = random.choice(ips)
proxies = k[0]+':'+k[1]
#kup_1028
print(proxies)
driverPath = '../chromedriver'
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
     print('專案連結')
     print(title_href_inf)
     time.sleep(1) 
     
print("開始抓專案囉！")

now_web = 0 
#專案網站
for link in title_href_inf:
     now_web +=1
     print(f"現在是第{now_web}個專案") 
     try:
          browser.get(link)
          print(browser.current_url)

     except Exception as e:
          print(e)#可看到錯誤是什麼
          error_link.append(link)
          continue
     ### 載入現在時間點
     now = datetime.now()
     now = now.strftime("%Y/%m/%d %H:%M:%S") #調整時間格式
     date_time.append(now)#時間戳記


    eighteen = browser.find_elements_by_css_selector('.lh-copy.ws-normal.button.green.mt3.w-100.tc') #18禁button位置
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
