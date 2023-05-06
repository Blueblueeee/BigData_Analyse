import re

import pandas as pd

# 读取文件1.csv为dataframe对象
df = pd.read_csv('成都二手房2.csv')

# 统计倒数第二列中有数据和无数据的情况，并存储结果到2.csv中
col = df.iloc[:, -2]
count = col.count()
empty_count = col.isna().sum()
counts_df = pd.DataFrame({'有': count, '无': empty_count}, index=['项数'])
counts_df.to_csv('近地铁的房源.csv')

# 对最后一列数据进行处理，取出数字并对应按照倒数第二列内容分组求均值，
# 最终将结果存储到文件3.csv中
nums = []
for s in df.iloc[:, -1]:
    num_list = re.findall(r'\d+', str(s))
    if len(num_list) > 0:
        nums.append(float(num_list[0]))
    else:
        nums.append(None)

df['numbers'] = nums
result = df.groupby(df.iloc[:, -2].fillna(''))['numbers'].mean().round(2).reset_index()
result.to_csv('有无地铁的均价.csv', header=['倒数第二列', '平均值'], index=False)

