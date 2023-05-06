import re

import pandas as pd

# 读取文件1.csv
df = pd.read_csv('成都二手房.csv')
# 获取第三列和最后一列的数据
col3 = df.iloc[:, 8]
col_last = df.iloc[:, -1]
# 定义正则表达式
pattern = r'[+-]?\d{1,3}(,\d{3})*'
nums = []
for item in df.iloc[:, -1]:
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
df.iloc[:, -1] = nums
# 将nums转换为DataFrame对象
df_new = pd.concat([col3, pd.DataFrame(nums)], axis=1)
# # 取第三列和最后一列数据
# result = df.iloc[:, [2, -1]]
# # 根据第三列数据去重，并对最后一列数据求均值
result = df_new.groupby(df_new.iloc[:, 0]).mean().round(2)
# 将第三列数据恢复成列
result.reset_index(inplace=True)
# 将结果保存到文件2.csv中
result.to_csv('装修.csv', index=False)
# -- coding: utf-8 --
