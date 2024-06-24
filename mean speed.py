import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Times New Roman'

# 读取数据，从第10行开始
df = pd.read_excel('data.xlsx', header=9)

# 数据预处理
bins = np.linspace(0, 360, 17)  # 16个风向区间
df['WindDirectionBin'] = pd.cut(df['Direction_100m [°]'], bins, labels=False)

# 计算每个风向区间内的平均风速
grouped = df.groupby('WindDirectionBin', observed=False)['Speed_100m [m/s]'].mean()

# 为了首尾封闭，需要重复第一个点
angles = np.deg2rad(np.linspace(0, 360, 17, endpoint=True))  # 17个方向，最后一个与第一个重合
grouped = pd.concat([grouped, pd.Series(grouped.iloc[0])], ignore_index=True)

# 绘制风玫瑰图
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})

# 设置角度和数值标签
angle_labels = np.linspace(0, 360, 16, endpoint=False)  # 16个数值标签
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)

# 设置格式化函数来显示带单位的标签
ax.set_thetagrids(angle_labels, labels=[f"{x:.1f}°" for x in angle_labels])

# 绘制点和线，并填充区域
ax.plot(angles, grouped, marker='o', linestyle='-', color='skyblue')
ax.fill(angles, grouped, color='skyblue', alpha=0.4)  # 填充区域

# 设置速度单位的极坐标标签
ax.set_rlabel_position(0)  # 极径标签位置
ax.yaxis.set_tick_params(labelright=True, labelsize=16)  # 在右侧显示标签
r_labels = [f"{x:.1f} m/s" for x in ax.get_yticks()]
ax.set_yticklabels(r_labels, fontsize=16)

# 显示极径网格线
ax.grid(axis='y', linestyle='--', color='gray')  # 显示网格线

# 添加标题
ax.set_title('Mean Wind Speed (100m)', y=1.10, fontsize=18)
plt.show()
