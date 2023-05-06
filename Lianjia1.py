import requests
from bs4 import BeautifulSoup
from lxml import etree
import time
import random
import pandas as pd

qu = ['jinjiang', 'wuhou', 'gaoxin7', 'qingyang', 'jinniu', 'chenghua', 'tianfuxinqu', 'gaoxinxi1', 'shuangliu', 'wenjiang', 'pidou', 'longquanyi', 'xindou', 'tianfuxinqunanqu', 'qingbaijiang']
xiaoqu_list, tihubili_list, peibeidianti_list, guapai_list, last_deal_list, ownership_list, use_list, years_list, plege_list, check_code_list, indate_list, traffic_list, unit_price_list = [], [], [], [], [], [], [], [], [], [], [], [], []
qu_name = ['锦江区', '武侯区', '高新区', '青羊区', '金牛区', '成华区', '天府新区', '高新西区', '双流区', '温江区', '郫都区', '龙泉驿区', '新都区', '天府新区南区', '青白江区']

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
ip = {
        'http':'61.216.156.222'
        # 'http': '112.194.88.136'
    }
# 1. 发出请求，获取源码
def get_intro():
    for i in range(0, len(qu)):  # 属于哪个区
        print('现在爬取的是{}区的数据'.format(qu[i]))
        house_links = []  # 创建一个空列表，用于保存所有房源的详情页链接
        for j in range(1, 6):  # 页数
            url = 'https://cd.lianjia.com/ershoufang/' + qu[i] + '/pg' + str(j)
            # print(url)
            r = requests.get(url, headers=headers, proxies=ip).text
            soup = BeautifulSoup(r, 'html.parser')
            house_tag = soup.find_all('a', class_='noresultRecommend img LOGCLICKDATA')
            if house_tag:
                for tag in house_tag:
                    house_link = tag.get('href')
                    # print(house_link)
                    if not house_link:
                        continue
                    house_links.append(house_link)
            else:
                continue
            for house_link in house_links:
                if not house_link:
                    continue
                try:
                    detail_r = requests.get(house_link, headers=headers, proxies=ip).text
                except Exception as e:
                    print(f"获取房屋详情失败：{e}")
                    detail_r = None
                if detail_r is not None:
                    get_detail_content(detail_r)

    # res = requests.get(url, headers=headers, proxies=ip)
    # respone = res.content

    # return respone

# 2. 数据提取



def get_detail_content(detail_r):
    detail_soup = BeautifulSoup(detail_r, 'html.parser')
    xiaoqu_tag = detail_soup.select_one('.communityName .info')
    if xiaoqu_tag:
        xiaoqu_list.append(xiaoqu_tag.text)
        # print(xiaoqu_tag.text)
    else:
        xiaoqu_list.append('')

    tihubili_tag = detail_soup.select('.base .content ul li')
    if len(tihubili_tag) > 9:
        tihubili = tihubili_tag[9].get_text(strip=True).replace("梯户比例", "")
        # print(tihubili)
        tihubili_list.append(tihubili)
    else:
        # print("未找到梯户信息")
        tihubili_list.append('')

    peibeidianti_tag = detail_soup.select('.base .content ul li')
    if len(peibeidianti_tag) > 10:
        peibeidianti = peibeidianti_tag[10].get_text(strip=True).replace("配备电梯", "")
        # print(peibeidianti)
        peibeidianti_list.append(peibeidianti)
    else:
        # print("未找到电梯信息")
        peibeidianti_list.append('')

    guapai = detail_soup.find('span', text='挂牌时间').find_next_sibling('span').text if detail_soup.find('span',
                                                                                                      text='挂牌时间') else None
    guapai_list.append(guapai)
    last_deal = detail_soup.find('span', text='上次交易').find_next_sibling('span').text if detail_soup.find('span',
                                                                                                         text='上次交易') else None
    last_deal_list.append(last_deal)
    ownership = detail_soup.find('span', text='交易权属').find_next_sibling('span').text if detail_soup.find('span',
                                                                                                         text='交易权属') else None
    ownership_list.append(ownership)
    use = detail_soup.find('span', text='房屋用途').find_next_sibling('span').text if detail_soup.find('span',
                                                                                                   text='房屋用途') else None
    use_list.append(use)
    years = detail_soup.find('span', text='房屋年限').find_next_sibling('span').text if detail_soup.find('span',
                                                                                                     text='房屋年限') else None
    years_list.append(years)
    plege = detail_soup.find('span', text='抵押信息').find_next_sibling('span').text if detail_soup.find('span',
                                                                                                     text='抵押信息') else None
    plege_list.append(plege)
    check_code = detail_soup.find('span', text='房源核验码').find_next_sibling('span').text if detail_soup.find('span',
                                                                                                           text='房源核验码') else None
    check_code_list.append(check_code)
    indate = detail_soup.find('span', text='有效期限').find_next_sibling('span').text if detail_soup.find('span',
                                                                                                      text='有效期限') else None
    indate_list.append(indate)
    subway_info = detail_soup.find("a", {"class": "supplement"})
    if subway_info:
        traffic_list.append(subway_info.text)
        # print(subway_info.text)
    else:
        # print("未找到地铁站信息")
        traffic_list.append('')

    unit_price_tag = detail_soup.select_one('.unitPriceValue')
    if unit_price_tag is not None:
        unit_price = unit_price_tag.get_text(strip=True)
        # print(unit_price)
        unit_price_list.append(unit_price)
    else:
        print('未找到单价信息')
        unit_price_list.append('')

# 3.保存数据
def save_data():
    infos = {'小区': xiaoqu_list,
             '梯户比': tihubili_list,
             '是否配备电梯': peibeidianti_list,
             '挂牌时间': guapai_list,
             '上次交易': last_deal_list,
             '交易权属': ownership_list,
             '房屋用途': use_list,
             '房屋年限': years_list,
             '抵押信息': plege_list,
             '房屋核验码': check_code_list,
             '有效期限': indate_list,
             '交通情况': traffic_list,
             '单价': unit_price_list}
    data = pd.DataFrame(infos,
                        columns=['小区', '梯户比', '是否配备电梯','挂牌时间', '上次交易', '交易权属', '房屋用途', '房屋年限', '抵押信息', '房屋核验码', '有效期限', '交通情况', '单价'])
    data.to_csv("成都二手房2" + '.csv')

# url = "https://cd.lianjia.com/ershoufang/jinjiang/"
# get_intro(url)

get_intro()
save_data()

# f = open("index.html", "r", encoding="utf-8")
# t = f.readlines()
# content = "".join(t)
# # print(content)
# get_content(content)
# -- coding: utf-8 --
