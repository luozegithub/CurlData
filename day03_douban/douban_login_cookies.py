import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36'
}

cookies = {
    'cookies': ''}
url = 'http://www.douban.com'
r = requests.get(url, cookies=cookies, headers=headers)
with open('doubanlogin_cookies.txt', 'w+', encoding='utf-8') as f:
    f.write(r.text)
