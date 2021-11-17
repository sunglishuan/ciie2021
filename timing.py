#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#爬取資料
# def information():
# get_ipython().run_line_magic('pip', 'install selenium')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime, timezone, timedelta 
from fake_useragent import UserAgent
import random

start_time = time.time()#開始時間

tz = timezone(timedelta(hours=+8))
# 取得現在時間、指定時區、轉為 ISO 格式
a = datetime.now(tz)
#開始時間
print("開始時間：",datetime.strftime(a,"%Y/%m/%d %H:%M:%S"))

# user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
ua = UserAgent()
user_agent = ua.chrome


driverPath = '/home/g07153104/chromedriver'
opt = webdriver.ChromeOptions()
opt.add_argument('--user-agent=%s' % user_agent)

#改:之後要加上proxy
#opt.add_argument(f'--proxy-server={proxies}')

#改:不打開監控螢幕
opt.add_argument("--no-sandbox")
opt.add_argument("--disable-dev-shm-usage")
opt.add_argument("--headless")
#改底
browser = webdriver.Chrome(driverPath, chrome_options=opt)  #改：no options , only chrome_options
browser.implicitly_wait(1)   
browser.set_window_size(800, 700)



date_time = []#時間戳記
title_inf = []#專案
title_href_inf = []#專案網址
price_inf = []#募得金額
price_rate_inf = []#金額達成率
people_inf = []#贊助人數
times_left_inf = []#剩餘時間
program_price_inf = []#募資方案
program_price_inf1 = []#募資方案
program_people_inf = []#方案贊助人數
program_people_inf1 = []#方案贊助人數
realization_time_inf = []#實現時間
realization_time_inf1 = []#實現時間
updates_inf = []#專案更新次數
error_url = []#爬取網址
error_link = []#專案網站
error_updates = []#專案更新
timing_inf = []#判斷是否進行中專案

active =True
#爬取網址
page_inf = []
url = 'https://www.zeczec.com/categories?type=0'
browser.get(url)
page = browser.find_elements_by_css_selector("a.button.button-s.dn.dib-ns")
for item in page:
    if item:
        page_inf.append(item.text)
pages = int(page_inf[-1])

for page in range(1,pages+1):
    url = 'https://www.zeczec.com/categories?page=x&type=0'
    url1 = url.replace('x',str(page))
    if active == False:
        break
    try:
        browser.get(url1)

    except Exception as e:
        print("爬取網址：",e)#可看到錯誤是什麼
        error_url.append(url1)
        continue

    timing = browser.find_elements_by_xpath("//body/div/div/div/div/div/span[@class='f7']")
    for item in timing:
        if "成功" not in item.text:
            timing_inf.append(item.text)
        else:
            active = False
    title_href = browser.find_elements_by_xpath('//body/div/div/div/div/a')
    #專案網址
    for item in title_href:
        if item:
            title_href_inf.append(item.get_attribute('href'))
            
#索引進行中專案
title_href_inf = title_href_inf[0:len(timing_inf)]

#
print("開始抓專案囉！")
print(f"有{len(title_href_inf)}筆專案要抓")


#專案網站
for link in title_href_inf:
    try:
        browser.get(link)

    except Exception as e:
        print("專案網站：",e)#可看到錯誤是什麼
        error_link.append(link)
        date_time.append('NA')
        title_inf.append('NA')
        price_inf.append('NA')
        price_rate_inf.append('NA')
        people_inf.append(0)
        times_left_inf.append('NA')
        program_price_inf1.append('NA')
        program_people_inf1.append('NA')
        realization_time_inf1.append('NA')
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

    times_left = browser.find_elements_by_css_selector(".js-time-left")#剩餘時間
    for i in range(len(title)):
        try:
            if times_left[i].text:
                times_left_inf.append(times_left[i].text) 
        except IndexError:
            times_left_inf.append("專案即將開始")

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

    time.sleep(2)
for del_link in error_link:
    title_href_inf.remove(del_link)
#專案更新
for link in title_href_inf:
    new_url = link + "/updates"
    try:
        browser.get(new_url)

    except Exception as e:
        print("專案更新：",e)#可看到錯誤是什麼
        error_updates.append(new_url)
        updates_inf.append(0)
        continue

    updates = browser.find_elements_by_css_selector(".b.b--drak-gray.bb-l.dib.hover-b--dark-gray.mr4.mt1.near-black.pv3")#專案更新次數
    for i in range(len(title)):
        try:
            if updates[i].text:
                updates_inf.append(updates[i].text) 
        except IndexError:
            updates_inf.append(0)

end_time = time.time()#結束時間
alltime = end_time - start_time
print(f"{int(alltime//60)} 分 {int(alltime%60)} 秒爬取專案")    


#寫成字典格式並備份
import json

data = []

for i in range(len(title_inf)): #將爬蟲內容轉成字典
    result0 = dict(date_time=date_time[i],
                   title=title_inf[i],
                   title_url=title_href_inf[i],
                   price=price_inf[i],
                   price_rate=price_rate_inf[i],
                   people=people_inf[i],
                   times_left=times_left_inf[i],
                   program_price=program_price_inf1[i],
                   program_people=program_people_inf1[i],
                   realization_time=realization_time_inf1[i],
                   updates=updates_inf[i])
    data.append(result0)#存入list
#最終json
result={'error_url':error_url,'error_link':error_link,'error_updates':error_updates,'data':data}

#存成json
now = datetime.now() #載入現在時間點
now = now.strftime("%Y%m%d_%H%M") #調整時間格式
fn = f'./lotsFix/zeczec_timing_{now}.json'
# with open(fn, 'w', encoding='utf-8') as fnresult:
#     json.dump(result,fnresult,ensure_ascii=False)
    

start_time = time.time()#開始時間
#傳入資料庫    
# get_ipython().run_line_magic('pip', 'install pymysql')

import pymysql

data_last = result['data']
#將字典值的list轉成字串(因為sql無法放list)
def listtostr(x):
    for i in data_last:
        a = i[x]
        i[x] = str(a)
changelist = ['program_price','program_people','realization_time']
for j in changelist:
    listtostr(j)
    
# 資料庫設定
db_settings = {
    "host": "34.87.79.81",
    "port": 3306,
    "user": "07170282",
    "password": "ciie07170282",
    "charset": "utf8mb4",
    "db": "zeczec",
}

#將設定參數與資料庫連線
try:
    # 建立Connection物件
    conn = pymysql.connect(**db_settings)

    # 建立Cursor物件(可放入資料庫的指令或查詢)
    with conn.cursor() as cursor:

        for data in data_last:
            #sql語法
            columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())#加入欄位
            holder = ', '.join(['%s'] * len(data))#加入值的數量(%s)
            values = ', '.join("'" + str(x).replace("'",'"') + "'" for x in data.values())#加入值
            sql = "INSERT INTO timing (%s) VALUES (%s)" % (columns,values)#建立sql語法
            cursor.execute(sql)

        # 執行
        conn.commit()
    
except Exception as ex:
    print("Exception:", ex)
    
end_time = time.time()#結束時間
alltime = end_time - start_time
print(f"{int(alltime//60)} 分 {int(alltime%60)} 秒導入資料庫")


# In[57]:


# for j in range(len(title_inf)):
#     print('時間戳記:',date_time[j])
#     print('專案:',title_inf[j])
#     print('專案網址:',title_href_inf[j])
#     print('募得金額:',price_inf[j])
#     print('金額達成率:',price_rate_inf[j])
#     print('贊助人數:',people_inf[j])
#     print('剩餘時間:',times_left_inf[j])
#     print('募資方案:',program_price_inf1[j])
#     print('方案贊助人數:',program_people_inf1[j])
#     print('實現時間:',realization_time_inf1[j])
#     print('專案更新次數:',updates_inf[j])


