class TimetableParser:
    def __init__(self, extracted_text):
        self.extracted_text = extracted_text
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    def parse_extracted_text(self):
        parsed_events = []
        lines = self.extracted_text.strip().split('\n')
        current_day = None
        current_start_time = None
        subjects = []

        for line in lines:
            if line in self.days:
                current_day = line
            elif line.startswith('Batch Details'):
                pass
            elif line.isdigit():
                if current_start_time:
                    end_time = line.split()[1]
                    parsed_events.append({
                        'day': current_day,
                        'start_time': current_start_time,
                        'end_time': end_time,
                        'subjects': subjects
                    })
                    current_start_time = None
                    subjects = []
                else:
                    current_start_time = line.split()[0]
            else:
                subjects.extend(line.split())

        return parsed_events
