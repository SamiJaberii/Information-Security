#!/usr/bin/env python3

import os
import time
from datetime import datetime

OUTPUT_FILE = "toy_shell_output.txt"

def write_line(line: str):
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def list_items_older_than(date_input: str):
    try:
        target_date = datetime.strptime(date_input, "%Y-%m-%d").timestamp()
        items = os.listdir(".")
        items.sort(key=os.path.getmtime)

        found_any = False
        lines = []

        for item in items:
            item_time = os.path.getmtime(item)
            if item_time < target_date:
                item_type = "Folder" if os.path.isdir(item) else "File"
                formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item_time))
                line = f"{item} ({item_type}, Last Modified: {formatted_time})"
                print(line)
                lines.append(line)
                found_any = True

        if not found_any:
            msg = "No files or folders older than this date."
            print(msg)
            lines.append(msg)

        write_line("========================================")
        write_line(f"Run Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        write_line(f"Input Date: {date_input}")
        for line in lines:
            write_line(line)

    except ValueError:
        msg = "Invalid date format. Please use YYYY-MM-DD."
        print(msg)
        write_line("========================================")
        write_line(f"Run Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        write_line(f"Input Date: {date_input}")
        write_line(msg)

def toy_shell():
    print("Toy Shell: List files and folders older than a given date")
    print("Enter a date in the format YYYY-MM-DD or type 'exit' to quit.")
    print(f"Output will be saved to: {OUTPUT_FILE}")

    while True:
        try:
            command = input("toy-shell> ").strip()
            if command.lower() == "exit":
                print("Exiting toy shell.")
                write_line("========================================")
                write_line(f"Session ended: {time.strftime('%Y-%m-%d %H:%M:%S')}")
                break
            list_items_older_than(command)

        except KeyboardInterrupt:
            print("\nUse 'exit' to quit the shell.")
            write_line("========================================")
            write_line(f"Session interrupted: {time.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    toy_shell()
