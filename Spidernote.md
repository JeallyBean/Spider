# 爬虫
- 步骤
    - 下载网页
    - 提取正确的信息
    - 根据一定规则自动跳到另外的网页上去执行上两步
- 爬虫分类
    - 通用爬虫
    - 专用爬虫（聚焦爬虫）
# 2.urllib
- 包含模块
    - urllib.request:打开和读取urls
    - urllib.error:包含urllib.request产生常见的错误,使用try捕捉
    - urllib.parse:包含解析url的方法
    - urllib.robotparse:解析robots.txt文件
-网页编码问题的解决
    -  charset 可以自动检测页面文件的编码格式
- urlopen
    - geturl:返回请求对象的url
    - info:请求反馈
    - getcode:返回的http code
    