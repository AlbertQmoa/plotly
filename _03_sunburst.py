'''
    reference: https://www.youtube.com/watch?v=6OMKTl7RKjQ&list=PLh3I780jNsiTXlWYiNWjq2rBgg3UsL1Ub&index=4
    Notes:
        Sunburst 圖，或稱為旭日圖，是一種用於數據可視化的圓形層次結構圖，它可以有效地展示數據的層次結構和比例大小。
        Sunburst 圖由多個環狀層組成，每個環代表數據層次結構中的一級，從中心向外擴展，越靠近中心的是上層級，越靠近邊緣的是下層級。
        這種圖表特別適合於展示包含父子關係的樹狀數據。
'''


import plotly.express as px
import pandas as pd
import numpy as np


# ================== Step 0: Prepare data ==================
df = pd.read_csv("data/MPVDataset.csv")
df["Victim's age"] = pd.to_numeric(df["Victim's age"], errors='coerce').fillna(0).astype(np.int64)
df.rename(columns={'Fleeing (Source: WaPo)': 'Fleeing'}, inplace=True)

df = df[df["State"].isin(['NY', 'CA', 'TX'])]
df = df[df["Victim's race"].isin(["White", "Black", "Hispanic", "Asian"])]


# ====== Step 1: use plotly.express to plot a sketch of your figure ====== 
fig = px.sunburst(
    data_frame=df,
    path=["Unarmed", 'State', "Victim's race"],  # Root, branches, leaves
    maxdepth=-1,                # 参数用于控制旭日圖中呈现的層次深度。maxdepth=-1 顯示所有層次。

    # ------------ 設置顏色 ------------
    color="Unarmed",
    color_discrete_sequence=px.colors.qualitative.Pastel,
    # color="Victim's age",
    # color_continuous_scale=px.colors.sequential.BuGn,
    # range_color=[10,100],

    # ------------ 額外資料顯示 ------------
    hover_name="Unarmed",               # 當用戶將鼠標懸停在圖表的某個部分時，顯示為提示信息的主要標籤。
    hover_data={'Unarmed': False},      # 當用戶將鼠標懸停在圖表的某個部分時，要顯示什麼資料
    title="7-year Breakdown of Deaths by Police",
    template='ggplot2',                 # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
    #                                   # 'plotly_white', 'plotly_dark', 'presentation',
    #                                   # 'xgridoff', 'ygridoff', 'gridon', 'none'
)


# ====== Step 2: use plotly.graph_objective to refine your figure ======
# Traces represent the data (inside the layout)
# Layout represents the figure (frames, title, color, tick, hover, legend)
fig.update_traces(textinfo='label+percent entry')
fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))


# ====== Step 3: Show and save your figure ======
fig.show()
fig.write_image('images/sunburst.png')