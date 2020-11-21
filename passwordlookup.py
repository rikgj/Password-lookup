import urllib.request, urllib.error, urllib.parse
import hashlib


testlist = ["testpassword","mygoodpass23","leetpass1337","password"]
sha1list = []
hitlist = []


for test in testlist:
    m = hashlib.sha1()
    test = test.encode('utf-8')
    m.update(test)
    sha1list.append(m.hexdigest().upper())


baseURL = 'https://api.pwnedpasswords.com/range/'
count = 0

for hash in sha1list:
    url = baseURL + hash[0:5]
    response = urllib.request.urlopen(url)
    webContent = response.read()
    content = webContent.decode('ASCII')

    f = open('passwordlookup_dump.txt',"w")
    f.write(content)
    f.close()

    f = open('passwordlookup_dump.txt',"r")
    lines = f.readlines()
    found = False
    i = 0
    limit = len(lines)
    while found == False and i < limit:
        line = lines[i]
        pair = line.split(":")

        if(pair[0] == hash[5:]):
            hit = [testlist[count], int(pair[1])]
            hitlist.append(hit)
            found = True
        i+=1
    count+=1

print(hitlist)
