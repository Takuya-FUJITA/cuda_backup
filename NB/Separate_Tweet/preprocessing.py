import pandas as pd
import MeCab
import sys

df = pd.read_csv('/mnt/usbdisk1/NB_DATA/Original_Tweet/2013-08-12.csv')

# pandas が誤作動するので"(ダブルクォーテーション)は削除する．ファイル書き込み時はダブルクォーテーションで囲まれた文章がCSVファイルに表示されることに注意．
df['text'] = df['text'].str.replace('"','')
df = df.dropna(how='any').reset_index(drop=True)

removal_keywords = ["RT", "@", "#", "http"]
keywords = ['名詞', '動詞', '形容詞']
mecab = MeCab.Tagger()
for i in range(df.shape[0]):
  connect = ""
  terms = df['text'][i].split(" ")
  for term in terms:
    if term.startswith(tuple(removal_keywords)):
      pass
    else:
      connect = connect + term

  # 形態素解析
  mecab.parse('')     # 文字列がGCされるのを防ぐ
  node = mecab.parseToNode(connect)
  extract_words = ''
  while node:
    if node.feature.split(',')[0] in keywords:
      if node.feature.split(',')[6] != '*':
        extract_words += ' ' + node.feature.split(',')[6]
    node = node.next
  df['text'][i] = extract_words[1:]

df = df.assign(label=99)
df.to_csv('/mnt/usbdisk1/NB_DATA/Each/Preprocessing/2013-08-12.csv', index=False)
