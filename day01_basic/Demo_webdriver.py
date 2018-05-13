from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get('http://www.17huo.com/newsearch/?k=%E7%94%B5%E8%84%91')
time.sleep(3)
# browser.find_element_by_css_selector('body > div.boot_mask > div').click()

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

page_info = browser.find_element_by_css_selector(
    'body > div.wrap > div.search_container > div.pagem.product_list_pager > div')
# 共 40 页，每页 60 条
pages = int((page_info.text.split('，')[0]).split(' ')[1])
for page in range(pages):
    if page != 0:
        url = 'http://www.17huo.com/newsearch/?k=%E7%94%B5%E8%84%91&page=' + str(page + 1)
        browser.get(url)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    goods = browser.find_element_by_css_selector(
        'body > div.wrap > div.search_container > div.book-item-list.clearfix').find_elements_by_class_name(
        'book-item-list-box')
    i = 1
    print('第%d页，该页共有%d条数据' % (page + 1, len(goods)))
    for good in goods:
        print((i, good.text))
        i += 1

browser.close()
