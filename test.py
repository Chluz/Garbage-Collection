from ics import Calendar
import requests

url = "https://service.stuttgart.de/lhs-services/aws/api/ical?street=Hau%C3%9Fmannstr.&streetnr=12"

c = Calendar(requests.get(url).text)

c
# <Calendar with 118 events and 0 todo>
c.events
# {<Event 'Visite de "Fab Bike"' begin:2016-06-21T15:00:00+00:00 end:2016-06-21T17:00:00+00:00>,
# <Event 'Le lundi de l'embarqué: Adventure in Espressif Non OS SDK edition' begin:2018-02-19T17:00:00+00:00 end:2018-02-19T22:00:00+00:00>,
#  ...}
#print(list(c.timeline))
#for event in list(c.timeline):
#e = list(c.timeline)[0]
#    print("Event '{}' started {}".format(event.name, event.begin.humanize()))
# "Event 'Workshop Git' started 2 years ago"


class myCalendar:

    def __init__(self, path):
        from django.core.validators import URLValidator
        from django.core.exceptions import ValidationError
        val = URLValidator()
        try:
            val(path)
        except ValidationError:
            print('Provided URL is not valid')

    def getCalendar(self):
        from collections import defaultdict
        cal = Calendar(requests.get(url).text)
        self.event_dict = defaultdict(list)
        for event in list(cal.timeline):
            self.event_dict[event.name].append(event.begin)

    def printEvents(self, specific_event=None):
        if specific_event is not None:
            key_list = [specific_event]
        else:
            key_list = self.event_dict.keys()
        for event_title in key_list:
            print("Event '{}' will occur on :".format(event_title))
            for event_date in self.event_dict[event_title]:
                print(str(event_date))

myCal = myCalendar(url)
myCal.getCalendar()
myCal.printEvents()
myCal.printEvents(specific_event = 'Restmüll 02-wöchentl.')
