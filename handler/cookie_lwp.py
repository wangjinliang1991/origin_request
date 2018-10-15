import http.cookiejar
import urllib.request

# MozillaCookieJar是CookieJar的子类，处理Cookies和文件相关的事件，读取和保存cookies,为Mozilla浏览器的Cookie格式
filename = 'cookies_lwp.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)