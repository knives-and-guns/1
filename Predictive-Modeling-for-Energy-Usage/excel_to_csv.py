import pandas as pd
import os
import sys

def excel_to_csv(excel_file, output_file=None):
    """
    将Excel文件转换为CSV文件
    
    参数:
        excel_file: Excel文件路径
        output_file: 输出CSV文件路径，如果为None，则使用相同的文件名但扩展名为.csv
    
    返回:
        输出CSV文件的路径
    """
    try:
        # 检查文件是否存在
        if not os.path.exists(excel_file):
            print(f"错误: 文件 '{excel_file}' 不存在")
            return None
        
        # 如果未指定输出文件，则使用相同的文件名但扩展名为.csv
        if output_file is None:
            output_file = os.path.splitext(excel_file)[0] + '.csv'
        
        # 读取Excel文件
        print(f"正在读取Excel文件: {excel_file}")
        df = pd.read_excel(excel_file)
        
        # 数据处理：保留3位小数
        print("正在处理数据：保留3位小数")
        # 对所有数值列应用round函数，保留3位小数
        df = df.round(3)
        
        # 数据处理：删除"日类型"列
        if "日类型" in df.columns:
            print("正在处理数据：删除'日类型'列")
            df = df.drop(columns=["日类型"])
        else:
            print("注意：未找到'日类型'列")
        
        # 将数据保存为CSV文件
        print(f"正在将数据保存为CSV文件: {output_file}")
        df.to_csv(output_file, index=False, encoding='utf-8-sig')  # 使用utf-8-sig编码以支持中文
        
        print(f"转换完成! CSV文件已保存到: {output_file}")
        return output_file
    
    except Exception as e:
        print(f"转换过程中出现错误: {str(e)}")
        return None

# 如果直接运行此脚本
if __name__ == "__main__":
    # 检查命令行参数
    if len(sys.argv) < 2:
        # 如果没有提供命令行参数，则使用默认文件
        excel_file = "events.xlsx"
        print(f"未提供Excel文件路径，使用默认文件: {excel_file}")
    else:
        # 使用提供的第一个命令行参数作为Excel文件路径
        excel_file = sys.argv[1]
    
    # 如果提供了第二个命令行参数，则使用它作为输出文件路径
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    # 转换Excel文件为CSV文件
    excel_to_csv(excel_file, output_file)