import requests

# 先拿到二进制码content
r = requests.get("https://github.com/favicon.ico")
print(r.content)
# 保存用open()方法，第二个参数用二进制写
with open('favicon.ico', 'wb') as f:
    f.write(r.content)