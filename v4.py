from urllib import request, parse
'''
掌握对url进行参数编码的方法
需要使用parse模块
'''
if __name__ == '__main__':
    url = "https://www.baidu.com/s?"
    wd = input("请输入的你的关键字")
    #想要使用data,需要使用字典结构
    qs = {
        "wd": wd
    }
    #转换url编码
    qs = parse.urlencode(qs)
    print(qs)
    fullurl = url + qs
    print(fullurl)
    rsp = request.urlopen(fullurl)
    html = rsp.read()
    #使用get取值保证不会出错
    html = html.decode()
    print(html)