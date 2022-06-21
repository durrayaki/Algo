import plotly.graph_objects as go
import pandas as pd 

sg_pos = pd.read_csv('Singaporepositive.csv')
uae_pos = pd.read_csv('UAEpositive.csv')
ch_pos = pd.read_csv('Chinapositive.csv')
ph_pos = pd.read_csv('Phillipinespositive.csv')
can_pos = pd.read_csv('Canadapositive.csv')

sg_nega= pd.read_csv('Singaporenegative.csv')
uae_nega= pd.read_csv('UAEnegative.csv')
ch_nega= pd.read_csv('Chinanegative.csv')
ph_nega= pd.read_csv('Phillipinesnegative.csv')
can_nega= pd.read_csv('Canadanegative.csv')

group = ["Positive","Negative"]

fig = go.Figure(data=[
    go.Bar(name='Singapore', x=group, y=[sg_pos['pos_total'].values[0],sg_nega['neg_total'].values[0]]),
    go.Bar(name='UAE', x=group, y=[uae_pos['pos_total'].values[0],uae_nega['neg_total'].values[0]]),
    go.Bar(name='China', x=group, y=[ch_pos['pos_total'].values[0],ch_nega['neg_total'].values[0]]),
    go.Bar(name='Phillipines', x=group, y=[ph_pos['pos_total'].values[0],ph_nega['neg_total'].values[0]]),
    go.Bar(name='Canada', x=group, y=[can_pos['pos_total'].values[0],can_nega['neg_total'].values[0]])
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.show()