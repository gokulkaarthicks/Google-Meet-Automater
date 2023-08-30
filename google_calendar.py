from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import datetime

class GoogleCalendarManager:
    def __init__(self, credentials_path, token_path):
        self.credentials_path = credentials_path
        self.token_path = token_path
        self.SCOPES = ['https://www.googleapis.com/auth/calendar']
        self.service = self._get_calendar_service()

    def _get_calendar_service(self):
        flow = InstalledAppFlow.from_client_secrets_file(self.credentials_path, self.SCOPES)
        creds = flow.run_local_server(port=0)
        with open(self.token_path, 'w') as token:
            token.write(creds.to_json())
        return build('calendar', 'v3', credentials=creds)

    def create_event(self, summary, start_time, end_time):
        event = {
            'summary': summary,
            'start': {
                'dateTime': start_time,
                'timeZone': 'UTC',
            },
            'end': {
                'dateTime': end_time,
                'timeZone': 'UTC',
            },
        }
        event = self.service.events().insert(calendarId='primary', body=event).execute()
        print(f'Event created: {event.get("htmlLink")}')
