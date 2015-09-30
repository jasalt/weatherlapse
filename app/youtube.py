## TODO handle videos for multiple months
# daily_videos dict contains videos by day.

import pafy

# TODO import app key
# pafy.set_api_key(key)

print("Loading Youtube video playlist")
playlist = pafy.get_playlist("PLy7eek8wTbV9OtrbY3CJo5mRWnhuwTen0")
videos = playlist['items']
daily_videos = {}

for vid in videos:
    vid_title = vid['playlist_meta']['title']
    day = vid_title[4:].split('.')[0]
    try:
        daily_videos[int(day)] = vid['pafy']
    except:
        print("Cant add " + vid_title)
