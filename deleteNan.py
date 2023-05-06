# -- coding: utf-8 --
import pandas as pd

# 读取文件1.csv
df = pd.read_csv('成都二手房1.csv')
# 在原 DataFrame 上删除最后一列中为空的行
# 删除存在空值的行
df = df.dropna(how='any').reset_index(drop=True)
# 删除第一列
# df = df.drop(df.columns[0], axis=1)
df.to_csv('成都二手房.csv', index=False)