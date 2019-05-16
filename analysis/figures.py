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
fig.savefig("sf-sequence.svg")

lora_mons_static = pd.read_pickle('data/lora_mons_static_clean.pkl.gz')
channel = lora_mons_static.query('gtw_id == "eui-0000024b08030186"')[['received', 'dev_id', 'rssi', 'snr', 'data_rate']].set_index('received').sort_index()
channel.index = channel.index.tz_convert('Europe/Brussels')
channel['spreading_factor'] = channel['data_rate'].str.extract('SF([0-9]+)BW').astype(dtype=np.int64)

ax = sns.stripplot(x='spreading_factor', y='rssi', data=channel, alpha=0.3)
ax.set(ylabel='RSSI (dBm)', xlabel='Spreading Factor', title='Distribution of received packets RSSI');
ax.figure.savefig('rssi_sf.png')

ax = sns.stripplot(x='spreading_factor', y='snr', data=channel, alpha=0.3)
ax.set(ylabel='SNR (dB)', xlabel='Spreading Factor', title='Distribution of received packets SNR');
ax.figure.savefig('snr_sf.png')

ax = sns.scatterplot(x='snr', y='rssi', data=channel, alpha=0.3)
ax.set(xlabel='SNR (dB)', ylabel='RSSI (dBm)');
ax.figure.savefig('rssi_snr.png')
