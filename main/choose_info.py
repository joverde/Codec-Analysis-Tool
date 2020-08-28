results = [(0,offline_sizes), (1,"realtime_sizes"), (2, "realtime_threshold")]

# Change metric_choice to pick specific feature to visualize below, based on index value (ex. to choose vmaf, metric_choice = 15)
metrics = [(0, 'vpx-ssim'), (1, 'ssim'), (2, 'ssim-y'), (3, 'ssim-u'), (4, 'ssim-v'), (5, 'avg-psnr'), (6, 'avg-psnr-y'), (7, 'avg-psnr-u'), (8, 'avg-psnr-v'), (9, 'glb-psnr'), 
    (10, 'glb-psnr-y'), (11, 'glb-psnr-u'), (12, 'glb-psnr-v'), (13, 'encode-time-utilization'), (14, 'actual-encode-time-ms'), (15, 'vmaf')]

# Change file_choice to pick specific feature to visualize below, based on index value (ex. to choose 'Animation_480P-52af.mkv', file_choice = 0)
files = [(0, 'Animation_480P-52af.mkv'), (1, 'Animation_480P-6e23.mkv'), (2, 'Animation_480P-6ff4.mkv'), (3, 'Animation_480P-7114.mkv'), (4, 'Animation_480P-7ef2.mkv'), (5, 'CoverSong_480P-2142.mkv'), 
(6, 'CoverSong_480P-7f6d.mkv'), (7, 'Gaming_480P-14fc.mkv'), (8, 'Gaming_480P-1542.mkv'), (9, 'Gaming_480P-5a5a.mkv'), (10, 'Gaming_480P-6a5a.mkv'), (11, 'Gaming_480P-7893.mkv'), 
(12, 'HowTo_480P-187c.mkv'), (13, 'HowTo_480P-48ac.mkv'), (14, 'HowTo_480P-64a2.mkv'), (15, 'HowTo_480P-7579.mkv'), (16, 'Lecture_480P-4bc3.mkv'), (17, 'Lecture_480P-7eec.mkv'), 
(18, 'LyricVideo_480P-1484.mkv'), (19, 'LyricVideo_480P-4346.mkv'), (20, 'MusicVideo_480P-3aa2.mkv'), (21, 'MusicVideo_480P-4802.mkv'), (22, 'MusicVideo_480P-4cc8.mkv'), 
(23, 'MusicVideo_480P-5461.mkv'), (24, 'MusicVideo_480P-7955.mkv'), (25, 'NewsClip_480P-31bd.mkv'), (26, 'NewsClip_480P-41b1.mkv'), (27, 'NewsClip_480P-6615.mkv'), 
(28, 'Sports_480P-19e4.mkv'), (29, 'Sports_480P-3404.mkv'), (30, 'Sports_480P-41a5.mkv'), (31, 'TelevisionClip_480P-19d3.mkv'), (32, 'TelevisionClip_480P-280f.mkv'), 
(33, 'VerticalVideo_480P-1bb9.mkv'), (34, 'VerticalVideo_480P-3a6a.mkv'), (35, 'VerticalVideo_480P-5168.mkv'), (36, 'VerticalVideo_480P-7278.mkv'), (37, 'Vlog_480P-5dfe.mkv'), 
(38, 'Vlog_480P-5ebd.mkv'), (39, 'Vlog_480P-7237.mkv')] 

def chooser(results_choice):
    #convert results to json and group results by input file
    data = results[results_choice][1]
    obj = pd.json_normalize(data["data"])
    obj = obj.sort_values(by=["input-file","actual-bitrate-bps"])
    grouped = obj.groupby("input-file")
    return obj,grouped
   

# Only run when new set of files are generated and a new constant list is needed.
def generate_file_names():
  for name,info in grouped:
    groups.append((len(groups),name))
  print(groups)

    

