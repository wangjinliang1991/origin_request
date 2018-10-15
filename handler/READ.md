# handler用法，利用handler构建Opener

## 验证
* 借助HTTPBasicAuthHandler

## 代理
* ProxyHandler

## 问题
* 每次都显示[WinError 10061] 由于目标计算机积极拒绝，无法连接
    + 网上方案： 1.点开设置-->代理设置-->弹出Internet属性-->局域网设置-->自动检测设置  失败
    + 网上方案： 2.关掉防护墙，卫士等，Chrome权限关闭重启  失败
    
## cookies获取
* 直接输出
* 保存为Mozilla型浏览器的cookies格式.txt
* 保存为LWP格式
> cookies的文件读取，以LWPCookieJar为例