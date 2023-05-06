import textwrap

import pandas as pd
import matplotlib.pyplot as plt
# 读取文件1.csv
df = pd.read_csv('排名前二十小区.csv')
# 取第一列为X轴，第二列为Y轴
x = df.iloc[:, 0]
y = df.iloc[:, 1]
# 更换字体
plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号
# 绘制柱状图
plt.bar(x, y)
# 添加X轴和Y轴标签
plt.title('价格排名前二十的小区', fontsize=16)
plt.ylabel('单价（元/平米）')
# 设置X轴标签旋转角度
# plt.xticks(rotation=90, wrap=True)
# 设置X轴刻度的字体大小和其他属性
plt.xticks(fontsize=8, rotation=90)
# 设置Y轴的比例尺
plt.ylim(0, 100000)
# 调整图表边距和间距
plt.subplots_adjust(bottom=0.3, left=0.1, right=0.98, top=0.9)
# 显示网格线
plt.grid(axis='y', linestyle='--')
# 显示图像
plt.show()