import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
# 读取 Excel 文件，从第11行开始读取数据，并将第10行作为表头
df = pd.read_excel('data.xlsx', header=9)  # header=9 表示第10行是表头

# 转换日期时间格式
df['Date/time'] = pd.to_datetime(df['Date/time'])

# 提取月份
df['Month'] = df['Date/time'].dt.month

# 按月份分组并计算平均速度
grouped = df.groupby('Month')['Speed_100m [m/s]'].mean().reset_index()

# 重命名列，使输出更清晰
grouped = grouped.rename(columns={'Speed_100m [m/s]': '平均速度'})

# 打印结果
print(grouped.to_markdown(index=False, numalign="left", stralign="left"))

# matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 指定字体为黑体（SimHei）
#matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 微软雅黑
#matplotlib.rcParams['font.sans-serif'] = ['Source Han Sans CN']  # 思源黑体
matplotlib.rcParams['font.family'] = 'Times New Roman'
plt.figure(figsize=(10, 6))
plt.plot(grouped['Month'], grouped['平均速度'], marker='o', linestyle='-', color='skyblue', label='100m')
plt.title('Monthly Wind Speed Profile', fontsize=18)
plt.xlabel('Month', fontsize=16)
plt.ylabel('Mean Wind Speed(m/s)', fontsize=16)
plt.xticks(grouped['Month'],fontsize=16)
plt.yticks(fontsize=16)

plt.grid(axis='y', linestyle='--')
plt.legend(loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0.)
plt.show()

