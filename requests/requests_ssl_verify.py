import requests

# 避免证书错误，verify=False
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)
