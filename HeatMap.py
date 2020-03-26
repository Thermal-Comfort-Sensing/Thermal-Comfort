# Reference:
# 1. https://blog.quantinsti.com/creating-heatmap-using-python-seaborn/
# 2. https://seaborn.pydata.org/generated/seaborn.heatmap.html
# 3. https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html
# 4. https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class HeatMap(object):

    def __init__(self):
        self.fig, self.ax = plt.subplots()
        
    def parse_data(self):
        self.data = pd.read_excel('Data.xlsx', header=0, 
            names=['Computer Time',
                   'Sensor Time',
                   'Ambient Temperature',
                   'Temp1',
                   'Temp2',
                   'X Axis',
                   'Y Axis',
                   'Avg Temp'])

    def gen_heatmap(self):
        sns.heatmap(self.data.pivot('Y Axis', 'X Axis', 'Avg Temp'), ax=self.ax)
        plt.show()


if __name__ == '__main__':
    heat_map = HeatMap()
    heat_map.parse_data()
    # print(heat_map.data)
    heat_map.gen_heatmap()