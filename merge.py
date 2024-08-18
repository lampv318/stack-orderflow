import pandas as pd

# Bước 1: Đọc dữ liệu từ hai file CSV
df1 = pd.read_csv('./data/tpb/price.csv')
df2 = pd.read_csv('delta.csv')

df1 = df1.drop(['pot_ask','pot_bid'], axis=1)
# df1.to_csv('data.csv')
# df1 = pd.read_csv('data.csv')
# print(df1.columns)
# Bước 2: Gộp hai DataFrame dựa trên cột 't'
merged_df = pd.merge(df2, df1, on='t')


# rename
merged_df = merged_df.rename(columns={'delta': 'pot_ask', 'cum_del': 'pot_bid'})

# replace
merged_df = merged_df[['t','o','h','l','c','v','pot','pot_ask','pot_bid']]

merged_df['pot_ask'] = merged_df['pot_ask'] / 1000000
merged_df['pot_bid'] = merged_df['pot_bid'] / 1000000

# Bước 3: Lưu DataFrame mới thành file CSV
merged_df.to_csv('merged_data.csv', index=False)

# Hiển thị kết quả
print(merged_df)
