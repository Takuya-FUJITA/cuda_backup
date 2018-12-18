import pandas as pd
import sys
from sklearn.feature_extraction.text import CountVectorizer

def tokenize(t):
  return t.split(' ')

MIN = '1'

df_train = pd.read_csv('./TrainingData/DataSet/Dataset_' + MIN + '.csv')
df_test = pd.read_csv('/mnt/usbdisk1/NB_DATA/Connect_Time/' + MIN + 'minutes/2013-08-12.csv')

print(df_train.shape)
print(df_test.shape)

df = pd.concat([df_train, df_test])
print(df.shape)
print('------------')

# BoWの作成
frequency = 5/df.shape[0]
print(frequency)
feature_data = df['text'].values
CV = CountVectorizer(min_df=frequency, tokenizer=tokenize)  # CountVectorizerオブジェクトの生成
# CV = CountVectorizer(tokenizer=tokenize)  # CountVectorizerオブジェクトの生成
X = CV.fit_transform(feature_data)
# terms = CV.get_feature_names()                          # 特徴ベクトルの単語順番の確認用

# 特徴ベクトルとラベルをセットでファイルに書き込む
df_feature_vector = pd.DataFrame(X.toarray())
print(df_feature_vector.shape)
df_fv_train = df_feature_vector[:df_train.shape[0]]
df_fv_test  = df_feature_vector[df_train.shape[0]:]
print('------------')
print(df_fv_train.shape)
print(df_fv_test.shape)

df_fv_train = df_fv_train.assign(label=df_train['label'].values)
df_fv_test = df_fv_test.assign(label=df_test['label'].values)
df_fv_train.to_csv('./TrainingData/' + MIN + 'min_train.csv', index=False)
df_fv_test.to_csv('./TrainingData/' + MIN + 'min_test.csv', index=False)
