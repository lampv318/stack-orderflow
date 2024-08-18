import glob
import os
import pandas as pd
import csv
from datetime import datetime


df = pd.read_csv('./data/tpb/of.csv')

# Bước 2: Tính toán giá trị delta và cum
df['delta'] = df['a'] - df['b']

# Tính toán cum bằng cách nhóm theo ngày và tính tổng giá trị delta
df['cum_del'] = df['delta'].cumsum()

# Bước 4: Lấy các cột cần thiết và gộp theo ngày
result_df = df.groupby('t').agg({'delta': 'sum', 'cum_del': 'last'}).reset_index()

# Bước 3: Lưu kết quả vào file CSV mới
result_df.to_csv('delta.csv', index=False)

# Hiển thị kết quả
print(result_df)
