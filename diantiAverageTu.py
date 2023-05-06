import pandas as pd
import matplotlib.pyplot as plt

# 读取文件数据
df = pd.read_csv('电梯均价.csv')
# 更换字体
plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号
# 创建画布和子图
fig, ax = plt.subplots(figsize=(7,6))
# 绘制折线图
plt.plot(df['是否配备电梯'], df['Average'], marker='o')
ax.set_title('电梯情况与房价的关系')
ax.set_xlabel('电梯情况')
ax.set_ylabel('平均单价（元/平米）')
# plt.xticks(rotation=45)
plt.grid(axis='y')

# 保存图像并显示
# plt.savefig('line_chart.png')
plt.show()

