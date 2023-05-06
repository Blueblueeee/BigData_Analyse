import pandas as pd
import matplotlib.pyplot as plt

# 读取 CSV 文件
df = pd.read_csv('floorNum.csv', encoding='gbk', index_col='楼层数范围')
# 更换字体
plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号

# 计算各项数量所占比例
total = df['数量'].sum()
ratios = df['数量'] / total

# 绘制饼状图
labels = ['低楼层', '中等楼层', '高楼层', '超高楼层']
explode = [0.1, 0.1, 0.1, 0.1]
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(ratios, labels=labels, explode=explode, autopct='%1.1f%%',
       shadow=True, startangle=90, colors=['green', 'orange', 'red', 'purple'])
ax.axis('equal')

# 显示和保存图像
plt.tight_layout()
plt.savefig('pie_chart.png')
plt.show()