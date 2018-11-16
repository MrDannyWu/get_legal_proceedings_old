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

#工具函数：用于请求页面并返回页面数据
def get_web_data(url):
    service_args = []
    service_args.append('--load-images=no')  ##关闭图片加载
    service_args.append('--disk-cache=yes')  ##开启缓存
    service_args.append('--ignore-ssl-errors=true')  ##忽略https错误
    warnings.filterwarnings('ignore')
    browser = webdriver.PhantomJS(service_args=service_args)
    web_data = None
    try:
        browser.get(url)
        web_data = browser.page_source
    except:
        print('请求错误！')
    return web_data

#def get_more_year():


def get_court_data(web_data):
    soup = BeautifulSoup(web_data,'lxml')
    court_list = soup.select('#myMenuID a')
    court_name_list = []
    court_url_list = []
    court_data = []
    for court in court_list:
        if  'href' in str(court):
            print(court.text,court.get('href'))
            court_name_list.append(court.text)
            court_url_list.append(court.get('href'))
            court_data.append([court.text,court.get('href')])
    #print(court_name_list)
    #print(court_url_list)
    #print(court_data)
    return court_data

def get_court_subclass(court_data):
    web_data = get_web_data(court_data[1])
    soup = BeautifulSoup(web_data,'lxml')
    subclass_list = soup.select('.ThemeXPTreeLevel1 a')
    subclass_name_list = []
    subclass_url_list = []
    subclass_data = []
    for court in subclass_list:
        if 'href' in str(court):
            #print(court.text, court.get('href'))
            subclass_name_list.append(court.text)
            subclass_url_list.append(court.get('href'))
            subclass_data.append([court_data[0], court.text, court.get('href')])
    #print(subclass_name_list)
    #print(subclass_url_list)
    #print(subclass_data)
    return subclass_data
def get_court_subclass_years(subclass_data):
    web_data = get_web_data(subclass_data[2])
    soup = BeautifulSoup(web_data,'lxml')
    years = soup.select('.ThemeXPTreeLevel1 .ThemeXPTreeLevel1 a')
    year_list = []
    year_url_list = []
    year_data = []
    for year in years:

        if 'href' in str(year):
            #print(court.text, court.get('href'))
            year_list.append(year.text)
            year_url_list.append(year.get('href'))
            # if 'Pre' in year.text:
            #     web_data1 = get_web_data(year.get('href'))
            #     soup1 = BeautifulSoup(web_data1, 'lxml')
            #     years1 = soup1.select('#JSCookTreeFolderClosed .ThemeXPFolderText a')
            #     year_list1 = []
            #     year_url_list1 = []
            #     year_data1 = []
            #     for year1 in years1:
            #         if 'href' in str(year1):
            #             year_list1.append(year1.text)
            #             year_url_list1.append(year1.get('href'))
            #             year_data1.append([subclass_data[0], subclass_data[1], year1.text, year1.get('href')])
            #             #print(year_data1)
            #     return year_data1
            # else:
            year_data.append([subclass_data[0], subclass_data[1], year.text, year.get('href')])
    #print("@@@@@@@@@@",year_data)
    if 'Pre' in str(year_data[-1][2]):
        web_data1 = get_web_data(year_data[-1][3])
        soup1 = BeautifulSoup(web_data1, 'lxml')
        years1 = soup1.select('.ThemeXPTreeLevel1 .ThemeXPTreeLevel1 #JSCookTreeFolderClosed .ThemeXPFolderText a')
        year_list1 = []
        year_url_list1 = []
        year_data1 = []
        for year1 in years1:
            if 'href' in str(year1):
                year_list1.append(year1.text)
                year_url_list1.append(year1.get('href'))
                year_data1.append([subclass_data[0], subclass_data[1], year1.text, year1.get('href')])
        return year_data1
    else:
        return year_data

                #print(year_data)
    #print(year_list)
    #print(year_url_list)
    #print(year_data)
    #return year_data
    # for i in year_data:
    #     if i[]

def get_details(year_data):
    web_data = get_web_data(year_data[3])
    soup = BeautifulSoup(web_data,'lxml')

    print()

url = 'https://legalref.judiciary.hk/lrs/common/ju/judgment.jsp'
web_data = get_web_data(url)
court_data = get_court_data(web_data)
for data in court_data:
    subclass_data = get_court_subclass(data)
    for data1 in subclass_data:
        data2 = get_court_subclass_years(data1)
        print(data2)
        # for each in data2:
        #     print('########',each[3])