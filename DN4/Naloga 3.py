import requests

def html(povezava):
    sintaksa = requests.get(povezava, headers={"User-Agent": "Requests"}).content
    print(sintaksa)

html('https://www.rtvslo.si/iskalnik?q=iskalni%20niz')