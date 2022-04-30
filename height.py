import pandas as pd
import plotly.figure_factory as pff
df=pd.read_csv("data.csv")
r=df["Avg Rating"].tolist()
fig = pff.create_distplot([r],["Avg Rating"],show_hist=True)
fig.show()