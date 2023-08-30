import argparse
from timetable_parser import TimetableParser
from class_scheduler import ClassScheduler
from google_calendar import GoogleCalendarManager

def main():
    parser = argparse.ArgumentParser(description="Automated Class Scheduler")
    parser.add_argument('--extract', action='store_true', help='Extract timetable from image')
    args = parser.parse_args()

    if args.extract:
        image_path = 'timetable.jpeg'
        extracted_text = extract_text_from_image(image_path)
        timetable_parser = TimetableParser(extracted_text)
        parsed_events = timetable_parser.parse_extracted_text()

        google_calendar = GoogleCalendarManager('credentials.json', 'token.json')
        for event in parsed_events:
            start_time = event['day'] + 'T' + event['start_time']
            end_time = event['day'] + 'T' + event['end_time']
            google_calendar.create_event('Class', start_time, end_time)

    google_calendar = GoogleCalendarManager('credentials.json', 'token.json')
    events = google_calendar.get_events()
    scheduler = ClassScheduler(events)
    scheduler.open_classes()

if __name__ == "__main__":
    main()