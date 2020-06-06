import sys
import requests


r = requests.get("https://www.google.com.au")
print(r.status_code)
