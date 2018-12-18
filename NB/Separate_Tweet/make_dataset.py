import pandas as pd

# 負例データの読み込み
dates = ['2013-06-13', '2013-07-23_other', '2013-07-25', '2013-08-29', '2013-09-10', '2013-10-20']
df_list = []
for date in dates:
  data = pd.read_csv("/mnt/usbdisk1/NB_DATA/Each/Preprocessing/" + date + '.csv')
  df_list.append(data)
# 全ての負例CSVファイルを結合して，NANを除去して，任意のデータを抽出する（重複なし）
df_neg = pd.concat(df_list)
df_neg = df_neg.dropna(how='any')
df = df_neg.sample(n=44697)

# 正例データの読み込み，NANを除去して，負例と結合する
df_pos = pd.read_csv('/mnt/usbdisk1/NB_DATA/Each/Preprocessing/2013-07-23_1600-1759.csv')
df_pos = df_pos.dropna(how='any')
df_pos.to_csv('./Dataset_pos.csv', index=False)   # 別の実験のために保存
df.to_csv('./Dataset_neg.csv', index=False)       # 別の実験のために保存
df = pd.concat([df, df_pos])
df = df.reset_index(drop=True)
df.to_csv('./Dataset.csv', index=False)           # この実験のために保存
