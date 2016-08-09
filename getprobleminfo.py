import urllib2,re,urllib,cookielib,socket,codecs
from HTMLParser import HTMLParser
'''cookie'''
cookiejar=cookielib.CookieJar()
cookieproc=urllib2.HTTPCookieProcessor(cookiejar)
opener=urllib2.build_opener(cookieproc)

timeout=15
socket.setdefaulttimeout(timeout)

Max_Num=10

def get(url,headers=False):
    if headers:
        req=urllib2.Request(url,headers=headers)
    else:
        req=urllib2.Request(url)
    for i in range(Max_Num):
        try:
            page=opener.open(req,timeout=20).read()
            try:
                page=page.decode('utf-8')
            except:
                page=page.decode('gbk','ignore')
            return page
            break
        except Exception,ex:
            if i<Max_Num-1:
                continue
            else:
                print Exception,ex

def post(url,postdata,headers=False):
    if headers:
        req=urllib2.Request(url,postdata,headers)
    else:
        req=urllib2.Request(url,postdata)
    for i in range(Max_Num):
        try:
            page=opener.open(req,timeout=20).read()
            #print '41'+page
            try:
                page=page.decode('utf-8')
            except:
                page=page.decode('gbk','ignore')
            return page
            break
        except Exception,ex:
            if i<Max_Num-1:
                continue
            else:
                print Exception,ex                    
print 'input your username:'
username=raw_input()
print 'input your password:'
password=raw_input()
print 'input your output path'
path=raw_input()
path=path+'info.txt'
url='http://acm.tju.edu.cn/toj/list.php?vol=1'

par={
    'user_id':      '781595099',
    'passwd':       '781595099',
    'login':        '+Login+'
}
page=post(url,urllib.urlencode(par))
#print page
data=re.findall('(?<=p\()(.*)(?=\))',page)
#print data

f=codecs.open(path,'a','utf-8')
for i in range(1,len(data)):
    f.write(data[i])
    f.write('\n')
i=2
url='http://acm.tju.edu.cn/toj/list'+str(i)+'.html'
page=get(url)
#print page
while (i < 33):
    url='http://acm.tju.edu.cn/toj/list'+str(i)+'.html'
    page=get(url)
    data=re.findall('(?<=p\()(.*)(?=\))',page)
    for j in range(1,len(data)):
        f.write(data[j])
        f.write('\n')
    i=i+1
print('finished')
