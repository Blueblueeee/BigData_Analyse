# -- coding: utf-8 --
import pandas as pd
# 读取文件1.csv
df = pd.read_csv('成都二手房.csv')
# 统计第六列每个值的出现次数
counts = df.iloc[:, 5].value_counts()
# print(counts)
# 将统计结果保存到文件2.csv中
counts.to_csv('户型分析.csv', header=['count'])