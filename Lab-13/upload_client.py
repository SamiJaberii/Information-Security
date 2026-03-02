import requests

URL = "http://127.0.0.1:8080/upload"

with open("sample_log.txt", "rb") as f:
    files = {"file": ("sample_log.txt", f, "text/plain")}
    r = requests.post(URL, files=files, timeout=10)

print("Status:", r.status_code)
print("Response:", r.json())
