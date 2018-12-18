import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import KFold
import sys

clf = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
def NaiveBayes(TRAIN, TEST):
  X   = TRAIN.iloc[:,:TRAIN.shape[1]-1].values  # 配列に変換 ('label'を除く)
  y   = TRAIN['label'].values # ラベル抽出
  X_t = TEST.iloc[:,:TEST.shape[1]-1].values
  y_t = TEST['label'].values
  clf.fit(X, y)               # 学習する
  result = clf.predict(X_t)   # 予測する
  print("精度 -> %f" % (np.sum(result==y_t)/TEST.shape[0]))


# データを読み込んで，シャッフルする
df = pd.read_csv('./feature_vector51.csv', dtype='int16')
df = df.sample(frac=1).reset_index(drop=True)

kf = KFold(n_splits=10)
for train, test in kf.split(df):
  train_df = df.iloc[train]
  test_df = df.iloc[test]
  NaiveBayes(train_df, test_df)
