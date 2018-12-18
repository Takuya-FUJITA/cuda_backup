import pandas as pd

WIDTH = '300'

df_result = pd.read_csv('./result_' + WIDTH + 'width.csv')
df_date = pd.read_csv('/mnt/usbdisk1/NB_DATA/Connect_Tweet/' + WIDTH + 'width/2013-08-12.csv')

df = pd.concat([df_result, df_date['created_at']], axis=1)
df.to_csv('./plot_' + WIDTH + 'width.csv', index=False)
