from icalendar import Calendar, Event
from datetime import timedelta, date
from pytz import UTC # timezone

class FileICal(object):
    def __init__(self, path):
        data = open(path).read()
        self._cal = Calendar.from_ical(data)
        self._events = []
        for item in self._cal.walk("VEVENT"):
            self._events.append(item)

    def getEventsNextWeek(self):
        events = []
        nextweek = date.today() + timedelta(days=20)
        today = date.today()
        for event in self._events:
            try:
                eventdate = event["DTSTART"].dt.date()
            except AttributeError:
                eventdate = event["DTSTART"].dt
            if nextweek > eventdate >= (today):
                events.append(event)
        return events

    def formWallMessage(self, events):
        messages = []
        for event in events:
            stringi = "Please keep in mind that the Event %s will hapen on Cam on the %s" % \
                      (event['SUMMARY'], event["DTSTART"].dt.strftime("%d.%m"))
            messages.append(stringi)
        return messages