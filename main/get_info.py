from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
from google.colab import files
from google.colab import drive

drive.mount('/content/drive')

with open("/content/drive/My Drive/Final Design Doc/results/Final/Offline/offline-sizes_colab.txt", encoding="utf-8") as offline_sizes_file:
    offline_sizes = json.load(offline_sizes_file)
with open("/content/drive/My Drive/Final Design Doc/results/Final/Realtime/realtime-threshold_colab.txt", encoding="utf-8") as realtime_sizes_file:
    realtime_sizes = json.load(realtime_sizes_file)