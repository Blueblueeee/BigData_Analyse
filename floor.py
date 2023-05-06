import csv

import pandas as pd

data = pd.read_csv('成都二手房.csv', usecols=[8])
# 获取第九列数据，并保存为一个列表
column_data = data.iloc[:, 0].tolist()

digits = []
for text in column_data:
    digit = ''
    # 遍历字符串，如果是数字或者小数点，就加入新的字符串中
    for char in text:
        if char.isdigit() or char == '.':
            digit += char
    digits.append(digit)

# print(digits)
# 根据楼层数划分区间
low_floor_range = (0, 10)
mid_floor_range = (11, 20)
high_floor_range = (21, 30)
superhigh_floor_range = (31, float('inf'))

# 将数字转换为浮点数
digit_list = [float(digit) for digit in digits]

# 对数字进行分组
low_floor_count = sum(low_floor_range[0] <= x < low_floor_range[1] for x in digit_list)
mid_floor_count = sum(mid_floor_range[0] <= x < mid_floor_range[1] for x in digit_list)
high_floor_count = sum(high_floor_range[0] <= x < high_floor_range[1] for x in digit_list)
superhigh_floor_count = sum(superhigh_floor_range[0] <= x < superhigh_floor_range[1] for x in digit_list)

# 输出结果
print("低楼层数量：", low_floor_count)
print("中等楼层数量：", mid_floor_count)
print("高楼层数量：", high_floor_count)
print("超高楼层数量：", superhigh_floor_count)

# 将结果写入CSV文件
with open('floorNum.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['楼层数范围', '数量'])
    writer.writerow(['低楼层', low_floor_count])
    writer.writerow(['中等楼层', mid_floor_count])
    writer.writerow(['高楼层', high_floor_count])
    writer.writerow(['超高楼层', superhigh_floor_count])
# -- coding: utf-8 --
