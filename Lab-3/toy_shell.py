#!/usr/bin/env python3

import os
import time
from datetime import datetime

def list_items_older_than(date_input):
    try:
        target_date = datetime.strptime(date_input, "%Y-%m-%d").timestamp()
        items = os.listdir('.')
        items.sort(key=os.path.getmtime)
        found = False
        for item in items:
            item_time = os.path.getmtime(item)
            if item_time < target_date:
                item_type = "Folder" if os.path.isdir(item) else "File"
                formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item_time))
                print(f"{item} ({item_type}, Last Modified: {formatted_time})")
                found = True
        if not found:
            print("No files or folders older than this date.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

def toy_shell():
    print("Toy Shell: List files and folders older than a given date")
    print("Enter a date in the format YYYY-MM-DD or type 'exit' to quit.")
    while True:
        try:
            command = input("toy-shell> ").strip()
            if command.lower() == "exit":
                print("Exiting toy shell.")
                break
            list_items_older_than(command)
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit the shell.")

if __name__ == "__main__":
    toy_shell()
