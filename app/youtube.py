# Load data for videos in Youtube playlist
# Uses video title as date, formatted as 20151230

## TODO handle videos for multiple months
# all_videos dict contains videos by day.

import pafy
from datetime import datetime

# TODO import app key
# pafy.set_api_key(key)

print("Loading Youtube video playlist")

playlist = pafy.get_playlist("PLXSngHQzQiiI8DyrElGi_N_rv-8ToJvIT")
videos = playlist['items']
all_videos = {}

for vid in videos:
    # Date is stored in video title
    vid_date_str = vid['playlist_meta']['title']
    
    vid_day = datetime.strptime(vid_date_str, "%Y%m%d")
    
    year, month, day = vid_day.year, vid_day.month, vid_day.day

    if not all_videos.get(year):
        all_videos[year] = {}
    if not all_videos[year].get(month):
        all_videos[year][month] = {}

    try:
        all_videos[year][month][day] = vid['pafy']
    except:
        print("Cant add " + vid_date_str)
