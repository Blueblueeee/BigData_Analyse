import pandas as pd

# 读取文件1.csv和文件2.csv为dataframe对象
df1 = pd.read_csv('成都二手房.csv')
df2 = pd.read_csv('成都二手房2.csv')

# 对两个dataframe进行合并，依据1.csv的第三列和2.csv的第二列
merged_df = pd.merge(df1, df2, left_on=df1.columns[2], right_on=df2.columns[1], how='inner')

# 将结果保存到文件4.csv中
merged_df.to_csv('zongdata.csv', index=False)
# -- coding: utf-8 --
