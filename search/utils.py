import matplotlib.pyplot as plt
import base64
from io import BytesIO
import matplotlib.dates as mdates
from .models import aiModel
import numpy as np


def get_graph():
    buffer = BytesIO()
    print(buffer)

    plt.savefig(buffer, format='png',bbox_inches='tight')
    print('saved')

    buffer.seek(0)
    print('seeked')

    image_png = buffer.getvalue()

    graph = base64.b64encode(image_png)


    graph = graph.decode('utf-8')


    buffer.close()
    print('closed')
    
    return graph

def get_plot(x,y):
    fmt = mdates.DateFormatter('%m-%d')
    freq = mdates.DayLocator(interval=1)
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,8))
    plt.scatter(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('WER(%)')
    plt.tight_layout()
    plt.gca().xaxis.set_major_formatter(fmt)
    plt.gca().xaxis.set_major_locator(freq)
    plt.plot(x,y, linestyle=':')
    plt.title('Model WER Performance')
    graph = get_graph()
    return graph