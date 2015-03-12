import requests
r = requests.get("http://www.sina.com.cn")
s = r.content
img_list = []
count = 0
src_list = []
while 1:
    of = s.find("<img")
    if of > -1:
        count += 1
        s = s[of+4:]
        e = s.find(">")
        img_list.append("img" + s[:e+1])
    else:
        break
print len(img_list)
print"-----------------------------" 
#s1 = img_list[0]
#of = s1.find("data-src")
#s1 = s1[of+10:]
#e = s1.find('"')
#print s1[:e]

for s1 in img_list:
    of = s1.find("data-src")
    if of > -1:
        s1 = s1[of+10:]
        e = s1.find('"')
        src_list.append(s1[:e])
    else:
        of = s1.find("src")
        s1 = s1[of+5:]
        e = s1.find('"')
#        if s1[:e] not in src_list:
        src_list.append(s1[:e])
print len(src_list)
print len(list(set(src_list)))#ШЅжи
#img_list.append("img" + s[:e+1])
 
