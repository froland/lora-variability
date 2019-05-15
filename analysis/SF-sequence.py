import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
import numpy as np
import pandas as pd
def insert_packet(spreading_factor):
    if spreading_factor < 7:
        return []
    return insert_packet(spreading_factor - 1) + [spreading_factor] + insert_packet(spreading_factor - 1)

sf_as_category = pd.Categorical(insert_packet(12), categories=[7, 8, 9, 10, 11, 12], ordered=True)
pyramid = pd.DataFrame({'SF': sf_as_category})
pyramid['seq_num'] = pyramid.index
cmap = sns.color_palette('Blues_d', 6)
fig, ax = plt.subplots(figsize=(4, 3))
plot = sns.scatterplot(x=pyramid.index, y='SF', data=pyramid, hue='SF', legend=False, palette=cmap, ax=ax)
plot.set_title('Spreading factor sequence')
plot.set_ylabel('spreading factor')
plot.set_xlabel('sequence number')
fig.show()
fig.savefig("sf-sequence.svg")

