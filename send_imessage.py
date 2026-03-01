import sys
import subprocess
import re
from pathlib import Path

DEFAULT_MARKDOWN_PATH = Path("data/awesome_events_README.md")

def send_message(text, recipient):
    escaped_text = text.replace('"', '\\"')
    script = f'''
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy "{recipient}" of targetService
        send "{escaped_text}" to targetBuddy
    end tell
    '''
    subprocess.run(['osascript', '-e', script])

def preprocess_markdown(text):
    text = re.sub(r'`([^`]*)`', r'\1', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1 (\2)', text)
    text = re.sub(r'^#{1,6}\s*', '', text, flags=re.M)
    text = re.sub(r'[*_~>|]', '', text)
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = text.replace('\\', '/').replace('"', "'")
    text = text.encode('ascii', 'ignore').decode()
    return text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python send_imessage.py <recipient>")

    recipient = sys.argv[1]
    events_raw = DEFAULT_MARKDOWN_PATH.read_text()
    events = preprocess_markdown(events_raw)
    send_message(events, recipient)
