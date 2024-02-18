import pandas as pd
import plotly.express as px


# ================== Step 0: Prepare data ==================
the_years = ["1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003",
             "2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"]

df = pd.read_csv("data/Gender_StatsData.csv")
df = df[(df["Indicator Name"]=="Expected years of schooling, female")|\
        (df["Indicator Name"]=="Expected years of schooling, male")]
df = df.groupby(["Country Name","Country Code","Indicator Name"], as_index=False)[the_years].mean()
# print(df[:10])

world=["Arab World","South Asia","Latin America & Caribbean","East Asia & Pacific","European Union"]
world_xrange=[4,19]

# asia_latin_years = ["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"]

# europe=["Bulgaria","Romania","Denmark","France","Hungary"]
# africa=["Malawi","Egypt, Arab Rep.","Mauritania","Morocco","Lesotho"]
# arab=["Jordan","Oman","Qatar","Tunisia","Syrian Arab Republic"]
# asia_central=["India","Iran, Islamic Rep.","Mongolia","Tajikistan","Uzbekistan"]
# latin_caribb=["El Salvador","Mexico","Argentina","Cuba","Chile"]

# europe_xrange=[10,20]
# africa_xrange=[2,15]
# arab_xrange=[6,17]
# asia_central_xrange=[6,16]
# latin_caribb_xrange=[10,19]

# ------------------------------------------------------------------------------
# Choose dataframe Region and sort column
df = df[df['Country Name'].isin(world)]
df['Country Name'] = pd.Categorical(df['Country Name'], ['South Asia','Arab World','East Asia & Pacific',
                                                         'Latin America & Caribbean',"European Union"])
df.sort_values("Country Name", inplace=True)

df = pd.melt(df,id_vars=['Country Name','Country Code','Indicator Name'],var_name='Year',value_name='Rate')
# print(df[:20])


# ====== Step 1: use plotly.express to plot a sketch of your figure ====== 
# 這段代碼的目的是通過一個互動式的動畫散點圖來展示不同國家在不同年份的教育性別差距情況，並通過動畫的形式展示這些差距隨時間的變化。
# 這種圖表對於展示和探索時間序列數據非常有用，尤其是當數據涉及多個維度（如國家、時間、性別指標）時。
fig = px.scatter(df, x="Rate", y="Country Name", color="Indicator Name", animation_frame="Year",
                 range_x=world_xrange, range_y=[-0.5,5.0],
                 title="Gender Gaps in our Education",
                 labels={"Rate":"Years a child is expected to spend at school/university",
                        "Indicator Name":"Gender"} # customize label
      )


# ====== Step 2: use plotly.graph_objective to refine your figure ======
# Traces represent the data (inside the layout)
# Layout represents the figure (frames, title, color, tick, hover, legend)
# 圖表標題（title）
    # x: 指定標題在圖表中的水平位置，0.5 表示標題位於圖表的中央。
    # xanchor: 與 x 屬性配合使用，'center' 確保標題根據指定的 x 位置水平居中對齊。
    # font: 指定標題的字體設置，這裡設置字體大小為 20。
# X軸標題（xaxis）
    # 為x軸標題設定字體大小為 20。這裡沒有明確指定x軸標題的文本，只是對其字體大小進行了設定。
# Y軸標題（yaxis）
    # 這行代碼將y軸標題的文本設置為 None，意味著y軸不顯示標題文本。
# 圖例（legend）
    # 設置圖例中文字的字體大小為 18。
    # 同時也為圖例標題（如果有的話）設定了字體大小為 18。
fig.update_layout(title={'x':0.5,'xanchor':'center','font':{'size':20}},
                  xaxis=dict(title=dict(font=dict(size=20))),
                  yaxis={'title':{'text':None}},
                  legend={'font':{'size':18},'title':{'font':{'size':18}}})


# 動畫設定
    # 這兩行代碼設定了圖表動畫的兩個關鍵參數：
    # frame['duration']：設定每個動畫幀切換的持續時間為800毫秒。這影響動畫播放的速度，使得每次幀的更新間隔為800毫秒。
    # transition['duration']：設定動畫過渡效果的持續時間為800毫秒。這影響從一幀過渡到另一幀的平滑程度和速度。
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 800
fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 800

# 數據系列命名（# fig.data 的詳細說明請見 _00_info.md）
    # 這兩行代碼將圖表中的第一個和第二個數據系列（通常對應於不同的數據組或類別）分別命名為「Girl」和「Boy」。
    # 這影響圖例（legend）中顯示的名稱，幫助使用者識別不同的數據系列。
fig.data[0].name = 'Girl'
fig.data[1].name = 'Boy'
fig.data[0]['marker'].update(size=14)
fig.data[1]['marker'].update(size=14)
fig.data[0]['marker'].update(color='#22bc22')
fig.data[1]['marker'].update(color="#fda026")

# for x in fig.frames:：遍历图表 fig 中的所有动画帧。
# x.data[0]['marker']['color'] = '#22bc22'：对每个帧中的第一个数据系列，更新其标记的颜色为绿色 '#22bc22'。
# x.data[1]['marker']['color'] = '#fda026'：对每个帧中的第二个数据系列，更新其标记的颜色为橙色 '#fda026'。
for x in fig.frames:
    x.data[0]['marker']['color'] = '#22bc22'
    x.data[1]['marker']['color'] = '#fda026'


# ====== Step 3: Show your figure ======
fig.show()