# import re
#
# import pandas as pd
#
# # 读取csv文件
# df = pd.read_csv('成都二手房.csv', header=None)
# # 获取第二列和最后一列的数据
# # col3 = df.iloc[1:, 2]
# # col_last = df.iloc[1:, -1]
# # 定义正则表达式
# pattern = r'[+-]?\d{1,3}(,\d{3})*'
# nums = []
# for item in df.iloc[1:, -1]:
#     if isinstance(item, str):
#         match = re.search(pattern, item)
#         if match:
#             num_str = match.group().replace(',', '')  # 将逗号替换为空字符串
#             nums.append(float(num_str))
#         else:
#             nums.append(float('nan'))
#     else:
#         nums.append(item)
# # 将两列数据合并
# df.iloc[1:, -1] = nums
# # 将nums转换为DataFrame对象
# # df_new = pd.concat([col3, pd.DataFrame(nums)], axis=1)
#
# # df_new = pd.concat([col2, nums], axis=1)
# # 将 DataFrame 中的所有值转换为 float 类型
# df = df.apply(pd.to_numeric, errors='coerce')
# # 按最后一列数据降序排序
# df_sorted = df.sort_values(by=[df.columns[-1]], ascending=False)
# # 按照第二列数据去重
# # df_unique = df_sorted.drop_duplicates(subset=[df_sorted.columns[0]])
# # 输出排名前二十的第二列数据
# result = df_sorted.iloc[:,][:20].values.tolist()
# # 将列表转换为 DataFrame 对象
# df = pd.DataFrame(result)
# # 将 DataFrame 对象写入 CSV 文件
# df.to_csv('2.csv', index=False)
# print(result)

# -- coding: utf-8 --
# import pandas as pd
# DataFrame1 = pd.read_csv('成都二手房.csv')
# DataFrame2 = pd.read_csv('2.csv')
# # result = pd.merge(DataFrame1, DataFrame2[['0']], on='0', how='inner')
# # result = result.sort_values(by='0', ignore_index=True)
# result = pd.merge(DataFrame2[['0']], DataFrame1, on='0')
# result.to_csv('排名前二十小区.csv', index=False)

import pandas as pd
# 读取文件1.csv
df = pd.read_csv('小区价格.csv')
# 按照第二列数据降序排列并取前二十行数据
result = df.sort_values(by=df.columns[1], ascending=False).iloc[:20]
# 将结果保存到文件2.csv中
result.to_csv('排名前二十小区.csv', index=False)
