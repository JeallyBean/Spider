
from urllib import request
'''
使用urllib.request请求一个网页,把内容打印
'''
if __name__ == '__main__':
    url = "http://www.baidu.com"
    # 打开相应url并且把相应页面作为返回
    rsp = request.urlopen(url)
    html = rsp.read()
    #读取出的是bytes内容
    html = html.decode()
    print(html)
