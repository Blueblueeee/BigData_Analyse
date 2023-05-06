import requests
from bs4 import BeautifulSoup
from lxml import etree
import time
import random
import pandas as pd

qu = ['jinjiang', 'wuhou', 'gaoxin7', 'qingyang', 'jinniu', 'chenghua', 'tianfuxinqu', 'gaoxinxi1', 'shuangliu', 'wenjiang', 'pidou', 'longquanyi', 'xindou', 'tianfuxinqunanqu', 'qingbaijiang']
qu_list, xiaoqu_list, quyu_list, room_list, area_list, orien_list, decor_list, floor_list, build_time_list, total_price_list, unit_price_list = [], [], [], [], [], [], [], [], [], [], []
qu_name = ['锦江区', '武侯区', '高新区', '青羊区', '金牛区', '成华区', '天府新区', '高新西区', '双流区', '温江区', '郫都区', '龙泉驿区', '新都区', '天府新区南区', '青白江区']

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
ip = {
        # 'http':'61.216.156.222',
        'http': '112.194.88.136'
    }
# 1. 发出请求，获取源码
def get_intro():
    for i in range(0, len(qu)):# 属于哪个区
        print('现在爬取的是{}的数据'.format(qu_name[i]))
        for j in range(1, 61): # 页数
            url = 'https://cd.lianjia.com/ershoufang/' + qu[i] + '/pg' + str(j)
            # print(url)
            r = requests.get(url, headers=headers, proxies=ip).text
            quname = qu_name[i]
            get_content(r, quname)

    # res = requests.get(url, headers=headers, proxies=ip)
    # respone = res.content

    # return respone

# 2. 数据提取
def get_content(r,quname):
    s = etree.HTML(r)
    # 获取小区名
    soup = BeautifulSoup(r, 'html.parser')
    xiaoqu_tag = soup.find_all('a', {'data-el': 'region'})
    if xiaoqu_tag:
        for tag in xiaoqu_tag:
            xiaoqu = tag.text.strip()
            xiaoqu_list.append(xiaoqu)  # 添加到对应的列表中
            qu_list.append(quname)
    else:
        xiaoqu = ''
        xiaoqu_list.append('')
        qu_list.append('')
        # print(xiaoqu)

    # 获取区域名
    quyu_tag = soup.find_all('div', {'class': 'positionInfo'})
    if quyu_tag:
        for tag in quyu_tag:
            quyu = tag.find_all('a')[1].text.strip()
            # print(quyu)
            quyu_list.append(quyu)
    else:
        quyu = ''
        quyu_list.append('')

    # 获取总价
    total_price_tag = soup.find_all('div', {'class': 'totalPrice totalPrice2'})
    if total_price_tag:
        for tag in total_price_tag:
            total_price = tag.text.strip()
            total_price_list.append(total_price)
            # print(total_price)
    else:
        total_price = ''
        total_price_list.append('')
        # print(total_price)

    # 获取单价
    unit_price_tag = soup.find_all('div', {'class': 'unitPrice'})
    if unit_price_tag:
        for tag in unit_price_tag:
            unit_price = tag.span.text.strip()
            unit_price_list.append(unit_price)
            # print(unit_price)
    else:
        unit_price = ''
        unit_price_list.append('')
        # print(unit_price)

    # 获取户型、面积、朝向、装修
    info_tag = soup.find_all('div', {'class': 'houseInfo'})
    if info_tag:
        for tag in info_tag:
            info = tag.text.strip()
            # 利用字符串的split方法，按照"|"分割字符串
            items = info.split('|')
            # 获取房间数和厅数
            room = items[0].strip()
            room_list.append(room)
            # 获取面积
            area = items[1].strip()
            area_list.append(area)
            # 朝向
            orien = items[2].strip()
            orien_list.append(orien)
            # 装修
            decor = items[3].strip()
            decor_list.append(decor)
            # 楼层
            floor = items[4].strip() if len(items) >= 5 else ''
            floor_list.append(floor)
            # 建成年份
            build_time = items[5].strip() if len(items) >= 6 else ''
            build_time_list.append(build_time)
            # # 输出结果
            # print('户型：', room)
            # print('面积：', area)
            # print('朝向：', orien)
            # print('装修：', decor)
            # print('楼层：', floor)
            # print('年份：', build_time)
    else:
        info = ''
        room_list.append('')
        area_list.append('')
        orien_list.append('')
        decor_list.append('')
        floor_list.append('')
        build_time_list.append('')
        # print(info)
# 3.保存数据
def save_data():
    infos = {'区': qu_list,
             '小区': xiaoqu_list,
             '区域': quyu_list,
             '户型': room_list,
             '面积': area_list,
             '朝向': orien_list,
             '装修': decor_list,
             '楼层': floor_list,
             '建造时间': build_time_list,
             '总价': total_price_list,
             '单价': unit_price_list}
    data = pd.DataFrame(infos,
                        columns=['区', '小区', '区域', '户型', '面积', '朝向', '装修', '楼层', '建造时间', '总价', '单价'])
    data.to_csv("成都二手房1" + '.csv')

# url = "https://cd.lianjia.com/ershoufang/jinjiang/"
# get_intro(url)

get_intro()
save_data()

# f = open("index.html", "r", encoding="utf-8")
# t = f.readlines()
# content = "".join(t)
# # rint(content)
# get_content(content)
# -- coding: utf-8 --
