import pandas as pd
import sys
from sklearn.feature_extraction.text import CountVectorizer

def tokenize(t):
  return t.split(' ')

# # 負例データの読み込み
# dates = ['2013-06-13', '2013-07-23_other', '2013-07-25', '2013-08-29', '2013-09-10', '2013-10-20']
# df_list = []
# for date in dates:
#   data = pd.read_csv("/mnt/usbdisk1/NB_DATA/Each/Preprocessing/" + date + '.csv')
#   df_list.append(data)
# # 全ての負例CSVファイルを結合して，NANを除去して，任意のデータを抽出する（重複なし）
# df_neg = pd.concat(df_list)
# df_neg = df_neg.dropna(how='any')
# df = df_neg.sample(n=44697)
#
# # 正例データの読み込み，NANを除去して，負例と結合する
# df_pos = pd.read_csv('/mnt/usbdisk1/NB_DATA/Each/Preprocessing/2013-07-23_1600-1759.csv')
# df_pos = df_pos.dropna(how='any')
# df_pos.to_csv('./Dataset_pos.csv', index=False)   # 別の実験のために保存
# df.to_csv('./Dataset_neg.csv', index=False)       # 別の実験のために保存
# df = pd.concat([df, df_pos])
# df = df.reset_index(drop=True)
# df.to_csv('./Dataset.csv', index=False)           # この実験のために保存

df = pd.read_csv('/mnt/usbdisk1/NB_DATA/Each/Dataset/Dataset.csv')

# BoWの作成
feature_data = df['text'].values
# CV = CountVectorizer(min_df=0.00005, tokenizer=tokenize)  # CountVectorizerオブジェクトの生成
CV = CountVectorizer(tokenizer=tokenize)  # CountVectorizerオブジェクトの生成
X = CV.fit_transform(feature_data)
# terms = CV.get_feature_names()                          # 特徴ベクトルの単語順番の確認用

# 特徴ベクトルとラベルをセットでファイルに書き込む
df_feature_vector = pd.DataFrame(X.toarray())
df_feature_vector['label'] = df['label']
df_feature_vector.to_csv('./feature_vector4.csv', index=False)
