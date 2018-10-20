# 京东APP的爬取，利用Appium和mitmdump

## 目标：  
抓取JDapp的商品信息和评论，一部分是商品信息包括商品ID，名称和图片，另一部分是评论信息，
包括评论人的昵称、评论正文、评论日期和发表图片

## 步骤：
1. Charles抓包分析手机的数据，获取商品详情和商品评论的接口
> 商品详情的接口是cdnware.m.jd.com的链接，返回结果为json字符串，包含商品的ID和商品名称
> 商品评论的接口是api.m.jd.com，包含评论信息
2. mitmdump抓取   
见spider.py
3.  运行脚本
```mitdump -s spider.py```
代理设置到mitmdump上，控制台输出两部分的结果，保存到MongoDB数据库
4. Appium自动化  
Appium对接到手机上，驱动APP点击搜索框、输入商品名、点击进入商品详情、进入评论页面，自动滚动刷新

