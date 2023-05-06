import re

import pandas as pd
# 读取csv文件
df = pd.read_csv('成都二手房.csv')
# 定义正则表达式
pattern = r'[+-]?\d{1,3}(,\d{3})*'
nums = []
for item in df.iloc[:, 6]:
    if isinstance(item, str):
        match = re.search(pattern, item)
        if match:
            num_str = match.group().replace(',', '')  # 将逗号替换为空字符串
            nums.append(float(num_str))
        else:
            nums.append(float('nan'))
    else:
        nums.append(item)
# 将最后一列的数据替换为nums
df.iloc[:, 6] = nums
# 计算第七列数据的平均值
avg = df.iloc[:, 6].mean()
# 输出平均值
print("房源平均面积：", avg)