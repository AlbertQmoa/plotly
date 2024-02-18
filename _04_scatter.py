'''
    reference: https://www.youtube.com/watch?v=VdCMzpVcsCc&list=PLh3I780jNsiTXlWYiNWjq2rBgg3UsL1Ub&index=10
'''

import pandas as pd     #(version 1.0.0)
import plotly           #(version 4.5.0) #pip install plotly==4.5.0
import plotly.express as px
import plotly.io as pio
import statsmodels.api as sm


# ================== Step 0: Prepare data ==================
tips = px.data.tips()
tips.rename(columns={'size':'tbl_size'}, inplace=True)

#fake margin of error, standard deviation, or 95% confidence interval
tips['err_plus'] = tips['total_bill']/100
tips['err_minus'] = tips['total_bill']/40


# ====== Step 1: use plotly.express to plot a sketch of your figure ====== 
scatterplot = px.scatter(
    data_frame=tips,
    x="total_bill",
    y="tip",

    # ------------ 設置散射點 ------------
    size="tbl_size",                                # 根據 "tbl_size" 的數值調整點的大小
    size_max=13,                                    # 點大小的最大值
    symbol="smoker",                                # 根據 "smoker" 的類別調整點的形狀
    # symbol_sequence=[3,'square-open'],            # 設置點的形狀
    symbol_map={"No": "square-open" ,"Yes":3},      # 設置類別值設定點的形狀

    # ------------ 設置顏色 ------------
    color="day",                                                # 根據 "day" 的類別設定顏色
    opacity=0.5,                                                # 透明度
    color_discrete_map={"Thur": "green" ,"Fri":"red",           # 離散顏色配置
                        "Sat":"black","Sun":"brown"},
    # color_continuous_scale=px.colors.diverging.Armyrose,      # 連續顏色配置（如果顏色是根據連續數值設定）
    # color_continuous_midpoint=2,

    # ------------ 額外資料顯示 ------------
    text='tbl_size',                # 在散射點上顯示數值
    hover_name='time',              # 滑鼠選到散射點上顯示的備註資訊名稱
    hover_data=['time'],            # 滑鼠選到散射點上顯示的備註資訊
    # custom_data=['tbl_size'],     # values are extra data to be used in Dash callbacks

    # ------------ 畫多個散射圖 ------------
    # facet_row='tbl_size',         # assign marks to subplots in the vertical direction
    # facet_col='tbl_size',         # 根據 tbl_size 的數值畫獨立的散射圖
    # facet_col_wrap=3,             # 每個 j 方向的最多散射圖數目

    # ------------ 風格設置 ------------
    # labels={"tip":"the TIP",
    # "smoker":"SMOKER or NOT"},    # map the labels
    # title='All Tips',             # figure title
    # width=500,                    # figure width in pixels
    # height=1000,                  # igure height in pixels
    # template='seaborn',           # 'ggplot2', 'seaborn', 'simple_white', 'plotly',
                                    # 'plotly_white', 'plotly_dark', 'presentation',
                                    # 'xgridoff', 'ygridoff', 'gridon', 'none'

    # ------------ 動畫 ------------
    animation_frame='tbl_size',     # 根據什麼欄位來區分動畫的分鏡圖
    #animation_group=,              # use only when df has multiple rows with same object
    range_x=[5,50],                 # 設定 x 軸範圍
    range_y=[0,10],                 # 設定 y 軸範圍
    category_orders={'tbl_size':[1,2,3,4,5,6]},   # 根據什麼欄位來決定動畫執行的順序。
)


# ====== Step 2: use plotly.graph_objective to refine your figure ======
# Traces represent the data (inside the layout)
# Layout represents the figure (frames, title, color, tick, hover, legend)
scatterplot.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000
scatterplot.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 500


# ====== Step 3: Show and save your figure ======
scatterplot.show()
scatterplot.write_image('images/scatter.png')
