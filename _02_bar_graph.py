'''
    reference: https://www.youtube.com/watch?v=N1GwQNatOwo&list=PLh3I780jNsiTXlWYiNWjq2rBgg3UsL1Ub&index=2&t=55s
    Some Notes:
        px.bar 函數創建條形圖時，如果指定的 x 軸是類別型數據，而 y 軸是數值型數據，px 會自動計算每個類別下 y 值的總和。
        換句話說，對於相同的 x 類別值，它們對應的 y 值會被自動累加起來，然後以條形圖的形式展示出來。
'''

import pandas as pd
import plotly
import plotly.express as px
import plotly.io as pio


# ====== Step 0: Prepare data ====== 
df = pd.read_csv('data/Caste.csv')
df = df[df.state_name == 'Maharashtra']
#df = df.groupby(['year', 'gender'], as_index=False)[['detenues', 'under_trial', 'convicts', 'others']].sum()

#fake margin of error, standard deviation, or 95% confidence interval
df['err_plus'] = df['convicts']/100
df['err_minus'] = df['convicts']/40


# ====== Step 1: use plotly.express to plot a sketch of your figure ====== 
barchart = px.bar(
    data_frame=df,
    x='year',               # 類別
    y='convicts',           # 數值
    color='gender',         # 依照 gender 欄位替長條圖上色
    opacity=0.9,            # 長條圖的透明度，0 表示完全透明，1 表示完全不透明
    orientation='v',        # 長條圖方向。 v:垂直; h:水平的; 使用 h 必須調換 x 和 y
    barmode='group',        # 'overlay' : 長條圖會重疊在一起。
                            # 'group'   : 長條圖會並排。
                            # 'relative': 長條圖會疊羅漢。

    # ------------ 依 'caste' 欄位的類型，每種類型畫出一個 "x-y" 的長條圖 ------------
    # facet_row='caste',    # 以 row 方向的形式顯示各類型的長條圖
    facet_col='caste',      # 以 col 方向的形式顯示各類型的長條圖
    facet_col_wrap=2,       # 每個 col 方向最多顯示多少類型。

    # ------------ 設置顏色 ------------
    # color_discrete_sequence=["pink","yellow"],            # 根據 y 類別依序配置顏色
    color_discrete_map={"Male": "gray" ,"Female":"red"},    # 根據 y 類別指定顏色

    # ------------ 額外資料顯示 ------------
    text='convicts',              # 長條圖中顯示數值。也可以顯示其他類別，例如 'gender'。
    hover_name='under_trial',     # 將滑鼠懸停在任何一個條形上時，將看到那一年及性別分類下的被告人數（under_trial 列的值）。
    hover_data=['detenues'],      # 參數用於指定當用戶將滑鼠懸停在圖表的某個點或物件上時，應該顯示哪些額外的資料列。

    # ------------ 統計相關繪圖 ------------
    # log_x=True,                 # x-axis is log-scaled
    # log_y=True,                 # y-axis is log-scaled
    # error_y="err_plus",           # y-axis error bars are symmetrical or for positive direction
    # error_y_minus="err_minus",    # y-axis error bars in the negative direction

    # ------------ 顯示相關 ------------
    labels={"convicts":"Convicts in Maharashtra",
    "gender":"Gender"},           # map the labels of the figure
    title='Indian Prison Statistics', # figure title
    
    template='gridon',            # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
                                  # 'plotly_white', 'plotly_dark', 'presentation',
                                  # 'xgridoff', 'ygridoff', 'gridon', 'none'
    width=1400,                   # figure width in pixels
    height=720,                   # figure height in pixels
    # range_x=[5,50],             # set range of x-axis
    # range_y=[0,9000],           # set range of y-axis

    # ------------ 動畫 ------------
    # animation_frame='year',     # assign marks to animation frames
    # animation_group=,           # use only when df has multiple rows with same object
    # category_orders={'year':    # force a specific ordering of values per column
    # [2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001]},
)


# ====== Step 2: use plotly.graph_objective to refine your figure ======
# Traces represent the data (inside the layout)
# Layout represents the figure (frames, title, color, tick, hover, legend)
barchart.update_layout(uniformtext_minsize=14, uniformtext_mode='hide',
                       legend={'x':0,'y':1.0}),
barchart.update_traces(texttemplate='%{text:.2s}', textposition='outside',
                       width=[.3,.3,.3,.3,.3,.3,.6,.3,.3,.3,.3,.3,.3])


# ====== Step 3: Show and save your figure ======
pio.show(barchart)
barchart.write_image('images/barchart.png')