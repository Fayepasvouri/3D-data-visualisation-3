"""
faye

"""

import pandas as pd
import numpy as np
timesData = pd.read_csv("C:/Users/Faye/Downloads/timesData.csv")

timesData.info()
timesData.head(10)

df = timesData.iloc[:100,:]

# import graph objects as "go"
from chart_studio.plotly import plot, iplot
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)
import plotly.graph_objs as go
import matplotlib.pyplot as plt

# Creating trace1
trace1 = go.Scatter(
                    x = df.world_rank,
                    y = df.citations,
                    mode = "lines",
                    name = "citations",
                    marker = dict(color = 'rgba(16, 112, 2, 0.8)'),
                    text= df.university_name)
# Creating trace2
trace2 = go.Scatter(
                    x = df.world_rank,
                    y = df.teaching,
                    mode = "lines+markers",
                    name = "teaching",
                    marker = dict(color = 'rgba(80, 26, 80, 0.8)'),
                    text= df.university_name)
data = [trace1, trace2]
layout = dict(title = 'Citation and Teaching vs World Rank of Top 100 Universities',
              xaxis= dict(title= 'World Rank',ticklen= 5,zeroline= False)
             )
fig = dict(data = data, layout = layout)
iplot(fig)

df2016 = timesData[timesData.year == 2016].iloc[:20,:]
num_students_size = [float(each.replace(',','.')) for each in df2016.num_students]
international_color = [float(each) for each in df2016.international]

data = [
    {
        'x' : df2016.world_rank,
        'y' : df2016.teaching,
        'mode' : 'markers',
        'marker' : {
            'color' : international_color,
            'size' : num_students_size,
            'showscale' : True
        },
        'text' : df2016.university_name        
    }
]
iplot(data)
