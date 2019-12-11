import plotly
import pandas as pd
import plotly.graph_objs as go

#mapbox token and style
mapbox_style = "mapbox://styles/garrett4311/ck1s78co60uht1crol6lxs6fr"
mapbox_access_token = "pk.eyJ1IjoiZ2FycmV0dDQzMTEiLCJhIjoiY2s0MXB1Z2wzMDNiYjNscDl6MjFwMmZzMSJ9.D6D5ioEr74VEgbdHtDlm2A"

#read volcano csv
volc = pd.read_csv('/Users/garrettmorris/Desktop/volcanoes.csv')

#store all relevant volcano data in lists
PEI = volc['properties/PEI']
lat = volc['properties/Latitude']
lon = volc['properties/Longitude']

#lists to hold top 3 PEIs
worstVolc = []

for x in range(len(PEI)):
    #fill list if less than 3 values
    if len(worstVolc) < 3:
        worstVolc.append([PEI[x], lat[x], lon[x]])
    else:
        lowestPEI = worstVolc[0][0]
        lowestIndex = 0
        for y in range(len(worstVolc)):
            if worstVolc[y][0] < lowestPEI:
                lowestPEI = worstVolc[y][0]
                lowestIndex = y

        if PEI[x] > lowestPEI:
            del worstVolc[lowestIndex]
            worstVolc.append([PEI[x], lat[x], lon[x]])

data1 = [go.Scattermapbox(
            lat= [worstVolc[0][1]],
            lon= [worstVolc[0][2]],
            mode='markers',
            marker=dict(
                size= 4,
                color = 'red',
                opacity = .8,
            ),
          )]

data2 = [go.Scattermapbox(
            lat= [worstVolc[1][1]],
            lon= [worstVolc[1][2]],
            mode='markers',
            marker=dict(
                size= 4,
                color = 'orange',
                opacity = .8,
            ),
          )]

data3 = [go.Scattermapbox(
            lat= [worstVolc[2][1]],
            lon= [worstVolc[2][2]],
            mode='markers',
            marker=dict(
                size= 4,
                color = 'yellow',
                opacity = .8,
            ),
          )]

layout = go.Layout(autosize=True,
                   mapbox= dict(accesstoken= mapbox_access_token,
                        bearing=0,
                        pitch=0,
                        zoom=5,
                        center= dict(lat=0,lon=0),
                        style=mapbox_style),
                    width=1500,
                    height=1080,
                    title = "Arm2")

fig = dict (data=data1+data2+data3, layout=layout)
plotly.offline.plot(fig, image_filename='Arm2.html')