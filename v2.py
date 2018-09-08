import urllib
from urllib import request
import chardet
'''
利用request下载网页
自动检测页面编码
'''

if __name__ == '__main__':
    url = "https://blog.csdn.net/zhengyikuangge/article/details/71106778"
    rsp = urllib.request.urlopen(url)
    html = rsp.read()

    #利用 chardet自动检测
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)
    #使用get取值保证不会出错
    html = html.decode(cs.get("encoding", "utf-8"))
    print(html)