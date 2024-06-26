import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from windrose import WindroseAxes

matplotlib.rcParams['font.family'] = 'Times New Roman'
# 读取数据，从第10行开始
df = pd.read_excel('data.xlsx', header=9)

# 数据预处理
bins = np.linspace(0, 360, 17)  # 16个风向区间
df['WindDirectionBin'] = pd.cut(df['Direction_100m [°]'], bins, labels=False)

# 计算每个风向区间内的频率
frequency = df['WindDirectionBin'].value_counts(normalize=True).sort_index()

# 为了首尾封闭，需要重复第一个点
angles = np.deg2rad(np.linspace(0, 360, 17, endpoint=True))  # 17个方向，最后一个与第一个重合
frequency = pd.concat([frequency, pd.Series(frequency.iloc[0])], ignore_index=True)

# 使用 WindroseAxes 绘制风频玫瑰图
fig = plt.figure(figsize=(8, 8))
ax = WindroseAxes.from_ax(fig=fig)

# 设置风频玫瑰图
ax.bar(df['Direction_100m [°]'], np.ones_like(df['Direction_100m [°]']), normed=True, opening=0.8, edgecolor='white', bins=np.linspace(0, 1, 6))

# 设置标签和标题
ax.set_title('Wind Frequency Rose(100m)', y=1.05, fontsize=18)
ax.set_legend(title="Frequency(%)", loc='upper right', fontsize=12)

plt.show()
