from urllib.error import URLError
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener

username = 'username'
password = 'password'
url = 'http://localhost:5000'

# 实例化HTTPBasicAuthHandler对象，参数是HTTPPasswordMgrWithDefaultRealm对象，利用add_password()添加用户名密码，建立处理验证的handler
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
# 利用build_opener()方法构建opener,利用opener的open()方法打开链接完成验证
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
except URLError as e:
    print(e.reason)