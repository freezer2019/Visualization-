#import required libraries.
import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

cov_cases = pd.read_csv("data/cov_cases.csv")
fig = go.Figure()

fig = px.choropleth(cov_cases,
                   color_continuous_scale = 'rdpu',
                   locations='abbrev',
                   color='death',
                   hover_name = 'state',
                   locationmode = 'USA-states',
                   animation_frame = 'date')

layout = (
fig.update_layout(
title_text = 'Covid-19 Deaths in the United States',
title_x = 0.5,
geo_scope = 'usa',
geo=dict(
showframe = False,
showcoastlines = False))
)

pio.write_html(fig,
               file='death_cases.html',
               config={'displayModeBar': False},
               auto_open=True,
               include_plotlyjs='cdn',
               full_html=False)


