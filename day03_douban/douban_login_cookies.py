import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36'
}

cookies = {
    'cookies': 'bid=Nm9v-6V4OJw; ps=y; ue="1007557275@qq.com"; dbcl2="178657335:OCkHhI6ovHA"; ck=hhEH; push_noty_num=0; push_doumail_num=0; __utmc=30149280; __utmz=30149280.1527080753.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=30149280.17865; _pk_ses.100001.8cb4=*; __utma=30149280.1241439531.1527080753.1527080753.1527084569.2; _pk_id.100001.8cb4=ed93024ad048120e.1527080752.2.1527085826.1527080752.; __utmt=1; __utmb=30149280.58.10.1527084569; ap=1'}
url = 'http://www.douban.com'
r = requests.get(url, cookies=cookies, headers=headers)
with open('doubanlogin_cookies.txt', 'w+', encoding='utf-8') as f:
    f.write(r.text)
