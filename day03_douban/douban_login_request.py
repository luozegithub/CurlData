import requests
import html5lib
import re
from bs4 import BeautifulSoup
session = requests.Session
s = requests.session()
url_login = 'https://www.douban.com/accounts/login'
url_contacts = ''

formdata = {
    'redir': 'https://www.douban.com/',
    # 'source': 'index_nav',
    'form_email': '',
    'form_password': '',
    'login': u'登陆'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36'
}

r = s.post(url_login, data=formdata, headers=headers)
print(r)
# content = r.content
content = r.content.decode('utf-8')

'''
<img id="captcha_image" src="https://www.douban.com/misc/captcha?id=NH9RoR9g0VFMmiFmCTZVJcQc:en&amp;size=s" alt="captcha" class="captcha_image"/>
<div class="captcha_block">
  <span id="captcha_block"  class="pl">请输入上图中的单词</span>
  <input type="text" id="captcha_field" name="captcha-solution" tabindex=3 placeholder="验证码" />
  <input type="hidden" name="captcha-id" value="NH9RoR9g0VFMmiFmCTZVJcQc:en"/>
'''

soup = BeautifulSoup(content, 'html5lib')
captcha = soup.find('img', id='captcha_image')
if captcha:
    captcha_url = captcha['src']
    re_captcha_id = r'<input type="hidden" name="captcha-id" value="(.*?)"/>'
    captcha_id = re.findall(re_captcha_id, content)
    print(captcha_url)
    print(captcha_id)
    captcha_text = input('Please input the captcha :')
    formdata['captcha-solution'] = captcha_text
    formdata['captcha-id'] = captcha_id
    logincontent = s.post(url_login, data=formdata, headers=headers).content.decode('utf-8')
    print(logincontent)

with open('./content.txt', 'w+', encoding='utf-8') as f:
    f.write(r.text)
