import pandas as pd
import datetime
import csv

# Excel日期序列号转datetime
# Excel起始日期为1899-12-30

def excel_date_to_datetime(excel_date):
    dt = datetime.datetime(1899, 12, 30) + datetime.timedelta(days=int(excel_date))
    return dt

def main():
    input_file = 'events.csv'
    output_file = 'events1.csv'
    # 读取原始数据
    df = pd.read_csv(input_file, encoding='utf-8')
    # 新表头
    header = [
        'Start time UTC',
        'End time UTC',
        'Start time UTC+03:00',
        'End time UTC+03:00',
        'Average Load'
    ]
    rows = []
    for idx, row in df.iterrows():
        excel_serial = row[0]
        avg_load = row[1]
        # 起始时间为当天0点，结束时间为次日0点
        start_utc = excel_date_to_datetime(excel_serial)
        end_utc = start_utc + datetime.timedelta(days=1)
        # UTC+03:00
        start_utc3 = start_utc + datetime.timedelta(hours=3)
        end_utc3 = end_utc + datetime.timedelta(hours=3)
        # 格式化
        start_utc_str = start_utc.strftime('%Y-%m-%d %H:%M:%S')
        end_utc_str = end_utc.strftime('%Y-%m-%d %H:%M:%S')
        start_utc3_str = start_utc3.strftime('%Y-%m-%d %H:%M:%S')
        end_utc3_str = end_utc3.strftime('%Y-%m-%d %H:%M:%S')
        rows.append([
            start_utc_str,
            end_utc_str,
            start_utc3_str,
            end_utc3_str,
            avg_load
        ])
    # 写入新文件
    with open(output_file, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    print(f'转换完成，已生成 {output_file}')

if __name__ == '__main__':
    main()