import plotly
plotly.tools.set_credentials_file(username='gowrir2', api_key='R4p8IhxxlgwefxJzv9Td')

import json, urllib
import plotly.plotly as py
import pandas as pd
import numpy as np


funding_df = pd.read_csv('Donor_Funding_2.csv')
data_trace = dict(
    type='sankey',
    domain = dict(
      x =  [0,1],
      y =  [0,1]
    ),
    orientation = "h",
    valueformat = ".0f",
    node = dict(
      pad = 10,
      thickness = 30,
      line = dict(
        color = "black",
        width = 0
      ),
      label =  'AAA'
    ),
    link = dict(
      source = funding_df['Source'].dropna(axis=0, how='any'),
      target = funding_df['Target'].dropna(axis=0, how='any'),
      value = funding_df['Value'].dropna(axis=0, how='any')
  )
)

layout =  dict(
    title = "Scottish Referendum Voters who now want Independence",
    height = 772,
    font = dict(
      size = 10
    ),    
)

fig = dict(data=[data_trace], layout=layout)
py.plot(fig, validate=False) 