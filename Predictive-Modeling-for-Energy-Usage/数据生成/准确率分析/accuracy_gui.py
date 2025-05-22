import tkinter as tk
from tkinter import messagebox, scrolledtext
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def analyze():
    try:
        y_true = [float(x) for x in text_true.get("1.0", tk.END).strip().split()]
        y_pred = [float(x) for x in text_pred.get("1.0", tk.END).strip().split()]
        if len(y_true) != len(y_pred):
            messagebox.showerror("错误", "初始数据和预测数据长度不一致！")
            return
        y_true = np.array(y_true)
        y_pred = np.array(y_pred)
        mae = mean_absolute_error(y_true, y_pred)
        mse = mean_squared_error(y_true, y_pred)
        rmse = np.sqrt(mse)
        mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
        r2 = r2_score(y_true, y_pred)
        accuracy_percent = 100 - mape  # 或者 accuracy_percent = (1 - mape/100) * 100
        result = (
            f"样本数: {len(y_true)}\n"
            f"MAE(平均绝对误差): {mae:.3f}\n"
            f"MSE(均方误差): {mse:.3f}\n"
            f"RMSE(均方根误差): {rmse:.3f}\n"
            f"MAPE(平均绝对百分比误差): {mape:.2f}%\n"
            f"R²(决定系数): {r2:.4f}\n"
            f"准确率百分比: {accuracy_percent:.2f}%\n"
        )
        text_result.config(state=tk.NORMAL)
        text_result.delete("1.0", tk.END)
        text_result.insert(tk.END, result)
        text_result.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("错误", f"数据格式有误或计算出错：\n{e}")

root = tk.Tk()
root.title("预测准确率分析工具")

tk.Label(root, text="粘贴初始数据（每行一个数）:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
tk.Label(root, text="粘贴预测数据（每行一个数）:").grid(row=0, column=1, padx=5, pady=5, sticky="w")

text_true = scrolledtext.ScrolledText(root, width=30, height=20)
text_true.grid(row=1, column=0, padx=5, pady=5)
text_pred = scrolledtext.ScrolledText(root, width=30, height=20)
text_pred.grid(row=1, column=1, padx=5, pady=5)

btn = tk.Button(root, text="分析准确率", command=analyze)
btn.grid(row=2, column=0, columnspan=2, pady=10)

text_result = scrolledtext.ScrolledText(root, width=65, height=8, state=tk.DISABLED)
text_result.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()