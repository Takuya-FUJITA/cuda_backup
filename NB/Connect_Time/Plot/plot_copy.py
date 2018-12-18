import numpy as np
import pandas as pd
import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('/mnt/usbdisk1/NB_DATA/Test_Directory/HOGE.csv')

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

x = [0,20,60,65,70,80]
# ax.plot(df['created_at'], df['result'], linestyle='-', color='b', label='All_Tweet')
ax.plot(x, df['result'], drawstyle='steps-post', color='b', label='All_Tweet')
plt.grid()
plt.xlim(pd.Timestamp('2013-8-10 00:00:00'),pd.Timestamp('2013-8-11 00:00:00'))
# x = pd.date_range('2013-08-10', '2013-08-11', freq='60min').time
# ax.set_xticklabels(x)
# ax.grid(True)


ax.legend(loc='best')
ax.set_title('Plot of sine and cosine')
plt.savefig('figure.png')

# # y = f(x)
# x = np.linspace(-np.pi, np.pi)
# y1 = np.sin(x)
# y2 = np.cos(x)
#
# # figure
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
#
# # plot
# ax.plot(x, y1, linestyle='--', color='b', label='y = sin(x)')
# ax.plot(x, y2, linestyle='-', color='#e46409', label='y = cos(x)')
#
# # x axis
# plt.xlim([-np.pi, np.pi])
# ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
# ax.set_xticklabels(['-pi', '-pi/2', '0', 'pi/2', 'pi'])
# ax.set_xlabel('x')
#
# # y axis
# plt.ylim([-1.2, 1.2])
# ax.set_yticks([-1, -0.5, 0, 0.5, 1])
# ax.set_ylabel('y')
#
# # legend and title
# ax.legend(loc='best')
# ax.set_title('Plot of sine and cosine')
#
# # save as png
# plt.savefig('figure.png')
