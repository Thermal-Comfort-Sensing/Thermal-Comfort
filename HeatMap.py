# Reference:
# 1. https://blog.quantinsti.com/creating-heatmap-using-python-seaborn/
# 2. https://seaborn.pydata.org/generated/seaborn.heatmap.html
# 3. https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html
# 4. https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
# 5. https://stackoverflow.com/questions/13842088/set-value-for-particular-cell-in-pandas-dataframe-using-index
# 6. https://stackoverflow.com/questions/17071871/how-to-select-rows-from-a-dataframe-based-on-column-values
# 7. https://stackoverflow.com/questions/34091877/how-to-add-header-row-to-a-pandas-dataframe
# 8. https://stackoverflow.com/questions/34232073/seaborn-heatmap-y-axis-reverse-order

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math

SCALE = 10


def coordinate_conversion(row):
    vertical_angle = row['vertical_angle']
    horizontal_angle = row['horizontal_angle']
    # row['vertical_angle'] = SCALE * (math.cos(vertical_angle) * math.sin(horizontal_angle)) / \
    #               (1 + math.fabs(math.sin(vertical_angle))) * (-1)
    # row['horizontal_angle'] = SCALE * (math.cos(vertical_angle) * math.cos(horizontal_angle)) / \
    #               (1 + math.fabs(math.sin(vertical_angle)))

    # row['vertical_angle'] = SCALE * math.cos(vertical_angle) * math.sin(horizontal_angle) * (-1)
    # row['horizontal_angle'] = SCALE * math.sin(vertical_angle)

    row['vertical_angle'] = SCALE * math.cos(vertical_angle) * math.sin(horizontal_angle) * (-1) / math.cos(vertical_angle)
    row['horizontal_angle'] = SCALE * math.sin(vertical_angle) / math.cos(vertical_angle)

    # row['vertical_angle'] = SCALE * math.tan(horizontal_angle) * (-1)
    # row['horizontal_angle'] = (SCALE * math.tan(vertical_angle)) / math.cos(horizontal_angle)

    return row


class HeatMap(object):

    def __init__(self):
        self.fig, self.ax = plt.subplots()
        
    def parse_data(self):
        # Data format: vertical angle, horizontal angle, temperature
        data = pd.read_csv('heatmap_otcbvs/Meng/Meng1-1-1.csv',
                           names=['vertical_angle', 'horizontal_angle', 'temp'])
        data = data.apply(coordinate_conversion, axis=1)
        data = data.drop_duplicates(subset=['vertical_angle', 'horizontal_angle'])
        self.data = data
        print(self.data)

    def gen_heatmap(self):
        ax = sns.heatmap(self.data.pivot('horizontal_angle', 'vertical_angle', 'temp'), ax=self.ax)
        ax.invert_yaxis()
        plt.show()


if __name__ == '__main__':
    heat_map = HeatMap()
    heat_map.parse_data()
    heat_map.gen_heatmap()
