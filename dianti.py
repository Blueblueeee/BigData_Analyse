import re

import pandas as pd

# 读取文件1.csv为dataframe对象
df = pd.read_csv('成都二手房2.csv')

# 获取第4列和最后一列
col_4 = df.iloc[:, 3]
col_last = df.iloc[:, -1]
# 定义正则表达式
pattern = r'\d+'

# 从最后一列中提取数字，并存储到新列表中
nums = []
for s in col_last:
    num_list = re.findall(pattern, str(s))
    if len(num_list) > 0:
        nums.append(float(num_list[0]))
    else:
        nums.append(None)

# 将新列表添加到原始DataFrame中
df.iloc[:, -1] = nums
df_new = pd.concat([col_4, pd.DataFrame(nums)], axis=1)
# 按照第4列的数据相同的数据对最后一列数据求平均，并存储结果到文件3.csv中
result = df_new.groupby(col_4).mean().round(2)
result.to_csv('电梯均价.csv', header=['Average'])

# 统计第4列中的数据情况（不同数据的数量），并存储结果到文件4.csv中
count = col_4.value_counts()
count.to_csv('电梯数量.csv', header=['Count'])
# -- coding: utf-8 --
