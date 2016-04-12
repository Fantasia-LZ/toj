import urllib2,os
print 'please put your toj code in the dictory of the submitcode.py, the name fo code must like "Problem 1001 - Hello, world!.cpp"'
print 'input your id'
#user_id=raw_input()
print 'input your password'
#passwd=raw_input()
i=0
for files in os.listdir(os.getcwd()):
    try:

        f=file(files)
    except Exception,e:
        print e
"""
prob_id='1003'
f=file('demo.cpp')
code=f.read()
boundary='----WebKitFormBoundaryIzegM8dr5vB9iM2A'
data=[]
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="user_id"\r\n')
data.append(user_id)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="passwd"\r\n')
data.append(passwd)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="prob_id"\r\n')
data.append(prob_id)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="language"\r\n')
data.append('1')
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="source"\r\n')
data.append(code)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="MAX_FILE_SIZE"\r\n')
data.append('32768')
data.append('Content-Disposition: form-data; name="userfile"; filename=""')
data.append('Content-Type: application/octet-stream\r\n')
data.append('\r\n')
data.append('--%s--\r\n'%boundary)
httpBody='\r\n'.join(data)

print type(httpBody)
print httpBody

headers={
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryIzegM8dr5vB9iM2A',
    'User_Agent':   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
}
postDataUrl='http://acm.tju.edu.cn/toj/submit_process.php'
req=urllib2.Request(postDataUrl,data=httpBody,headers=headers)
page=urllib2.urlopen(req).read().decode('utf-8')
print page
"""
