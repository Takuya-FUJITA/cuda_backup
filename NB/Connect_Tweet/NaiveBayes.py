import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
import sys

WIDTH = '300'

clf = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
def NaiveBayes(TRAIN, TEST):
  X   = TRAIN.iloc[:,:TRAIN.shape[1]-1].values  # 配列に変換 ('label'を除く)
  y   = TRAIN['label'].values # ラベル抽出
  X_t = TEST.iloc[:,:TEST.shape[1]-1].values
  y_t = TEST['label'].values
  clf.fit(X, y)               # 学習する
  result = clf.predict(X_t)   # 予測する
  df_result = pd.DataFrame(result).rename(columns={0: 'result'})
  df_result.to_csv('./Plot/result_' + WIDTH + 'width.csv', index=False)
  # print("精度 -> %f" % (np.sum(result==y_t)/TEST.shape[0]))

# データを読み込んで，シャッフルする
df_train = pd.read_csv('./TrainingData/' + WIDTH + 'width_train.csv', dtype='int16')
df_test = pd.read_csv('./TrainingData/' + WIDTH + 'width_test.csv', dtype='int16')
NaiveBayes(df_train, df_test)
