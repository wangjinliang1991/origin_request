from urllib import request,error
# HTTPError专门处理HTTP请求错误，三个属性reason,code,headers
try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
