import pandas as pd

MIN = '10'
# sample_number = (((60/int(MIN))*24)*9)/2
sample_number = int((60/int(MIN))*2)    # 正例のデータ数に揃える
print('sample_number -> ', sample_number)

# 負例データの読み込み
dates = ['2013-06-13', '2013-07-23_other', '2013-07-25', '2013-08-29', '2013-09-10', '2013-10-20']
df_list = []
for date in dates:
  data = pd.read_csv('/mnt/usbdisk1/NB_DATA/Connect_Time/' + MIN + 'minutes/' + date + '.csv')
  df_list.append(data)
# 全ての負例CSVファイルを結合して，NANを除去して，任意のデータを抽出する（重複なし）
df_neg = pd.concat(df_list)
df_neg = df_neg.dropna(how='any')
df = df_neg.sample(n=sample_number)

# 正例データの読み込み，NANを除去して，負例と結合する
df_pos = pd.read_csv('/mnt/usbdisk1/NB_DATA/Connect_Time/' + MIN + 'minutes/2013-07-23_1600-1759.csv')
print('df_pos -> ', df_pos.shape)
df_pos = df_pos.dropna(how='any')
print('df_pos -> ', df_pos.shape)
df = pd.concat([df, df_pos])
df = df.reset_index(drop=True)
df.to_csv('./TrainingData/DataSet/Dataset_' + MIN + '.csv', index=False)
