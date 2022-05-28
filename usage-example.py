import requests

r = requests.post("https://elementaryprevioussymbol.terimaarankichw.repl.co", headers={"token": token})
print(r.json())
print(r.status_code)
