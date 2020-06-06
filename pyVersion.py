import sys
import requests


print(sys.version)
print(sys.executable)

r = requests.get("https://www.google.com.au")
print(r.status_code)
