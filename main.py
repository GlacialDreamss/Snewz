import requests as rq

class response():
    response = rq.get("https://api.steampowered.com")

    print(response.status_code)