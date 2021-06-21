from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Sum
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, City, Country, SentData
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from django.db.models import Count
import os
    
import pandas as pd

from theblog.preprocessing import * 
from theblog.model import *
from collections import Counter
import matplotlib.pyplot as plt

# detail is 1, list is all
# Create your views here.

def startanalysis(request):
    
   
    # import pandas as pd

    # Filename = filename.csv

    # importing data
    try:
        df = pd.read_excel('Facebook.xls')
    except:
        try:
            df = pd.read_excel('Twitter.xls')
        except:
            try:
                df = pd.read_excel('Youtube.xls')
            except:
                print(".")
    
    
        
    df = df.astype(str)
    print('File Imported')

    # Preprcoessing
    print('\nPreprocessing Started')
    df_2 = proceprocessData(df)
    df_2['text_lemmatized'] = df_2['Content'].apply(lambda text: lemmatize_words(text))
    print('Preprocessing End')

    filter_df = df_2[['text_lemmatized']]
    filter_df = filter_df.astype(str)
    filter_df.drop_duplicates(keep='first', inplace=True)


    # prediction
    Prediction = prediction(filter_df)
    filter_df['Sentiment'] = Prediction
    filter_df.to_excel('label.xls', index=False)


    import xlrd
    from itertools import islice
    # Give the location of the file
    loc = ("label.xls")
    
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    
   
    #temp5 = request.user
    
    # Comment = SentData.objects.create(comment='temp5')
    # Date =  SentData.objects.create(date='temp5')
    # Sentiment = SentData.objects.create(sentiment='temp5')
    # OwnerData = SentData.objects.create(ownerData='temp5')
    # Owner = SentData.objects.create(owner=request.user)
    from datetime import datetime

    # datetime object containing current date and time
    now = datetime.now()
    
    #print("now =", now)

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    #print("date and time =", dt_string)

    sentdata = {}
    df = pd.read_excel('label.xls')  
    #for i in range(0,2):
    i = 1
    # while(sheet.cell_value(i, 0) != None):
    
    for i in range(0 ,df['text_lemmatized'].size):
        sentdata[i] = SentData()
        sentdata[i].comment = df['text_lemmatized'][i]
        sentdata[i].date = dt_string
        sentdata[i].sentiment = df['Sentiment'][i]
        sentdata[i].ownerData = request.user.email + dt_string
        sentdata[i].owner = request.user
        sentdata[i].save()
    #    i = i + 1
    try:
        os.remove("Facebook.xls")
    except:
        try:
            os.remove("Twitter.xls")
        except:
            try:
                os.remove("Youtube.xls")
            except:
                print(".")
    

    return render(request,'dashboard.html', {'temp8' : df['text_lemmatized'].size})


def youtube(request):
    from selenium import webdriver
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.chrome.options import Options
    from xlwt import Workbook
    from xlwt import XFStyle,Borders, Pattern, Font, easyxf
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.common.exceptions import TimeoutException
    from xlrd import open_workbook
    import time
    from datetime import date
    import json
    import selenium.webdriver
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import StaleElementReferenceException
    from multiprocessing import Process
    import sys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys

    start_time = time.time()
    opts = selenium.webdriver.ChromeOptions()
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument("--disable-extensions")
    opts.add_argument("--proxy-server='direct://'")
    opts.add_argument("--proxy-bypass-list=*")
    opts.add_argument("--start-maximized")
    #opts.add_argument('--headless')
    opts.add_argument('--disable-gpu')
    opts.add_argument('--disable-dev-shm-usage')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--ignore-certificate-errors')
    opts.add_argument('--allow-running-insecure-content')
    opts.add_argument("--mute-audio")
    #driver = selenium.webdriver.Chrome(executable_path=r'C:\chromedriver.exe', options=opts)
    driver = selenium.webdriver.Chrome('chromedriver.exe', options=opts)
    
    #driver = selenium.webdriver.Chrome(executable_path=r'C:\chromedriver.exe')

    #driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')

    postLink2 = request.POST.get("postlink2")
    postCount2 = int(request.POST.get("postCount2"))
    #postLink = postLink.replace("https://www.", "https://mbasic.")

    #driver.get("https://www.youtube.com/watch?v=nfWlot6h_JM")
    driver.get(postLink2)

    driver.maximize_window()
    driver.execute_script("window.scrollTo(-1000, document.body.scrollHeight);")

    kb = Workbook()
    # add_sheet is used to create sheet.
    sheet1 = kb.add_sheet('Sheet 1', cell_overwrite_ok=True)
    print(" WORKSHEET CREATED SUCCESSFULLY!")
    print(" ")
    # INITIALIZING THE COLOUMN NAMES NOW
    sheet1.write(0, 0, "Post No")
    sheet1.write(0, 1, "Date Of Post")
    sheet1.write(0, 2, "Text Of Post")
    sheet1.write(0, 3, "Likes")
    sheet1.write(0, 4, "Comments")
    sheet1.write(0, 5, "Shares")
    sheet1.write(0, 6, "Comment No")
    sheet1.write(0, 7, "Name Of Commenter")
    sheet1.write(0, 8, "Comment Likes")
    sheet1.write(0, 9, "Comment Replies")
    sheet1.write(0, 10, "Content")
    kb.save('Youtube.xls')
    mi = 1
    mi2 = 1
    #login = driver.find_element_by_id("yt-simple-endpoint style-scope ytd-button-renderer")

    #ActionChains(driver).move_to_element(login).click().perform()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[@class='style-scope ytd-button-renderer style-suggestive size-small' and @id='text']"))).click()
    time.sleep(3)
    driver.implicitly_wait(10)

    try:
        username = driver.find_element_by_xpath("//div[@class='Xb9hP']/input[1]")
        username.clear()
        username.send_keys("k173860@nu.edu.pk")
        username.send_keys(Keys.RETURN)
    except:
        username = driver.find_element_by_xpath("//input[@id='Email']")
        username.clear()
        username.send_keys("k173860@nu.edu.pk")
        username.send_keys(Keys.RETURN)

    #login = driver.find_element_by_xpath("//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc lw1w4b']").click()
    #ActionChains(driver).move_to_element(login).click().perform()
    time.sleep(3)
    driver.implicitly_wait(10)

    try:
        password = driver.find_element_by_xpath("//input[@class='whsOnd zHQkBf' and @name='password']")
        #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='whsOnd zHQkBf' and @name='password']"))).click()

        password.clear()
        password.send_keys("ZEDZEPHYR")
        password.send_keys(Keys.RETURN)
    except:
        password = driver.find_element_by_xpath("//input[@type='password']")
        password.clear()
        password.send_keys("ZEDZEPHYR")
        password.send_keys(Keys.RETURN)


    #SEARCH_INPUT2 = (By.XPATH, "//div[@class='kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql']")

    # all_spans = driver.find_elements_by_xpath("//div[@class='ecm0bbzt e5nlhep0 a8c37x1j']/span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh oo9gr5id']/div[@class='kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql']")
    # for span in all_spans:
    #     sheet1.write(mi, 10, span.text)
    #     kb.save('main.xls')
    #     mi = mi + 1

    #demo = driver.find_element_by_xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v lrazzd5p m9osqain']")
    #demo = driver.find_element_by_xpath("//a[text()='&nbsp;View more comments…']")       

    #ActionChains(driver).move_to_element(demo).click().perform()
    #demo.click()
    #ActionChains(driver).move_to_element(demo).click().perform()

    #demo.send_keys(Keys.RETURN)

    # gotocheckoutusingsidebarcart = (By.XPATH, "//div[@class='ec ew']")
    # search_input = driver.find_element(gotocheckoutusingsidebarcart)
    # search_input.send_keys(Keys.RETURN)
    cnt = 1
    temp = 0
    time.sleep(5)
    driver.implicitly_wait(20)
    driver.refresh()

    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #driver.execute_script("window.scrollTo(100, document.body.scrollHeight);")
    #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    #stop = driver.find_element_by_xpath("//div[@class='style-scope ytd-watch-flexy' and @id='player']")
    #stop.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='style-scope ytd-watch-flexy' and @id='player']"))).click()
    #driver.find_element_by_tag_name('html').send_keys(Keys.END)
    #driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)


    # for i in range(0,5):
    #     driver.execute_script("window.scrollTo(0,Math.max(document.documentElement.scrollHeight,document.body.scrollHeight,document.documentElement.clientHeight))")
    #     time.sleep(10)



    #driver.execute_script("window.scrollTo(100,document.body.scrollHeight)")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 500)") 

    #driver.find_element_by_tag_name('ytd-video-primary-info-renderer').send_keys(Keys.END)

    #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//paper-button[@class='style-scope ytd-button-renderer style-text size-default' and @id='button']"))).click()

    #driver.find_element_by_xpath("//div[@class='style-scope ytd-comment-simplebox-renderer' and @id='comment-dialog']").send_keys(Keys.END)

    #driver.execute_script("window.scrollTo(100, document.body.scrollHeight);")
    #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    #for i in range(1000):

        #search_input = driver.find_elements_by_xpath("//div[1]/div[1]/div[@class='_680y']/div[@class='_6cuy']/div[@class='b3i9ofy5 e72ty7fz qlfml3jp inkptoze qmr60zad rq0escxv oo9gr5id q9uorilb kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x d2edcug0 jm1wdb64 l9j0dhe7 l3itjdph qv66sw1b']/div[@class='tw6a2znq sj5x9vvc d1544ag0 cxgpxx05']/div[@class='ecm0bbzt e5nlhep0 a8c37x1j']/span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh oo9gr5id']/div[@class='kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql']")
    #search_input = driver.find_elements_by_xpath("//div[@class='style-scope ytd-expander']/yt-formatted-string[2]")
    time.sleep(2)
    driver.find_element_by_tag_name('html').send_keys(Keys.END)


    for i in range(0,postCount2): 
        search_input = driver.find_elements_by_xpath("//yt-formatted-string[@class='style-scope ytd-comment-renderer' and @id='content-text']")
        commentdate = driver.find_elements_by_xpath("//yt-formatted-string[@class='published-time-text above-comment style-scope ytd-comment-renderer']/a[@class='yt-simple-endpoint style-scope yt-formatted-string' and @spellcheck='false' and @dir='auto']")
   

        driver.find_element_by_tag_name('html').send_keys(Keys.END)
        temp = temp + 1

    for span in search_input:
        #    print(span.text)
            sheet1.write(mi, 10, span.text)
            kb.save('Youtube.xls')
            mi = mi + 1
    
    for span2 in commentdate:
        #    print(span.text)
            sheet1.write(mi2, 1, span2.text)
            kb.save('Youtube.xls')
            mi2 = mi2 + 1
            print(mi2)

    print(temp)
    #for span in search_input:
    #    print(span.text)
            #sheet1.write(mi, 10, span.text)
        #     kb.save('youtube.xls')
        #     #mi = mi + 1

        #     temp = temp + 1

        # print(temp)
            
        # print("time elapsed: {:.2f}s".format(time.time() - start_time))

        #uncomment the following 3
        #time.sleep(5)
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #driver.implicitly_wait(20)
            


    #print(search_input.text)

    print("time elapsed: {:.2f}s".format(time.time() - start_time))

    driver.close() 
    driver.quit()
    tme2 = time.time() - start_time
    temp2 = temp

    return render(request,'dashboard.html', {'temp2': temp2, 'time2': tme2, 'postLink2': postLink2, 'speed2': float(temp2/tme2)})
    
def facebook(request):
    from selenium import webdriver
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.chrome.options import Options
    from xlwt import Workbook
    from xlwt import XFStyle,Borders, Pattern, Font, easyxf
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.common.exceptions import TimeoutException
    from xlrd import open_workbook
    import time
    from datetime import date
    import json
    import selenium.webdriver
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import StaleElementReferenceException
    from multiprocessing import Process
    import sys
    from fake_useragent import UserAgent


    start_time = time.time()
    #chrome_options = Options()
    ua = UserAgent()
    userAgent = ua.random                                     #THIS IS FAKE AGENT IT WILL GIVE YOU NEW AGENT EVERYTIME
    #print(userAgent)
    #headers = {'User-Agent': userAgent}
    opts = selenium.webdriver.ChromeOptions()
    
    prefs = {
        "translate_whitelists": {"ur":"en"},
        "translate":{"enabled":"true"}
    }
    opts.add_experimental_option("prefs", prefs)
    opts.add_argument("--lang=en")
    opts.add_argument("user-agent=Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166")
    #opts.add_argument('headless')
    
    #driver = selenium.webdriver.Chrome(executable_path=r'C:\chromedriver.exe', options=opts)

    driver = selenium.webdriver.Chrome('chromedriver.exe', options=opts)
    #driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
    #driver = selenium.webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
    
    postLink = request.POST.get("postlink")
    postCount = request.POST.get("postCount")
    postLink = postLink.replace("https://www.", "https://mbasic.")

    #driver.get("https://mbasic.facebook.com/bbcnews/posts/10158670908802217")
    driver.get(postLink)
    
    driver.maximize_window()

    kb = Workbook()
    # add_sheet is used to create sheet.
    sheet1 = kb.add_sheet('Sheet 1', cell_overwrite_ok=True)
    print(" WORKSHEET CREATED SUCCESSFULLY!")
    print(" ")
    # INITIALIZING THE COLOUMN NAMES NOW
    sheet1.write(0, 0, "Post No")
    sheet1.write(0, 1, "Date Of Post")
    sheet1.write(0, 2, "Text Of Post")
    sheet1.write(0, 3, "Likes")
    sheet1.write(0, 4, "Comments")
    sheet1.write(0, 5, "Shares")
    sheet1.write(0, 6, "Comment No")
    sheet1.write(0, 7, "Name Of Commenter")
    sheet1.write(0, 8, "Comment Likes")
    sheet1.write(0, 9, "Comment Replies")
    sheet1.write(0, 10, "Content")
    kb.save('Facebook.xls')
    mi = 1
    mi2 = 1
    try:
        login = driver.find_element_by_xpath("//span[text()='Log In']")
    except:
             login = driver.find_element_by_xpath("//a[text()='صفحہ اول پر جائیں']")
   
    ActionChains(driver).move_to_element(login).click().perform()
    time.sleep(3)
    driver.implicitly_wait(10)

    username = driver.find_element_by_id("m_login_email")
    username.clear()
    username.send_keys("k173860@nu.edu.pk")

    password = driver.find_element_by_name("pass")
    password.clear()
    password.send_keys("B@efbcwfpiimrzfv1")

    driver.find_element_by_name("login").click()
    driver.get(postLink)
    #SEARCH_INPUT2 = (By.XPATH, "//div[@class='kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql']")

    # all_spans = driver.find_elements_by_xpath("//div[@class='ecm0bbzt e5nlhep0 a8c37x1j']/span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh oo9gr5id']/div[@class='kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql']")
    # for span in all_spans:
    #     sheet1.write(mi, 10, span.text)
    #     kb.save('main.xls')
    #     mi = mi + 1

    #demo = driver.find_element_by_xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v lrazzd5p m9osqain']")
    #demo = driver.find_element_by_xpath("//a[text()='&nbsp;View more comments…']")       

    #ActionChains(driver).move_to_element(demo).click().perform()
    #demo.click()
    #ActionChains(driver).move_to_element(demo).click().perform()

    #demo.send_keys(Keys.RETURN)

    # gotocheckoutusingsidebarcart = (By.XPATH, "//div[@class='ec ew']")
    # search_input = driver.find_element(gotocheckoutusingsidebarcart)
    # search_input.send_keys(Keys.RETURN)
    cnt = 1
    temp = 0
    postCount.replace('"', '')
    postCount = int(postCount)
    for i in range(0, int(postCount/10)):

        #search_input = driver.find_elements_by_xpath("//div[1]/div[1]/div[@class='_680y']/div[@class='_6cuy']/div[@class='b3i9ofy5 e72ty7fz qlfml3jp inkptoze qmr60zad rq0escxv oo9gr5id q9uorilb kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x d2edcug0 jm1wdb64 l9j0dhe7 l3itjdph qv66sw1b']/div[@class='tw6a2znq sj5x9vvc d1544ag0 cxgpxx05']/div[@class='ecm0bbzt e5nlhep0 a8c37x1j']/span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh oo9gr5id']/div[@class='kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql']")
        #search_input = driver.find_elements_by_tag_name('div')
        
        search_input = driver.find_elements_by_xpath("//div/h3/following-sibling::div[1]")
        #search_input = driver.find_elements_by_xpath("//div/h3/following-sibling::div[1]")
        commentdate = driver.find_elements_by_xpath("//h3/following-sibling::div[3]/abbr")
    
        for span in search_input:
            #print(span.text)
            sheet1.write(mi, 10, span.text)
            kb.save('Facebook.xls')
            mi = mi + 1

            temp = temp + 1
            
        for span2 in commentdate:
            #    print(span.text)
                sheet1.write(mi2, 1, span2.text)
                kb.save('Facebook.xls')
                mi2 = mi2 + 1
                print(mi2)
        
        print(temp)
        
        #time.sleep(1)
        
        if cnt == 1:
            try:
                demo = driver.find_elements_by_xpath("//img[@width='16' and @height='16']")
                #demo = driver.find_element_by_xpath("//a[text()='View more comments…']")       
                #ActionChains(driver).move_to_element(demo).click().perform()
                demo[-1].click()
            
                #driver.execute_script("arguments[0].click();", demo)
                #demo.click()
                cnt = cnt + 1
            except:
                break
        else:
            try:
                demo = driver.find_elements_by_xpath("(//img[@width='16' and @height='16'])")
                demo[-1].click()
            except:
                break
            #ActionChains(driver).move_to_element(demo).click().perform()
            #driver.execute_script("arguments[0].click();", demo)
            
            #demo.click()
        print("time elapsed: {:.2f}s".format(time.time() - start_time))

        #uncomment the following 3
        #time.sleep(5)
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #driver.implicitly_wait(20)
            


    #print(search_input)
    #search_input = driver.find_element_by_xpath("//div[2]/div[1]/div[@class='_680y']/div[@class='_6cuy']/div[@class='b3i9ofy5 e72ty7fz qlfml3jp inkptoze qmr60zad rq0escxv oo9gr5id q9uorilb kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x d2edcug0 jm1wdb64 l9j0dhe7 l3itjdph qv66sw1b']/div[@class='tw6a2znq sj5x9vvc d1544ag0 cxgpxx05']/div[@class='ecm0bbzt e5nlhep0 a8c37x1j']/span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh oo9gr5id']/div[1]")
    #print(search_input.text)
        
        #print(span.text)
    #demo = driver.find_element(SEARCH_INPUT2)
    #assert search_input.text == "I found this baby kraken, is it yours?"


    #driver.implicitly_wait(10)
    #time.sleep(3)

    print("time elapsed: {:.2f}s".format(time.time() - start_time))

    driver.close() 
    driver.quit()
    tme = time.time() - start_time
    return render(request,'dashboard.html', {'temp': temp, 'time': tme, 'postLink': postLink, 'speed': float(temp/tme)})
    
    #return render(request,'dashboard.html', {'temp': temp, 'time': tme })


def twitter(request):
    from selenium import webdriver
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.chrome.options import Options
    from xlwt import Workbook
    from xlwt import XFStyle,Borders, Pattern, Font, easyxf
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.common.exceptions import TimeoutException
    from xlrd import open_workbook
    #asdnasdj
    import time
    from datetime import date
    import json
    import selenium.webdriver
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import StaleElementReferenceException
    from multiprocessing import Process
    import sys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys

    start_time = time.time()
    postLink3 = request.POST.get("postlink3")
    date_since = request.POST.get("postCount3")

    postCount3 = request.POST.get("postCount4")
    
    
    kb = Workbook()
    # add_sheet is used to create sheet.
    sheet1 = kb.add_sheet('Sheet 1', cell_overwrite_ok=True)
    print(" WORKSHEET CREATED SUCCESSFULLY!")
    print(" ")
    # INITIALIZING THE COLOUMN NAMES NOW
    sheet1.write(0, 0, "Post No")
    sheet1.write(0, 1, "Date Of Post")
    sheet1.write(0, 2, "Text Of Post")
    sheet1.write(0, 3, "Likes")
    sheet1.write(0, 4, "Comments")
    sheet1.write(0, 5, "Shares")
    sheet1.write(0, 6, "Comment No")
    sheet1.write(0, 7, "Name Of Commenter")
    sheet1.write(0, 8, "Comment Likes")
    sheet1.write(0, 9, "Comment Replies")
    sheet1.write(0, 10, "Content")
    kb.save('Twitter.xls')
    mi = 1
    mi2 = 1
    #login = driver.find_element_by_id("yt-simple-endpoint style-scope ytd-button-renderer")

    #Twitter Api
    APIkey = "PMCVuv8IoBYZsfE5NC9iTAVUq"

    APIsecretkey = "5LQ00BLIowonJNI4O3iNjQDsO73zTU4RA9jU0P48qYHtKXQ9Sr"

    Bearertoken = "AAAAAAAAAAAAAAAAAAAAAOq1NQEAAAAA9D9%2Ff8KaNepiMlfE391KUWnOx5E%3Df3A5vL1P4b5oQCujLuQej6XGfLcdKI8PayRp3BNCIvX3YYdlzn"

    APPID = "20297194"

    Accesstoken = "1178293129734217728-BjQJpZj1hGcWeXMxT4jukac3zsepaA"

    Accesstokensecret = "7KvGcqa1rRIu8yXiBK8wyETyjWq1F2HPIU0gS70Ywq245"


    consumer_key= 'PMCVuv8IoBYZsfE5NC9iTAVUq'
    consumer_secret= '5LQ00BLIowonJNI4O3iNjQDsO73zTU4RA9jU0P48qYHtKXQ9Sr'
    access_token= '1178293129734217728-BjQJpZj1hGcWeXMxT4jukac3zsepaA'
    access_token_secret= '7KvGcqa1rRIu8yXiBK8wyETyjWq1F2HPIU0gS70Ywq245'
    #twurl -X GET "/labs/2/tweets/1138505981460193280?expansions=attachments.media_keys&tweet.fields=created_at,author_id,lang,source,public_metrics,context_annotations,entities"

    import os
    import tweepy as tw
    import pandas as pd
    import csv


    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    # Define the search term and the date_since date as variables
    search_words = postLink3
    
    tweets = tw.Cursor(api.search,
                q=search_words,
                lang="en",
                since=date_since).items(postCount3)

    cnt = 1
    temp = 0
    for tweet in tweets:
        #print("[---" +tweet.text + "---]\n")
        sheet1.write(mi, 10, tweet.text)
        date = (str(tweet.author.created_at).split(' '))
        sheet1.write(mi2, 1, date[0])
        kb.save('Twitter.xls')
        mi = mi + 1
        mi2 = mi2 + 1
        temp = temp + 1
            
        #print(tweet.created_at)
        #print('\n')
        
    
    #[tweet.text for tweet in tweets]


    tme3 = time.time() - start_time
    temp3 = temp

    return render(request,'dashboard.html', {'temp3': temp3, 'time3': tme3, 'postLink3': postLink3, 'speed3': float(temp3/tme3)})


def line_chart(request):

    labels = []
    data = []

    #queryset = SentData.objects.order_by('-sentiment')[:5]

    queryset = SentData.objects.filter(sentiment="What about those who drive")
    count = SentData.objects.values('sentiment').distinct().count()
    p = SentData.objects.values('sentiment').distinct().filter(owner=request.user)
    q = 0

    #q = SentData.objects.values('optional_first_name').annotate(c=Count('optional_first_name')).order_by('-c')
    cnt = 0
    for i in p:
        labels.append(i['sentiment'])
        q = SentData.objects.filter(sentiment=i['sentiment']).filter(owner=request.user).count()
        data.append(q)
   

    return render(request, 'line_chart.html', {
        'labels': labels,
        'data': data,
        'count' : count,
        'p' : len(p),
        'q' : q,
        'object_list': 2
      
    })

def population_chart(request):
    labels = []
    data = []

    #queryset = SentData.objects.order_by('-sentiment')[:5]

    queryset = SentData.objects.filter(sentiment="What about those who drive")
    count = SentData.objects.values('sentiment').distinct().count()
    p = SentData.objects.values('sentiment').distinct().filter(owner=request.user)
    q = 0

    #q = SentData.objects.values('optional_first_name').annotate(c=Count('optional_first_name')).order_by('-c')
    cnt = 0
    for i in p:
        labels.append(i['sentiment'])
        q = SentData.objects.filter(sentiment=i['sentiment']).filter(owner=request.user).count()
        data.append(q)
   

    return render(request, 'population_chart.html', {
        'labels': labels,
        'data': data,
        'count' : count,
        'p' : len(p),
        'q' : q,
        'object_list': 2
      
    })

def pie_chart(request):
    labels = []
    data = []

    labels2 = []
    data2 = []

    #queryset = SentData.objects.order_by('-sentiment')[:5]

    queryset = SentData.objects.filter(sentiment="What about those who drive")
    count = SentData.objects.values('sentiment').distinct().count()
    p = SentData.objects.values('sentiment').distinct().filter(owner=request.user, date="21/06/2021 13:04:36")
    
    count2 = SentData.objects.values('date').distinct().count()
    p2 = SentData.objects.values('date').distinct().filter(owner=request.user)
    

    #q = SentData.objects.values('optional_first_name').annotate(c=Count('optional_first_name')).order_by('-c')
    
    for i in p:
        labels.append(i['sentiment'])
        q = SentData.objects.filter(sentiment=i['sentiment']).filter(owner=request.user, date="21/06/2021 13:04:36").count()
        data.append(q)

    for i2 in p2:
        labels2.append(i2['date'])
        q2 = SentData.objects.filter(date=i2['date']).filter(owner=request.user).count()
        data2.append(q2)

    d = dict()
    d['set1'] = labels
    d['set2'] = labels
    # for city in queryset:
    #     #labels.append(city.sentiment) 
    #     data.append(count[city])

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
        'count' : count,
        'p' : len(p),
        'q' : q,
        'object_list': 2,
        'd' : d,
        'labels2': labels2,
        'data2': data2,

    })

#def line_chart(request):
    labels = []
    data = []

    queryset = City.objects.values('country__name').annotate(country_population=Sum('population')).order_by('-country_population')
    for entry in queryset:
        labels.append(entry['country__name'])
        data.append(entry['country_population'])
    
    #return JsonResponse(data={
    #    'labels': labels,
    #    'data': data,
    #})
    return render(request, 'line_chart.html', {
        'labels': labels,
        'data': data,
    })

#def population_chart(request):
    labels = []
    data = []

    queryset = City.objects.values('country__name').annotate(country_population=Sum('population')).order_by('-country_population')
    for entry in queryset:
        labels.append(entry['country__name'])
        data.append(entry['country_population'])
    
    #return JsonResponse(data={
    #    'labels': labels,
    #    'data': data,
    #})
    return render(request, 'population_chart.html', {
        'labels': labels,
        'data': data,
    })
 
#def pie_chart(request):
    labels = []
    data = []

    queryset = City.objects.order_by('-population')[:10]
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })   

def dashboard(request):
    dates = SentData.objects.values('date').distinct().filter(owner=request.user)
    return render(request,'dashboard.html', {'dates':dates})

def home(request):
    dates = SentData.objects.values('date').distinct().filter(owner=request.user)
    return render(request,'dashboard.html', {'dates':dates})

def addsent(request):
        
    import xlrd
    from itertools import islice
    # Give the location of the file
    loc = ("Facebook.xls")
    
    # To open Workbook
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    
    # For row 0 and column 0
    #print(sheet.cell_value(1, 10))
    temp5 = sheet.cell_value(3, 10)
    #temp5 = request.user
    
    # Comment = SentData.objects.create(comment='temp5')
    # Date =  SentData.objects.create(date='temp5')
    # Sentiment = SentData.objects.create(sentiment='temp5')
    # OwnerData = SentData.objects.create(ownerData='temp5')
    # Owner = SentData.objects.create(owner=request.user)
    sentdata = {}
    for i in range(0,2):
        sentdata[i] = SentData()
        sentdata[i].comment = sheet.cell_value(5, 10)
        sentdata[i].date = sheet.cell_value(5, 10)
        sentdata[i].sentiment = sheet.cell_value(5, 10)
        sentdata[i].ownerData = request.user.email
        sentdata[i].owner = request.user
        
        sentdata[i].save()
        
 
    
    return render(request,'dashboard.html', {'temp5':temp5})

# class HomeView(ListView):
#     model = Post
#     template_name = "home.html"
#     #ordering = ['-id']
#     ordering = ['-post_date']

#     #def get_context_date(self, *args, **kwargs):




def CategoryView(request, cats):
    category_posts = Post.objects.filter(category = cats.replace('-', ' '))
    return render(request,'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts' :category_posts})

class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    #fields = "__all__"
    #fields = ('title', 'body')

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = "add_category.html"
    fields = "__all__"
    #fields = ('title', 'body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
   
    template_name = 'update_post.html'
    #fields = ('title', 'title_tag', 'body')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')