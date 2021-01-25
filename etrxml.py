import requests
from lxml import etree  # lxml 是c语言的库，效率非常高


url = 'http://movie.douban.com'
headers = {'User-agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/55.0.2883.75 Safari/537.36"}
response = requests.get(url, headers=headers)

with response:
    if response.status_code == 200:
        text = response.text
        print(text)
        html = etree.HTML(text)
        print(html)

        titles = html.xpath('//div[@class="billboard-bd"]//a/text()')
        for title in titles:
            print(title)

        print("*********************")