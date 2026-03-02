#!/Library/Frameworks/Python.framework/Versions/3.14/bin/python3
from datetime import datetime

output_file = "/Users/samijabery/Desktop/Information-Security/Lab-7/cron_output.txt"

with open(output_file, "a") as f:
    f.write(f"Cron ran at {datetime.now()}\n")

