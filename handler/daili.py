from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener
# 本地搭建代理，使用ProxyHandler参数是字典，利用handler和build_opener()构造opener，发送请求
proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1:9743'
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)