#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#kelly-on zec branch

#爬取資料
# def information():
#get_ipython().run_line_magic('pip', 'install selenium')
#Ｋ：因為沒有jupyter,已經直接在外面裝好了
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
print("開始時間：",datetime.strftime(a,"%Y/%m/%d %H:%M:%S"))

#user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"

#kdown_1028
ua = UserAgent()
user_agent = ua.chrome

ips = [['80.59.199.212', '8080'],
    ['103.124.2.229', '3128'],
    ['103.23.60.103', '8080']]



k = random.choice(ips)
proxies = k[0]+':'+k[1]
print(proxies)

#kup_1028

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
browser.implicitly_wait(3)   
browser.set_window_size(800, 700)


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

#爬取網址
page_inf = []
url = 'https://www.zeczec.com/categories?type=0'
#k 保險requests
try:    
    # ua = {'User-agent': user_agent}
    # proxy = {'https':'https://'+proxies} 

    # re = requests.get(url,headers = ua,proxies = proxy , timeout =2)
    # print(re.status_code)
    # if str(re.status_code) == '200':
    #     print("成功get")
    # else:
    #     print("失敗")
    browser.get(url)


except Exception as e: 
    print("error get:",e)
finally :
    print(browser.current_url)
    


#k4
try :
    # page = browser.find_elements_by_class_name("button button-s dn dib-ns")
    page = browser.find_elements_by_css_selector("a.button.button-s.dn.dib-ns")

except Exception as e :
    print(e)

#專案
for item in page:
    if item:
        print(item.text)
        page_inf.append(item.text)

pages = int(page_inf[-1])

# for page in range(18,pages+1):
for page in range(18,18):
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
                    
    except Exception as e:
        print(e)#可看到錯誤是什麼
        error_url.append(url1)
        continue
    finally :
        time.sleep(1) 

#
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

    now = datetime.now() #載入現在時間點
    now = now.strftime("%Y-%m-%d %H:%M:%S") #調整時間格式
    date_time.append(now)#時間戳記
    
    eighteen = browser.find_elements_by_css_selector('.lh-copy.ws-normal.button.green.mt3.w-100.tc') #18禁button位置
    for item in eighteen:
        if "我已滿 18 歲並同意上述條款" in item.text:
            eighteen[0].click() #點擊按鈕

    title = browser.find_elements_by_css_selector(".f4.mt2.mb1")#專案
    for item in title:
        if item:
            title_inf.append(item.text)
            print(item.text)

    category = browser.find_elements_by_xpath('//body/div/div/div/div/div/a[2]')#專案類別
    for item in category:
        if item:
            category_inf.append(item.text)
            print(item.text)

    name = browser.find_elements_by_css_selector(".b.f6")#提案人
    for item in name:
        if item:
            name_inf.append(item.text)
            name_href_inf.append(item.get_attribute('href'))
            print(item.text)

    price_target = browser.find_elements_by_xpath("//body/div/div/div/div/div/div[@class='f7']")#目標金額
    for item in price_target:
        if item:
            price_target_inf.append(item.text)
            print(item.text)

    price = browser.find_elements_by_css_selector(".f3.b.js-sum-raised.nowrap")#募得金額
    for item in price:
        if item:
            price_inf.append(item.text)
            print(item.text)

    price_rate = browser.find_elements_by_css_selector(".js-percentage-raised.stroke")#金額達成率
    for item in price_rate:
        if item:
            price_rate_inf.append(item.text)
            print(item.text)

    people = browser.find_elements_by_css_selector(".js-backers-count")#贊助人數
    for i in range(len(title)):
        try:
            if people[i].text:
                people_inf.append(people[i].text) 
        except IndexError:
            people_inf.append(0)

    times = browser.find_elements_by_css_selector(".mb2.f7")#募資時間
    for item in times:
        if "時程" in item.text:
            times_inf.append(item.text)
            print(item.text)

    times_left = browser.find_elements_by_css_selector(".js-time-left")#剩餘時間
    for i in range(len(title)):
        try:
            if times_left[i].text:
                times_left_inf.append(times_left[i].text) 
        except IndexError:
            times_left_inf.append("專案已結束")

    program_price = browser.find_elements_by_css_selector(".black.b.f4")#募資方案
    for item in program_price:
        if item:
            program_price_inf.append(item.text)
    program_price_inf1.append(program_price_inf)
    program_price_inf = []#募資方案

    program_people = browser.find_elements_by_css_selector(".f7.mv2")#方案贊助人數
    for item in program_people:
        if item.text == '':
            program_people_inf.append(0)
        else:
            program_people_inf.append(item.text)
    program_people_inf1.append(program_people_inf)
    program_people_inf = []#方案贊助人數

    realization_time = browser.find_elements_by_css_selector(".mt3.gray.tc.ph2.f7.ba")#實現時間
    for item in realization_time:
        if item:
            realization_time_inf.append(item.text)
    realization_time_inf1.append(realization_time_inf)
    realization_time_inf = []#實現時間

    title_content = browser.find_elements_by_xpath('//tbody/tr/td')#專案內容
    for item in title_content:
        if item.text != '':
            title_content_inf.append(item.text)
        else:
            title_content_inf.append('NA')

    one_img = browser.find_elements_by_css_selector(".overflow-hidden.aspect-ratio-project-cover.bg-near-white.br2-l")#第一張圖片
    for item in one_img:
        if item:
            img1 = item.get_attribute('style')
            title_img_inf.append(img1.split('"')[1])

    title_img = browser.find_elements_by_xpath('//img')#專案圖片
    for item in title_img:
        if item:
            title_img_inf.append(item.get_attribute('src'))
        if "None" : 
            title_img_inf.append(item.get_attribute('data-img-src'))
    for item in title_img_inf:
        if item != None:
            title_img_inf1.append(item)
    count_img_inf.append(len(title_img_inf1))
    title_img_inf2.append(title_img_inf1)
    title_img_inf1 = []#專案圖片

    time.sleep(2)

#提案人網站
for link in name_href_inf:
    try:
        browser.get(link)

    except Exception as e:
        print(e)#可看到錯誤是什麼
        error_link.append(link)
        continue

    name_int = browser.find_elements_by_css_selector(".f6.mv-child-0.mv3")#提案人介紹
    for i in range(len(title)):
        try:
            if name_int[i].text:
                name_int_inf.append(name_int[i].text) 
        except IndexError:
            name_int_inf.append("NA")

    name_web = browser.find_elements_by_css_selector(".v-mid.mb2.mr3.dark-gray.f6.underline.b.relaitve.dib")#提案人網站平台
    for item in name_web:
        if item:
            name_web_inf.append(item.text)
            name_web_href_inf.append(item.get_attribute('href'))
    name_web_inf1.append(name_web_inf)
    name_web_href_inf1.append(name_web_href_inf)
    name_web_inf = []#提案人網站平台
    name_web_href_inf = []#提案人網站平台網址

    name_spon = browser.find_elements_by_css_selector(".tr.nowrap")#提案人贊助資訊與加入天數
    for item in name_spon:
        if item:
            name_spon_inf.append(item.text)
    name_spon_inf1.append(name_spon_inf)
    name_spon_inf = []#提案人贊助資訊與加入天數

    time.sleep(2)

#提案人發起計畫網頁
for link in name_href_inf:#更新網頁
    new_url = link + "?tab=projects"
    name_plan_url_inf.append(new_url)
for link in name_plan_url_inf:#開始爬取
    try:
        browser.get(link)

    except Exception as e:
        print(e)#可看到錯誤是什麼
        error_link.append(link)
        continue

    name_plan_title = browser.find_elements_by_xpath('//body/div/ul/li/div/a')#提案人發起計畫專案
    for item in name_plan_title:
        if item:
            name_plan_title_inf.append(item.text)
            name_plan_title_href_inf.append(item.get_attribute('href'))
    name_plan_title_inf1.append(name_plan_title_inf)
    name_plan_title_href_inf1.append(name_plan_title_href_inf)
    name_plan_title_inf = []#提案人發起計畫專案
    name_plan_title_href_inf = []#提案人發起計畫專案網址

    name_plan_title = browser.find_elements_by_css_selector(".db.f7")#提案人發起計畫專案日期
    for item in name_plan_title:
        if item:
            name_plan_day_inf.append(item.text)
    name_plan_day_inf1.append(name_plan_day_inf)
    name_plan_day_inf = []#提案人發起計畫專案日期

    time.sleep(2)

#專案更新
for link in title_href_inf:
    new_url = link + "/updates"
    try:
        browser.get(new_url)

    except Exception as e:
        print(e)#可看到錯誤是什麼
        error_link.append(new_url)
        continue

    updates = browser.find_elements_by_css_selector(".b.b--drak-gray.bb-l.dib.hover-b--dark-gray.mr4.mt1.near-black.pv3")#專案更新次數
    for i in range(len(title)):
        try:
            if updates[i].text:
                updates_inf.append(updates[i].text) 
        except IndexError:
            updates_inf.append(0)

#整理
for item in title_img_inf2:
    if item != []:
        title_img_inf3.append(item)
    elif item == []:
        title_img_inf3.append("NA")

for item in name_web_inf1:
    if item != []:
        name_web_inf2.append(item)
    elif item == []:
        name_web_inf2.append("NA")

for item in name_web_href_inf1:
    if item != []:
        name_web_href_inf2.append(item)
    elif item == []:
        name_web_href_inf2.append("NA")

for item in name_plan_title_inf1:
    if item != []:
        name_plan_title_inf2.append(item)
    elif item == []:
        name_plan_title_inf2.append("NA")

for item in name_plan_title_href_inf1:
    if item != []:
        name_plan_title_href_inf2.append(item)
    elif item == []:
        name_plan_title_href_inf2.append("NA")

for item in name_plan_day_inf1:
    if item != []:
        name_plan_day_inf2.append(item)
    elif item == []:
        name_plan_day_inf2.append("NA")

end_time = time.time()#結束時間
alltime = end_time - start_time

#k1028:f不能用
print("{} 分 {} 秒爬取".float(int(alltime//60),int(alltime%60)))


import json
data = []

for i in range(len(title_inf)): #將爬蟲內容轉成字典
    result0 = dict(date_time=date_time,
                   title=title_inf[i],
                   title_url=title_href_inf[i],
                   category=category_inf[i],
                   name=name_inf[i],
                   name_url=name_href_inf[i],
                   name_int=name_int_inf[i],
                   name_web=name_web_inf2[i],
                   name_web_url=name_web_href_inf2[i],
                   name_spon=name_spon_inf1[i],
                   name_plan_title=name_plan_title_inf2[i],
                   name_plan_title_url=name_plan_title_href_inf2[i],
                   name_plan_day=name_plan_day_inf2[i],
                   price_target=price_target_inf[i],
                   price=price_inf[i],
                   price_rate=price_rate_inf[i],
                   people=people_inf[i],
                   times=times_inf[i],
                   times_left=times_left_inf[i],
                   program_price=program_price_inf1[i],
                   program_people=program_people_inf1[i],
                   realization_time=realization_time_inf1[i],
                   title_content=title_content_inf[i],
                   count_img=count_img_inf[i],
                   title_img=title_img_inf3[i],
                   updates=updates_inf[i])
    data.append(result0)#存入list
#最終json
result={'error_url':error_url,'error_link':error_link,'error_nam':error_name,'error_name_plan':error_name_plan,'error_updates':error_updates,'error_updates_content':error_updates_content,'error_comments':error_comments,'error_faqs':error_faqs,'data':data}

#存成json
fn = 'zeczec_finish.json'
with open(fn, 'w', encoding='utf-8') as fnresult:
    json.dump(result,fnresult,ensure_ascii=False)
print(result)

