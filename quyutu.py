import pandas as pd
import matplotlib.pyplot as plt
# 读取csv文件
df = pd.read_csv('1.csv', index_col=0, encoding='gbk')
# 更换字体
plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号
# 绘制柱状图
ax = df.plot(kind='bar', width=1.2, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#0000FF', '#00FFFF', '#FFFF00', '#FF9912', '#F5DEB3', '#7FFF00', '#3D9140', '#ED9121', '#F5DEB3', '#C0C0C0', '#A020F0'])
# 设置每个柱形的标签
for i in ax.patches:
    ax.text(i.get_x()+0.001, i.get_height()+60, str(int(i.get_height())), fontsize=10, color='black')
# 设置图表标题和坐标轴标签
plt.title('不同区域二手房数量分布', fontsize=16)
plt.xlabel('区域', fontsize=14)
plt.ylabel('二手房数量', fontsize=14)
plt.xticks(range(len(df.index)), df.index)
# 设置X轴刻度的字体大小
plt.xticks([])
# 设置Y轴的比例尺
plt.ylim(0, 17000)
# 调整图表边距和间距
plt.subplots_adjust(bottom=0.1, left=0.1, right=0.98, top=0.9)
# 显示网格线
plt.grid(axis='y', linestyle='--')
# 显示图表
plt.show()
# 保存柱状图为图片
plt.savefig('bar_chart.png', dpi=300, bbox_inches='tight')