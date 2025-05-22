import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# 读取原始数据
df = pd.read_csv(r'd:\Predictive-Modeling-for-Energy-Usage\数据生成\测试1\原始数据.csv', encoding='utf-8')

# 将“日期”列转换为整数类型
df['日期'] = df['日期'].astype(int)

# 生成完整的日期范围
full_range = pd.DataFrame({'日期': range(df['日期'].min(), df['日期'].max() + 1)})

# 合并，补全缺失日期
df_full = pd.merge(full_range, df, on='日期', how='left')

# 数据清洗：去除异常值（如负荷小于0或大于合理上限，可根据实际情况调整）
upper_limit = df_full['负荷'].quantile(0.99)
lower_limit = df_full['负荷'].quantile(0.01)
df_full.loc[(df_full['负荷'] > upper_limit) | (df_full['负荷'] < lower_limit), '负荷'] = np.nan

# 先用插值法填充缺失值
df_full['负荷_interp'] = df_full['负荷'].interpolate(method='linear')

# 再用回归分析法填充剩余缺失值
not_null = df_full[df_full['负荷_interp'].notnull()]
nulls = df_full[df_full['负荷_interp'].isnull()]
if nulls.shape[0] == 0:
    df_full['负荷_filled'] = df_full['负荷_interp']
else:
    X_train = not_null[['日期']]
    y_train = not_null['负荷_interp']
    X_pred = nulls[['日期']]
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_pred)
    df_full['负荷_filled'] = df_full['负荷_interp']
    df_full.loc[df_full['负荷_interp'].isnull(), '负荷_filled'] = y_pred

# 只保留与原始数据相同的格式，并将负荷保留三位小数
result = df_full[['日期', '负荷_filled']].rename(columns={'负荷_filled': '负荷'})
result['负荷'] = result['负荷'].round(3)

# 保存到当前目录下，文件名可自定义
result.to_csv(r'd:\Predictive-Modeling-for-Energy-Usage\数据生成\测试1\补全清洗后数据.csv', index=False, encoding='utf-8')
print('数据清洗、缺失值填充完成，已保存为 补全清洗后数据.csv')
# 特征工程：添加差分特征
df_full['负荷_diff1'] = df_full['负荷_filled'].diff()
df_full['负荷_diff2'] = df_full['负荷_filled'].diff(2)

# 保存补全和特征工程后的数据
df_full.to_csv('补全清洗特征工程后数据.csv', index=False, encoding='utf-8')
print('数据清洗、缺失值填充和特征工程完成，已保存为 补全清洗特征工程后数据.csv')