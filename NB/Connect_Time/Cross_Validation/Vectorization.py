import pandas as pd
import sys
from sklearn.feature_extraction.text import CountVectorizer

def tokenize(t):
  return t.split(' ')

MIN = '10'

df = pd.read_csv('../TrainingData/DataSet/Dataset_' + MIN + '.csv')

# BoWの作成
frequency = 2/df.shape[0]
print(frequency)
feature_data = df['text'].values
CV = CountVectorizer(min_df=frequency, tokenizer=tokenize)  # CountVectorizerオブジェクトの生成
# CV = CountVectorizer(tokenizer=tokenize)  # CountVectorizerオブジェクトの生成
X = CV.fit_transform(feature_data)
# terms = CV.get_feature_names()                            # 特徴ベクトルの単語順番の確認用

# 特徴ベクトルとラベルをセットでファイルに書き込む
df_feature_vector = pd.DataFrame(X.toarray())
print(df_feature_vector.shape)
df_feature_vector = df_feature_vector.assign(label=df['label'].values)
df_feature_vector.to_csv('./' + MIN + 'min.csv', index=False)
