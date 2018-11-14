import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import warnings

# def get_court_url(url):
#     web_data = None
#     try:
#         web_data = requests.get(url)
#     except:
#         print('请求错误！')
#     print(web_data)
#
#     soup = BeautifulSoup(web_data.text,'lxml')
#     script_datas = soup.select('script')
#     for script in script_datas:
#         if 'var myMenu =' in str(script):
#             #dada_list = []
#             data_list = script.text.split('var myMenu =')[-1].split(';')[0].replace('\n','').replace(' ','').split(',')
#             #print(data_list)
#
#             for data in data_list:
#                 print(data)
#     court_urls = soup.select('a span')
#     # for court_url in court_urls:
#     #     print(court_url)
# url = 'https://legalref.judiciary.hk/lrs/common/ju/judgment.jsp'
# get_court_url(url)

def get_web_data(url):
    warnings.filterwarnings('ignore')
    browser = webdriver.PhantomJS()
    web_data = None
    try:
        browser.get(url)
        web_data = browser.page_source
    except:
        print('请求错误！')
    return web_data

def get_court_url(web_data):
    soup = BeautifulSoup(web_data,'lxml')
    court_list = soup.select('#myMenuID a')
    court_name_list = []
    court_url_list = []
    for court in court_list:
        if  'href' in str(court):
            print(court.text,court.get('href'))
            court_name_list.append(court.text)
            court_url_list.append(court.get('href'))
    #print(court_name_list)
    #print(court_url_list)
    return court_url_list

def get_court_subclass(web_data):
    soup = BeautifulSoup(web_data,'lxml')
    subclass_list = soup.select('.ThemeXPTreeLevel1 a')
    subclass_name_list = []
    subclass_url_list = []
    for court in subclass_list:
        if 'href' in str(court):
            #print(court.text, court.get('href'))
            subclass_name_list.append(court.text)
            subclass_url_list.append(court.get('href'))
    print(subclass_name_list)
    print(subclass_url_list)
    return subclass_url_list
def get_court_subclass_years(web_data):
    soup = BeautifulSoup(web_data,'lxml')
    years = soup.select('.ThemeXPTreeLevel1 .ThemeXPTreeLevel1 a')
    year_list = []
    year_url_list = []
    for year in years:
        if 'href' in str(year):
            #print(court.text, court.get('href'))
            year_list.append(year.text)
            year_url_list.append(year.get('href'))
    print(year_list)
    print(year_url_list)

url = 'https://legalref.judiciary.hk/lrs/common/ju/judgment.jsp'
web_data = get_web_data(url)
court_url_list = get_court_url(web_data)
for court_url in court_url_list:
    web_data1 = get_web_data(court_url)
    subclass_url_list = get_court_subclass(web_data1)
    for subclass_url in subclass_url_list:
        web_data2 = get_web_data(subclass_url)
        get_court_subclass_years(web_data2)