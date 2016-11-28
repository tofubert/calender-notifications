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
        target = date.today() + timedelta(days=3)
        for event in self._events:
            try:
                eventdate = event["DTSTART"].dt.date()
            except AttributeError:
                eventdate = event["DTSTART"].dt
            if target == eventdate:
                events.append(event)
        return events

    def formWallMessage(self, events):
        messages = []
        for event in events:
            if event["STATUS"] != "CONFIRMED":
                continue
            stringi = "Please keep in mind that the Event %s will happen on Cam on the %s.\n" % \
                      ( event['SUMMARY'], event["DTSTART"].dt.strftime("%d.%m"))
            if event["DTSTART"].dt.strftime("%H.%M") == "00.00":
                stringi = stringi + " This will be an all day event.\n"
            else:
                stringi = stringi + " Start: %s End: %s\n" % \
                                    (event["DTSTART"].dt.strftime("%H.%M %d.%m.%y"),
                                     event["DTEND"].dt.strftime("%H.%M %d.%m.%y"))
            try:
                stringi = stringi + " Location: %s"% event["LOCATION"] + "\n"
            except:
                pass
            try:
                stringi = stringi + "Additional Notes:%s \n"% event['DESCRIPTION']
            except:
                pass
            messages.append(stringi)
        print(messages)
        return messages