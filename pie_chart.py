'''
    A basic pie chart will sum the vlaues according to the names respectively 
    and then show the percetage of each names.
    reference: https://www.youtube.com/watch?v=_b2KXL0wHQg&list=PLh3I780jNsiTXlWYiNWjq2rBgg3UsL1Ub&index=1
'''

import pandas as pd
import plotly.express as px

df = pd.read_csv('data/bird-window-collision-death.csv')


# ====== Step 1: use plotly.express to plot a sketch of your figure ====== 
# https://plotly.com/python-api-reference/generated/plotly.express.pie.html#plotly.express.pie
fig = px.pie(df, values='Deaths', names='Bldg #', color='Side', hole=0.3)


# ====== Step 2: use plotly.graph_objective to refine your figure ======
# Traces represent the data (inside the layout)
# Layout represents the chart (frames, title, color, tick, hover, legend)
fig.update_traces(textinfo='label+percent', insidetextfont={'color':'white'})
fig.update_layout(legend={'itemclick':False})

# ====== Step 3: Show and save your figure ======
fig.show()

fig.write_image('images/pie.png')