from Event import Event
class Calender:

    def __init__(self):
        self.list_events = []

    def addEvent(self, user, event_date, start_time, end_time, event_description, eventId, isRecurring, recur, db):
        event = Event(user, event_date, start_time, end_time, event_description, eventId, isRecurring, recur)
        self.list_events.append(event)
        db.map_events[eventId] = event


    def showCalender(self):

        for event in self.list_events:
            print(event)

        return self.list_events
