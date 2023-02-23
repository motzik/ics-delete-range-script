from ics import Calendar, Event
import arrow
import os.path
from os import path

# path to ics file
filePath = ""
savePath = ""

# dateRange in format <YYYY-MM-DD>
# all events in this range remain in the ics file, all the others are deleted
# keep in mind that the events are only filtered by begin date when using events that are lasting longer than one day 
rangeBegin = "2023-03-01"
rangeEnd = "2023-09-30"

#override the destination file if it exists
overrideSaveFile = False


file = open(filePath)

c = Calendar(file.read())
print(file.name)

arrowBegin = arrow.get(rangeBegin)
arrowEnd = arrow.get(rangeEnd)

print("old Events: " + str(len(c.events)))
newEvents = set()
for x in c.events:
    if(x.begin < arrowEnd and x.begin > arrowBegin):
        newEvents.add(x)

print("new Events: " + str(len(newEvents)))

c.events = newEvents
if(os.path.exists(savePath) and overrideSaveFile == False):
    print("Destination file already exists, please configure the overrideSaveFile parameter or change the destination file path")
elif (os.path.exists(savePath)):
    open(savePath,"w").writelines(c)
else:
    open(savePath,"x").writelines(c)
