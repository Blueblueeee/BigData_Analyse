import pandas as pd
import matplotlib.pyplot as plt

# 读取文件数据
df = pd.read_csv('floorPrice1.csv', index_col='Prefix')
# 更换字体
plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号

# 绘制折线图
plt.plot(df.index, df['Price'], marker='o')
plt.xlabel('Floor Level')
plt.ylabel('Average Price')
plt.title('Average Price vs. Floor Level')
plt.xticks(rotation=45)
plt.grid(axis='y')

# 保存图像并显示
# plt.savefig('line_chart.png')
plt.show()
# -- coding: utf-8 --
