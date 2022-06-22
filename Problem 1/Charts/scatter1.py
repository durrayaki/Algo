import pandas as pd 
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

sg_pos = pd.read_csv('Problem 1\CSV Files\Singapore positive.csv')
uae_pos = pd.read_csv('Problem 1\CSV Files\\UAE positive.csv')
ch_pos = pd.read_csv('Problem 1\CSV Files\China positive.csv')
ph_pos = pd.read_csv('Problem 1\CSV Files\Phillipines positive.csv')
can_pos = pd.read_csv('Problem 1\CSV Files\Canada positive.csv')

#df_posi_sorted = posi.sort_values(by='pos_freq')
#df_nega_sorted = nega.sort_values(by='neg_freq')


fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=sg_pos['pos_word'],
        y=sg_pos['pos_freq'],
        mode='markers',
        name='Singapore'
    ))

fig.add_trace(
    go.Scatter(
        x=uae_pos['pos_word'],
        y=uae_pos['pos_freq'],
        mode='markers',
        name='UAE'
    ))

fig.add_trace(
    go.Scatter(
        x=ch_pos['pos_word'],
        y=ch_pos['pos_freq'],
        mode='markers',
        name='China'
    ))

fig.add_trace(
    go.Scatter(
        x=ph_pos['pos_word'],
        y=ph_pos['pos_freq'],
        mode='markers',
        name='Phillipines'
    ))

fig.add_trace(
    go.Scatter(
        x=can_pos['pos_word'],
        y=can_pos['pos_freq'],
        mode='markers',
        name='Canada'
    ))

fig.show()