# Codec-Analysis-Tool
This tool was created in colab, and is to be used in conjuncion with [The Google AV1 Codec Analysis Tool](https://github.com/googleinterns/av1-codec-comparison "Go to Github")

## Libraries Needed
- pandas
- plotly.express
- matplotlib.pyplot

## How to Run
- install libraries mentioned above
- change the file paths in get info, as well as new results, metrics and files if added in choose_info.py
- run one of graph_view_single, or graph_view_multi
- after running generate_graphs.py in the Google Codec Analysis tool, take the output text and make the following changes:
  - replace all singular quotes with double quotes ( ' -> ")
  - delete the hanging comma at the end of the file, usually between the last } and the ] 
  - wrap the whole file using {"data": (FILE_CONTENTS) } to make it a valid JSON format
