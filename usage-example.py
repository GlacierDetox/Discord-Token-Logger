import requests

web_url = "" # Your api url

r = requests.post(web_url, headers={"token": token})
print(r.status_code)
print(r.json())
