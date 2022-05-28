import requests

web_url = "" # Your api url

r = requests.post(web_url, headers={"token": token})
print(r.json())
print(r.status_code)
