import urllib.request, urllib.error, urllib.parse
import hashlib

# FIXME: adapt inputlist (testlist) such that reading passwords downloaded from chrome is easy
#        however it should still be possible to lookup typing a few words the way it is now
# FIXME: make a menu
# FIXME: graphical presentation of the result
# FIXME: lookup simelar words, upper-/lowercase and such
#       make sure that a password is not presented twice in the result doing this,
#       however a count might be appropriate



testlist = []
sha1list = []
hitlist = []

f = open('Chrome-passord.csv',"r")
lines = f.readlines()
for line in lines:
    line = line.rstrip()
    testlist.append(line)

print(testlist)

# f = open('testlist.csv',"r")
# lines = f.readlines()
# for line in lines:
#     line = line.rstrip()
#     line = line.split(",")
#     for l in line:
#         testlist.append(l)


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

    f = open('dump.txt',"w")
    f.write(content)
    f.close()

    f = open('dump.txt',"r")
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

if len(hitlist) == 0:
    print("all is good")
else:
    print(hitlist)
