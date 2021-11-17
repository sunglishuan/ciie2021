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

#改:之後要加上ua\
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
times_inf = []#募資時間
title_content_inf = []#專案內容
title_content_inf1 = []#專案內容
title_content_inf2 = []#專案內容
title_img_inf = []#專案圖片
title_img_inf1 = []#專案圖片
title_img_inf2 = []#專案圖片
title_img_inf3 = []#專案圖片
count_img_inf = []#專案圖片數
error_url = []#爬取網址
error_link = []#專案網站
error_name = []#提案人網站
error_name_plan = []#提案人發起計畫網頁
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
        category_inf.append('NA')
        name_inf.append('NA')
        name_href_inf.append('NA')
        price_target_inf.append('NA')
        times_inf.append('NA')
        title_content_inf2.append('NA')
        count_img_inf.append(0)
        title_img_inf3.append('NA')
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
            # print(item.text)

    category = browser.find_elements_by_xpath('//body/div/div/div/div/div/a[2]')#專案類別
    for item in category:
        if item:
            category_inf.append(item.text)
            # print(item.text)

    name = browser.find_elements_by_css_selector(".b.f6")#提案人
    for item in name:
        if item:
            name_inf.append(item.text)
            name_href_inf.append(item.get_attribute('href'))
            # print(item.text)

    price_target = browser.find_elements_by_xpath("//body/div/div/div/div/div/div[@class='f7']")#目標金額
    for item in price_target:
        if item:
            price_target_inf.append(item.text)
            # print(item.text)

    times = browser.find_elements_by_css_selector(".mb2.f7")#募資時間
    for item in times:
        if "時程" in item.text:
            times_inf.append(item.text)
            # print(item.text)

    title_content = browser.find_elements_by_xpath('//tbody/tr/td')#專案內容
    for item in title_content:
        title_content_inf.append(item.text)
    title_content_inf1.append(title_content_inf)
    title_content_inf = []#專案內容

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
for del_link in error_link:
    title_href_inf.remove(del_link)
#提案人網站
for link in name_href_inf:
    try:
        browser.get(link)

    except Exception as e:
        print("提案人網站：",e)#可看到錯誤是什麼
        error_name.append(link)
        name_int_inf.append('NA')
        name_web_inf2.append('NA')
        name_web_href_inf2.append('NA')
        name_spon_inf1.append('NA')
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
        print("提案人發起計畫網頁：",e)#可看到錯誤是什麼
        error_name_plan.append(link)
        name_plan_title_inf2.append('NA')
        name_plan_title_href_inf2.append('NA')
        name_plan_day_inf2.append('NA')
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

#整理
for item in title_content_inf1:
    if item != []:
        title_content_inf2.append(item)
    elif item == []:
        title_content_inf2.append("NA")

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
print(f"{int(alltime//60)} 分 {int(alltime%60)} 秒爬取")    


import json

data = []

for i in range(len(title_inf)): #將爬蟲內容轉成字典
    result0 = dict(date_time=date_time[i],
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
                   times=times_inf[i],
                   title_content=title_content_inf2[i],
                   count_img=count_img_inf[i],
                   title_img=title_img_inf3[i])
    data.append(result0)#存入list
#最終json
result={'error_url':error_url,'error_link':error_link,'error_name':error_name,'error_name_plan':error_name_plan,'data':data}

#存成json
now = datetime.now() #載入現在時間點
now = now.strftime("%Y%m%d_%H%M") #調整時間格式
print("存成json檔",now)

fn = f'./lotsFix/zeczec_fix_{now}.json'
with open(fn, 'w', encoding='utf-8') as fnresult:
    json.dump(result,fnresult,ensure_ascii=False)
    

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
changelist = ['name_web','name_web_url','name_spon','name_plan_title','name_plan_title_url','name_plan_day','title_content','title_img']

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
            sql = "INSERT INTO fix (%s) VALUES (%s)" % (columns,values)#建立sql語法
            cursor.execute(sql)

        # 執行
        conn.commit()
    
except Exception as ex:
    print("Exception:", ex)
    
end_time = time.time()#結束時間
alltime = end_time - start_time
print(f"{int(alltime//60)} 分 {int(alltime%60)} 秒導入資料庫")

now = datetime.now() #載入現在時間點
now = now.strftime("%Y%m%d_%H%M") #調整時間格式
print(f"FINISH {now}")


# In[ ]:


# for j in range(len(title_inf)):
#     print('時間戳記:',date_time[j])
#     print('專案:',title_inf[j])
#     print('專案網址:',title_href_inf[j])
#     print('專案類別:',category_inf[j])
#     print('提案人:',name_inf[j])
#     print('提案人網址:',name_href_inf[j])
#     print('提案人介紹:',name_int_inf[j])
#     print('提案人網站平台:',name_web_inf2[j])
#     print('提案人網站平台網址:',name_web_href_inf2[j])
#     print('提案人贊助資訊與加入天數:',name_spon_inf1[j])
#     print('提案人發起計畫專案:',name_plan_title_inf2[j])
#     print('提案人發起計畫專案網址:',name_plan_title_href_inf2[j])
#     print('提案人發起計畫專案及日期:',name_plan_day_inf2[j])
#     print('目標金額:',price_target_inf[j])
#     print('募資時間:',times_inf[j])
#     print('專案內容:',title_content_inf2[j])
#     print('專案圖片數:',count_img_inf[j])
#     print('專案圖片:',title_img_inf3[j])



# In[ ]:
