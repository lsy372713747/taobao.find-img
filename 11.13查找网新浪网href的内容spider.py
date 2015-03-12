#coding utf-8
import requests
url = "http://www.sina.com.cn"
url_list = [url]
def spider(url):
    r = requests.get(url)
    for a in r.content.split("<a")[1:]:
        temp = a.split('>')[0]
    if "href" in temp:
        url = temp.split('href="')[1].split('"')[0]
        url_list.append(url)
for url in url_list:
    print url
    spider(url)
    time.sleep(5)
