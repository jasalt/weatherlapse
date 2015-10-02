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

    # HACK for current youtube playlist name format
    daynum = vid_title[4:].split('.')[0]
    if len(daynum) == 1:
        daynum = '0' + daynum
    daystr = "2015-07-" + daynum
    strparts = daystr.split('-')

    year, month, day = int(strparts[0]), int(strparts[1]), int(strparts[2])

    if not daily_videos.get(year):
        daily_videos[year] = {}
    if not daily_videos[year].get(month):
        daily_videos[year][month] = {}

    try:
        daily_videos[year][month][day] = vid['pafy']

    except:
        print("Cant add " + vid_title)
