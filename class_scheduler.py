import webbrowser
import datetime

class ClassScheduler:
    def __init__(self, events):
        self.events = events

    def open_classes(self):
        current_time = datetime.datetime.utcnow().isoformat() + 'Z'
        for event in self.events:
            if event['start_time'] <= current_time <= event['end_time']:
                for subject in event['subjects']:
                    classroom_link = classroom_links.get(subject, None)
                    if classroom_link:
                        webbrowser.open(classroom_link)
                break
