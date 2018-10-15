import requests
import urllib3

# 引入urllib3的设置忽略警告的方式屏蔽警告
urllib3.disable_warnings()
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)