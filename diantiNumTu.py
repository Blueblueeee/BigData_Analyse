import pandas as pd
import matplotlib.pyplot as plt

# 读取文件1.csv为dataframe对象
df = pd.read_csv('电梯数量.csv')
# 更换字体
plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号
# 获取电梯数列并按照各个类别计数
elevator_count = df['Count'].value_counts()
# 计算各项数量所占比例
total = df['Count'].sum()
ratios = df['Count'] / total

# 将分类信息转化为文字标签
labels = ['有电梯', '无电梯', '暂无数据']

# 绘制饼状图
plt.pie(ratios, labels=labels, autopct='%1.1f%%', startangle=90)

# 添加标题
plt.title("电梯情况占比")

# 显示图形
plt.show()
# -- coding: utf-8 --
