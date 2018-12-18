import pandas as pd

MIN = '60'
print('MIN:', MIN)

cnt = 0
files = ['06-13', '07-23_1600-1759', '07-23_other', '07-25', '08-12', '08-29', '09-10', '10-20']
for f in files:
  path = '/mnt/usbdisk1/NB_DATA/Each/Preprocessing/2013-' + f + '.csv'
  df = pd.read_csv(path)
  df = df.dropna(how='any').reset_index(drop=True)
  df['created_at']  = pd.to_datetime(df['created_at'])

  DATA = []
  for name, group in df.groupby(pd.Grouper(key='created_at', freq=MIN+'min')):
    if group.shape[0] != 0:
      # 同じグループのテキストを結合する
      group = group.reset_index(drop=True)
      text = ''
      for i in range(group.shape[0]):
        text += ' ' + group['text'][i]

      # 任意に決定したグループを1文書として加える
      group_data = []
      group_data.append(name.strftime('%Y/%m/%d %H:%M:%S'))
      group_data.append(text[1:])
      DATA.append(group_data)

    else:
      cnt += 1

  if f=='07-23_1600-1759':
    label_value = 1
  elif f=='08-12':
    label_value = 99
  else:
    label_value = 0

  df2 = pd.DataFrame(DATA, columns=['created_at', 'text'])
  df2 = df2.assign(label=label_value)
  path2 ='/mnt/usbdisk1/NB_DATA/Connect_Time/' + MIN + 'minutes/2013-' + f + '.csv'
  df2.to_csv(path2, index=False)
