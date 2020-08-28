import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import setup_graph_view as setup
import get_info
import choose_info

setup()
files, metrics, results, grouped, file_choice, metric_choice, obj = setup.file, setup.metrics, setup.results, setup.grouped, setup.file_choice, setup.metric_choice, setup.obj
#creates graph for trends with metric_choice and results_choice
fig = px.line(obj,title= metrics[metric_choice][1] + " values for UGC Dataset", x="actual-bitrate-bps",y=metrics[metric_choice][1], color="encoder", facet_col = "input-file",\
              hover_name= "encoder", facet_col_wrap = 4, width=1650, height=3000)

#Updates graph legend layout to be more legible
fig.update_xaxes(matches=None)
fig.update_xaxes(showticklabels=True)
fig.update_yaxes(matches=None)
fig.update_yaxes(showticklabels=True)
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.005,
    xanchor="right",
    x=1
))
# Make titles of graphs more concise
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))