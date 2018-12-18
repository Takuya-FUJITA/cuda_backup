import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import sys

def tokenize(t):
  return t.split(' ')

WIDTH = '1000'

df = pd.read_csv('../TrainingData/DataSet/Dataset_' + WIDTH + '.csv')

# BoWの作成
frequency = 5/df.shape[0]
print('frequency -> ', frequency)
feature_data = df['text'].values
CV = CountVectorizer(min_df=frequency, tokenizer=tokenize)  # CountVectorizerオブジェクトの生成
X = CV.fit_transform(feature_data)
# terms = CV.get_feature_names()                            # 特徴ベクトルの単語順番の確認用

# 特徴ベクトルとラベルをセットでファイルに書き込む
df_feature_vector = pd.DataFrame(X.toarray())
print('division -> ', df_feature_vector.shape)
df_feature_vector = df_feature_vector.assign(label=df['label'].values)
df_feature_vector.to_csv('./' + WIDTH + 'width.csv', index=False)
