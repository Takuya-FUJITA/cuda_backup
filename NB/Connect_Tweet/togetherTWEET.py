import pandas as pd
import itertools
import sys

WIDTH = 300
print('WIDTH:', str(WIDTH))

files = ['06-13', '07-23_1600-1759', '07-23_other', '07-25', '08-12', '08-29', '09-10', '10-20']
for f in files:
  path = '/mnt/usbdisk1/NB_DATA/Each/Preprocessing/2013-' + f + '.csv'
  df = pd.read_csv(path)
  df = df.dropna(how='any').reset_index(drop=True)
  df['created_at']  = pd.to_datetime(df['created_at'])

  text = []
  arrival_time = []
  for i, j in itertools.product(range(df.shape[0]//WIDTH), range(WIDTH)):
    if j == 0:
      connect_text = ''
    connect_text += ' ' + df['text'][i*WIDTH+j]
    if j == WIDTH-1:
      text.append(connect_text[1:])
      arrival_time.append(df['created_at'][i*WIDTH+j])

  if f=='07-23_1600-1759':
    label_value = 1
  elif f=='08-12':
    label_value = 99
  else:
    label_value = 0

  df_text = pd.DataFrame(text).assign(label=label_value).rename(columns={0: 'text'})
  df_arrival_time = pd.DataFrame(arrival_time).rename(columns={0: 'created_at'})
  df = pd.concat([df_text, df_arrival_time], axis=1)
  df = df[['created_at','text','label']]
# df = df.reset_index(drop=True)


  path2 ='/mnt/usbdisk1/NB_DATA/Connect_Tweet/' + str(WIDTH) + 'width/2013-' + f + '.csv'
  df.to_csv(path2, index=False)
