import plotly.graph_objects as go
import pandas as pd 

sg_pos = pd.read_csv('Problem 1\CSV Files\Singapore positive.csv')
uae_pos = pd.read_csv('Problem 1\CSV Files\\UAE positive.csv')
ch_pos = pd.read_csv('Problem 1\CSV Files\China positive.csv')
ph_pos = pd.read_csv('Problem 1\CSV Files\Phillipines positive.csv')
can_pos = pd.read_csv('Problem 1\CSV Files\Canada positive.csv')

sg_nega= pd.read_csv('Problem 1\CSV Files\Singapore negative.csv')
uae_nega= pd.read_csv('Problem 1\CSV Files\\UAE negative.csv')
ch_nega= pd.read_csv('Problem 1\CSV Files\China negative.csv')
ph_nega= pd.read_csv('Problem 1\CSV Files\Phillipines negative.csv')
can_nega= pd.read_csv('Problem 1\CSV Files\Canada negative.csv')

group = ["Singapore","UAE","China","Phillipines","Canada"]

fig = go.Figure(data=[
    go.Bar(name='Positive', x=group, y=[sg_pos['pos_total'].values[0],uae_pos['pos_total'].values[0],ch_pos['pos_total'].values[0],ph_pos['pos_total'].values[0],can_pos['pos_total'].values[0]]),
    go.Bar(name='Negative', x=group, y=[sg_nega['neg_total'].values[0],uae_nega['neg_total'].values[0],ch_nega['neg_total'].values[0],ph_nega['neg_total'].values[0],can_nega['neg_total'].values[0]])
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.show()