from calender import FileICal
from calfacebook import FaceBookPoster

cal = FileICal("./basic.ics")

events = cal.getEventsNextWeek()
facebook = FaceBookPoster("./facebook.token")
messages = cal.formWallMessage(events)
for item in messages:
    facebook.post_to_wall(item)

