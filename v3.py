import urllib
from urllib import request
import chardet


if __name__ == '__main__':
    url = "https://blog.csdn.net/zhengyikuangge/article/details/71106778"
    rsp = urllib.request.urlopen(url)
    print(type(rsp))
    print(rsp)
    print("URL:{0}".format(rsp.geturl()))
    print("Info:{0}".format(rsp.info()))
    print("Code:{0}".format(rsp.getcode()))
    html = rsp.read()