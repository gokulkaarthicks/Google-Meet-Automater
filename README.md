# Google Meet Automator

Automate joining Google Meet classes based on your timetable and Google Calendar events.

## Setup

1. Clone the repository to your local machine:

```sh
git clone https://github.com/your-username/google-meet-automator.git
cd google-meet-automator
```
2. Install the required dependencies:

```sh
pip install -r requirements.txt
```
3. Schedule the script to run daily :

```sh
1. Edit the cron jobs using crontab -e.
2. Add a new cron job to run the script every day 
at your desired time.
3. For example, to run at 10 AM:
0 10 * * * /usr/bin/python3 ~/main.py
4. Save it.
```
"Lets end things."