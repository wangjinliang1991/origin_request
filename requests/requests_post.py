import requests

data = {'name': 'jinliang','age': '27'}
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)