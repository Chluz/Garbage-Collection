from aws import myCalendar

url = "https://service.stuttgart.de/lhs-services/aws/api/ical?street=Hau%C3%9Fmannstr.&streetnr=12"

myCal = myCalendar(url)
myCal.getCalendar()
#myCal.printEvents()
myCal.printEvents(specific_event = 'Restmüll 02-wöchentl.', force_update = True)

theevnt,thedate = myCal.getNextDate('Restmüll 02-wöchentl.')
print("Next DAteeeeeeeee")

print(thedate.day)
