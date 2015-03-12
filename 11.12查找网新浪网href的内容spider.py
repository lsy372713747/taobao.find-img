
#coding utf-8
import requests
url = "http://www.sina.com.cn"
url_list = [url]
def spider(url):
    r = requests.get(url)
    for a in r.content.split("<a")[1:]:
        temp = a.split(">")[0]
        if "href" in temp:
            url_list.append(temp.split('href="')[1].split('"')[0])
for a in url_list:
    print a
    print len(url_list)
    try:
        spider(a)
    except:
        pass

