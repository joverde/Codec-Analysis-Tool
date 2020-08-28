import json
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import setup_graph_view as setup
import get_info
import choose_info

setup()
files, metrics, results, grouped, file_choice, metric_choice, obj = setup.file, setup.metrics, setup.results, setup.grouped, setup.file_choice, setup.metric_choice, setup.obj
fig = px.line(grouped.get_group(files[file_choice][1]),title= "Results for " + files[file_choice][1], x="actual-bitrate-bps",y=metrics[metric_choice][1], color="encoder", hover_name= "encoder")
#Updates graph legend layout to be more legible
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.005,
    xanchor="right",
    x=1
))