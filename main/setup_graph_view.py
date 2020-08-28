import json
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import get_info
import choose_info

files, metrics, results = choose_info.file, choose_info.metrics, choose_info.results
results_choice = input("Choose index value of one of the following: " + choose_info.results)
metric_choice = input("Choose index value of one of the following: " + choose_info.metrics)
file_choice = input("Choose index value of one of the following: " + choose_info.files)

obj, grouped = choose_info.chooser(results_choice)