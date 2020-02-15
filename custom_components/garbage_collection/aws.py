class myCalendar:

    def __init__(self, path):
        from django.core.validators import URLValidator
        from django.core.exceptions import ValidationError
        val = URLValidator()
        try:
            val(path)
        except ValidationError:
            print('Provided URL is not valid')
        self.url = path

    def getCalendar(self):
        from ics import Calendar
        import requests
        from collections import defaultdict
        print("Downloading and parsing ICS Calendar")
        self.cal = Calendar(requests.get(self.url).text)
        self.event_dict = defaultdict(list)
        for event in list(self.cal.timeline):
            self.event_dict[event.name].append(event.begin)

    def getNextDate(self, specific_event=None, force_update= False):

        if (not hasattr(self, 'event_dict')) or (force_update is True):
            self.getCalendar()

        if specific_event is not None:
            if specific_event in self.event_dict:
                return specific_event, self.event_dict[specific_event][0]
            else:
                raise ValueError("The requested event name does not exist. "
                                 "Only %s are available."
                                 %', '.join(self.event_dict.keys()))
        else:
            next_event = list(self.cal.timeline)[0]
            return next_event.name, next_event.begin

    def printEvents(self, specific_event=None, force_update= False):

        if (not hasattr(self, 'event_dict')) or (force_update is True):
            self.getCalendar()

        if specific_event is not None:
            key_list = [specific_event]
        else:
            key_list = self.event_dict.keys()
        for event_title in key_list:
            print("Event '{}' will occur on :".format(event_title))
            for event_date in self.event_dict[event_title]:
                print(str(event_date))
