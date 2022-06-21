import pandas as pd 
import numpy as np
import plotly.graph_objects as go

posi = pd.read_csv('Singaporepositive.csv')
nega = pd.read_csv('Singaporenegative.csv')

df_posi_sorted = posi.sort_values(by='pos_freq')
df_nega_sorted = nega.sort_values(by='neg_freq')


fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df_posi_sorted['pos_word'],
        y=df_posi_sorted['pos_freq'],
    ))

fig.add_trace(
    go.Scatter(
        x=df_nega_sorted['neg_word'],
        y=df_nega_sorted['neg_freq'],
    ))


fig.show()