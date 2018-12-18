import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import KFold
import sys

MIN = '10'

def NaiveBayes(TRAIN, TEST):
  X   = TRAIN.iloc[:,:TRAIN.shape[1]-1].values  # 配列に変換 ('label'を除く)
  y   = TRAIN['label'].values # ラベル抽出
  X_t = TEST.iloc[:,:TEST.shape[1]-1].values
  y_t = TEST['label'].values
  clf.fit(X, y)               # 学習する
  result = clf.predict(X_t)   # 予測する
  print('精度 -> {:.2%}'.format(np.sum(result==y_t)/TEST.shape[0]))
  return (np.sum(result==y_t)/TEST.shape[0])


# データを読み込んで，シャッフルする
path = './' + MIN + 'min.csv'
df = pd.read_csv(path, dtype='int16')
df = df.sample(frac=1).reset_index(drop=True)

accuracy = 0
clf = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)

kf = KFold(n_splits=10)
for train, test in kf.split(df):
  train_df = df.iloc[train]
  test_df = df.iloc[test]
  # NaiveBayes(train_df, test_df, accuracy)
  accuracy += NaiveBayes(train_df, test_df)

print('分類精度 -> {:.2%}'.format(accuracy/10))
