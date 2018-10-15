import requests
# 文件上传部分单独有个files字段来标识
files = {'file': open('favicon.ico', 'rb')}
r = requests.post("http://httpbin.org/post", files=files)
print(r.text)