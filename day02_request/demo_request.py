import requests

# 测试请求 以及查看返回的状态
'''
reponse=requests.get('http://www.baidu.com')
print(reponse)
# print(reponse.text)
print(reponse.content.decode('utf-8'))
print(reponse.encoding)
'''

# 传参请求
'''
params = {'key1': 'value1', 'key2': [1,2,3]}
response = requests.get('http://httpbin.org/get', par ams)
print(response.url)
'''
# 根据图片地址，保存图片（二进制文件转化）
'''
from PIL import Image
from io import BytesIO
responese=requests.get('http://files.jb51.net/file_images/article/201406/2014060309205215.jpg')
content是二进制数据，text是已经转化后的数据
image=Image.open(BytesIO(responese.content))
image.save('./picture/lvbu.jpg')
'''

# json处理
'''
r = requests.get('http://github.com/timeline.json')
print(r)
print(r.text)
'''

# 原始数据处理(以流的方式处理文件)
'''
responese = requests.get('http://files.jb51.net/file_images/article/201406/2014060309205215.jpg')
with open('./picture/lvbu2.jpg', 'wb+') as f:
    for chunk in responese.iter_content(1024):
        f.write(chunk)
'''
# 提交表单
'''
import json
form = {'username': 'user', 'password':'pass'}
# print(json.dumps(form))
response = requests.post('http://httpbin.org/post',data=json.dumps(form))
# 根据传入值的类型决定赋值的对象，如果传入的是dic，默认我form  如果是json，默认为data
# response = requests.post('http://httpbin.org/post',data=form)
print(response.text)
'''

'''
{"args":{},"data":"{\"username\": \"user\", \"password\": \"pass\"}","files":{},"form":{},"headers":{"Accept":"*/*","Accept-Encoding":"gzip, deflate","Connection":"close","Content-Length":"40","Host":"httpbin.org","User-Agent":"python-requests/2.18.4"},"json":{"password":"pass","username":"user"},"origin":"110.16.82.246","url":"http://httpbin.org/post"}
'''

# cookie
'''
url = 'http://www.baidu.com'
response = requests.get(url)
cookies = response.cookies
for k, v in cookies.get_dict().items():
    print(k, v)
'''

'''
cookies = {'k1': 'v1', 'k2': 'v2'}
response = requests.get('http://httpbin.org/cookies', cookies=cookies)
print(response.text)
'''

# 重定向和重定向历史
'''
response = requests.head('http://github.com', allow_redirects=True)
print(response.url)
print(response.status_code)
print(response.history)
'''

