from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Sum
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, City, Country
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
# detail is 1, list is all
# Create your views here.

#def home(request):
#    return render(request,'home.html', {})
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
    driver = selenium.webdriver.Chrome(executable_path=r'C:\chromedriver.exe', options=opts)
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
    sheet1.write(0, 10, "Comment Text")
    kb.save('Youtube.csv')
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
            kb.save('Youtube.csv')
            mi = mi + 1
    
    for span2 in commentdate:
        #    print(span.text)
            sheet1.write(mi2, 1, span2.text)
            kb.save('Youtube.csv')
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
    opts.add_argument("user-agent=Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166")
    #opts.add_argument('headless')
    driver = selenium.webdriver.Chrome(executable_path=r'C:\chromedriver.exe', options=opts)
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
    sheet1.write(0, 10, "Comment Text")
    kb.save('Facebook.xls')
    mi = 1
    mi2 = 1
    login = driver.find_element_by_xpath("//span[text()='Log In']")
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



def line_chart(request):
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

def population_chart(request):
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


def pie_chart(request):
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
    return render(request,'dashboard.html', {})

def home(request):
    return render(request,'dashboard.html', {})


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