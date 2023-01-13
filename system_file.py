import sys
import random
import time

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/ishan/Downloads"


class FileEventHandler(FileSystemEventHandler) :

    def on_created(self, event) :
        print(f"Hey!, I have created {event.src_path} for you.")

    def on_deleted(self, event) :
        print(f"Oops!, I think somone have deleted {event.src_path}.")

    def on_modified(self, event) :
        print(f"Hey! there, I a have modified {event.src_path} for you.")

    def on_moved(self, event) :
        print(f"Hey!, someone moved {event.src_path} to {event.dest_path}")


event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try :
    while True:
        time.sleep(2)
        print("runnning.....")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()


