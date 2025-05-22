import pandas as pd
from datetime import datetime, timedelta

# 读取补全清洗后的数据
df = pd.read_csv(r'd:\Predictive-Modeling-for-Energy-Usage\数据生成\测试1\补全清洗后数据.csv', encoding='utf-8')

# Excel/Matlab 日期序列号的起始日期
base_date = datetime(1899, 12, 30)

rows = []
for i, row in df.iterrows():
    # 用日期列转换为真实日期
    start_utc = base_date + timedelta(days=int(row['日期']))
    end_utc = start_utc + timedelta(days=1)
    # 生成UTC+03:00时间
    start_utc3 = start_utc + timedelta(hours=3)
    end_utc3 = end_utc + timedelta(hours=3)
    # 格式化
    start_utc_str = start_utc.strftime('%Y/%m/%d %H:%M')
    end_utc_str = end_utc.strftime('%Y/%m/%d %H:%M')
    start_utc3_str = start_utc3.strftime('%Y/%m/%d %H:%M')
    end_utc3_str = end_utc3.strftime('%Y/%m/%d %H:%M')
    # 负荷保留三位小数
    avg_load = round(row['负荷'], 3)
    rows.append([start_utc_str, end_utc_str, start_utc3_str, end_utc3_str, avg_load])

# 构建DataFrame
result = pd.DataFrame(rows, columns=[
    'Start time UTC',
    'End time UTC',
    'Start time UTC+03:00',
    'End time UTC+03:00',
    'Average Load In Nanjing'
])

# 保存
result.to_csv(r'd:\Predictive-Modeling-for-Energy-Usage\数据生成\测试1\补全清洗后数据_events格式.csv', index=False, encoding='utf-8')
print('已生成 补全清洗后数据_events格式.csv，日期通过日期列转换，格式为5列，数据行数与原始补全数据一致。')