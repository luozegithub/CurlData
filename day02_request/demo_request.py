import requests

# 测试请求 以及查看返回的状态
# reponse=requests.get('http://www.baidu.com')
# print(reponse)
# # print(reponse.text)
# print(reponse.content.decode('utf-8'))
# print(reponse.encoding)

# 传参请求
# params = {'key1': 'value1', 'key2': [1,2,3]}
# response = requests.get('http://httpbin.org/get', par ams)
# print(response.url)

# 根据图片地址，保存图片（二进制文件转化）
# from PIL import Image
# from io import BytesIO
# responese=requests.get('http://files.jb51.net/file_images/article/201406/2014060309205215.jpg')
# content是二进制数据，text是已经转化后的数据
# image=Image.open(BytesIO(responese.content))
# image.save('./picture/lvbu.jpg')

# json处理
r=requests.get('http://github.com/luoze')
print(r)
print(r.text)
print(r.json)
print(r.text)
