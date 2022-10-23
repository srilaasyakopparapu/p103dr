import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src.path} has been created!")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src.path}!")

    def on_moved(self, event):
        print(f"Hey, {event.src.path} has been moved!")

    def on_modified(self, event):
        print(f"Hey, {event.src.path} has been modified!")

# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()
try:
    while True:
        time.sleep(2)
        print("running...")
    except KeyboardInterrupt:
        print("stopped!")
        observer.stop