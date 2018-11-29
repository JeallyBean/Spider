"""
利用parse模块模拟post请求
分析百度词典
分析步骤:
1. 打开F12
2. 尝试输入单词girl,发现敲一个字母后都有请求
3. 请求地址是http://fanyi.baidu.com/sug
4.利用NetWork-All-Hearders,查看,发现FormData的值是kw:girl
5.检查返回格式,发现返回的是json格式内容==>需要json包
"""

from urllib import request, parse
import json
"""
大致的流程是:
1. 利用data构造内容,然后urloprn打开
2. 返回一个json的结果
3. 结果应该是解释的意思
"""

baseurl = 'https://fanyi.baidu.com/sug'

# 存放用来模拟form的数据一定是dict格式
data = {
    'kw': 'girl'

}

# 需要使用parse模块对data进行编码
data = parse.urlencode(data).encode("utf-8")
# 我们需要构造一个请求头,至少应该包含传入数据的长度
# request要求传入的请求头是一个dict格式
headers = {
    # 使用post,至少包含content-length字段
    'Content-Length': len(data)
}

# 有了headers,data,url,就可以尝试发出请求了

rsp = request.urlopen(baseurl, data=data)
json_data = rsp.read().decode('utf-8')
print(json_data)
# 把json字符串转化成字典
json_data = json.loads(json_data)
print(json_data)
for item in json_data['data']:
    print(item['k'], "--", item['v'])
