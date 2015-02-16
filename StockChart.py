import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime



    
def graph():
    date, value = np.loadtxt('gpro.csv',
                             delimiter = ',',
                             unpack=True,
                             converters = {0:mdates.strpdate2num('%d-%m-%y')})
    fig = plt.figure()

    ax1 = fig.add_subplot(1,1,1, axisbg='white')

    plt.plot_date(x=date, y=value, fmt='-')
    plt.title('GPRO')
    plt.ylabel('Price in USD')
    plt.xlabel('Date')

    plt.show()

graph()
