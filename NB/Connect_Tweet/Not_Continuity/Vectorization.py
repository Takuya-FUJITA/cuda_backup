import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def tokenize(t):
  return t.split(' ')

df_pos = pd.read_csv('/mnt/usbdisk1/NB_DATA/Each/Dataset/Dataset_pos.csv')
df_neg = pd.read_csv('/mnt/usbdisk1/NB_DATA/Each/Dataset/Dataset_neg.csv')

width = 50
data_pos = []
data_neg = []
for i in range(df_pos.shape[0]//width):
  connect_pos = ''
  connect_neg = ''
  for j in range(width):
    connect_pos += ' ' + df_pos['text'][i*width+j]
    connect_neg += ' ' + df_neg['text'][i*width+j]
  data_pos.append(connect_pos[1:])
  data_neg.append(connect_neg[1:])

df_pos = pd.DataFrame(data_pos).assign(label=1).rename(columns={0: 'text'})
df_neg = pd.DataFrame(data_neg).assign(label=0).rename(columns={0: 'text'})
df = pd.concat([df_pos, df_neg])
df = df.reset_index(drop=True)

# BoWの作成
feature_data = df['text'].values
CV = CountVectorizer(min_df=0.003, tokenizer=tokenize)  # CountVectorizerオブジェクトの生成
# CV = CountVectorizer(tokenizer=tokenize)  # CountVectorizerオブジェクトの生成
X = CV.fit_transform(feature_data)
# terms = CV.get_feature_names()          # 特徴ベクトルの単語順番の確認用

# 特徴ベクトルとラベルをセットでファイルに書き込む
df_feature_vector = pd.DataFrame(X.toarray())
df_feature_vector['label'] = df['label']
df_feature_vector.to_csv('./feature_vector50.csv', index=False)
