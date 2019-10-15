import numpy as np
import pandas as pd
import plotly
import plotly.offline as offline
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, plot, iplot
#init_notebook_mode(connected=True)

#import csv file
train = pd.read_csv('/Users/garrettmorris/Desktop/database_stuff/earthquakes.csv')

#get mapbox token
mapbox_access_token = open("/Users/garrettmorris/Desktop/database_stuff/A07/mapbox_token.txt").read()

shaz13_custom_style = "mapbox://styles/shaz13/cjiog1iqa1vkd2soeu5eocy4i"
# #set the geo=spatial data
# data = [go.Scattermapbox(
#             lat= train['latitude'] ,
#             lon= train['longitude'],
#             customdata = train['earthquake_id'],
#             mode='markers',
#             marker=dict(
#                 size= 4,
#                 color = 'gold',
#                 opacity = .8,
#             ),
#           )]
# #set the layout to plot
# layout = go.Layout(autosize=False,
#                    mapbox= dict(accesstoken="Ypk.eyJ1IjoiZ2FycmV0dDQzMTEiLCJhIjoiY2sxcXhuZDEwMDF4ajNjczBrcDlnbDdubCJ9.ZCAz1yq24OiZ6o9wV2N_pw",
#                                 bearing=10,
#                                 pitch=60,
#                                 zoom=13,
#                                 center= dict(lat=40.721319,
#                                              lon=-73.987130),
#                                 style=shaz13_custom_style),
#                     width=900,
#                     height=600, 
#                     title = "Earthquakes")

# fig = dict (data=data, layout=layout)
latitude=[]
longitude=[]
fig = go.Figure(go.Scattermapbox(
        lat=latitude.append(train['latitude']),
        lon=longitude.append(train['longitude']),
        mode='markers',
        marker=dict(
          size = 4,
          color = 'green',
          opacity = .8
        )
    ))

fig.update_layout(
    autosize=True,
    hovermode='closest',
    mapbox=go.layout.Mapbox(
        accesstoken=mapbox_access_token,
        bearing = 0,
        center=go.layout.mapbox.Center(
            lat=38.92,
            lon=-77.07
        ),
        pitch=0,
        zoom=10
    ),
)
plotly.offline.plot(fig, image_filename='test')