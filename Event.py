class Event:

    def __init__(self, user, date, start_time,  end_time, event_description, eventId, isRecurring, recur):
        self.user = user
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.event_description = event_description
        self.event_accept_reject_status = None
        self.eventId = eventId
        self.isRecurring = isRecurring
        self.recur = recur

    def accept_event(self):
        self.event_accept_reject_status = True

    def reject_event(self):
        self.event_accept_reject_status = False


