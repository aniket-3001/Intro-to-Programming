class Event:
    def __init__(self, name, date, time, location):
        self.name = name
        self.date = date
        self.time = time
        self.location = location

    def update_date_time(self, date, time):
        self.date = date
        self.time = time

    def __str__(self):
        return self.name+" "+self.date+" "+self.time+" "+self.location


class Calendar:
    def __init__(self):
        self.events = {
            "birthdays": [],
            "holidays": [],
            "meetings": [],
            "other": []
        }

    def add_event(self, event, category):
        if category in self.events:
            self.events[category].append(event)

    def get_events(self, date):
        events = []
        for category in self.events:
            for event in self.events[category]:
                if event.date == date:
                    events.append(event)
        return events


if __name__ == "__main__":
    calendar = Calendar()
    event1 = Event("Rahul's Birthday", "12/12/22", "12:00", "Home")
    event2 = Event("Christmas", "25/12/22", "12:00", "Home")
    event3 = Event("Board Meeting", "7/12/22", "17:00", "IIITD")
    event4 = Event("ML Seminar", "12/12/22", "14:00", "IIITD")
    calendar.add_event(event1, "birthdays")
    calendar.add_event(event2, "holidays")
    calendar.add_event(event3, "meetings")
    calendar.add_event(event4, "other")
    query = calendar.get_events("12/12/22")
    for event in query:
        print(event)
