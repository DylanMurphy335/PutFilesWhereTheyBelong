from watchdog.observer import observer
from watchdog.events import FileSystemEventHandler
# pip install watchdog for these packages

import os
import json
import time

class MyHandler(FileSystemEventHandler):
	def on_modified(self, event):
		for filename in os.listdir(folder_to_track):
			src = folder_to_track + "/" + filename
			new_destination = folder_destination + "/" + filename
			os.rename(src, new_destination)

folder_to_track = "Users/dylan/Downloads"
folder_destination = "Users/dylan/Documents"
event_handler = MyHandler()
observer = observer()
observer.schdule(event_handler, folder_to_track, recursive=true)
observer.start()

try:
	while True:
		time.sleep(10)
except KeyboardInterrupt:
	observer.stop()
observer.join()
