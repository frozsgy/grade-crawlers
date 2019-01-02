import requests
import re
import os
import platform
import time

#regex search pattern
pattern='<tr><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td>'
pattern='<tr><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>'

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
#written file format: id,lastname,firstname,dept,mt1,mt2s
#reads from mt1 file, and uses the first 7 digits as student id's
try:
    f=open("219.csv", "r")
    ids=[]
    for line in f:
        ids.append(int(line[:7]))
    fn=open("219mt2.csv","a")
except:
    print "I cannot open 219.csv, please check permissions, OR I'LL DIE LIKE RIGHT NOW"
    exit()

def requestIt(headers,data):
    try:
        response=requests.post('http://ma219.math.metu.edu.tr/SIS/sis.php', headers=headers, data=data)
    except:
        print "Let's sleep a bit, baba yorgun"
        time.sleep(15)
        response=requests.post('http://ma219.math.metu.edu.tr/SIS/sis.php', headers=headers, data=data)
    return response

fn.write("ID,LASTNAME,FIRSTNAME,DEPT,MT1,MT2\n")
for i in ids:
    data={
      'id': i,
      'Submit': 'Show Info'
    }
    if not i % 100:
        print "Started new section: ", i

    response=requestIt(headers,data)

    temp=re.findall(pattern, response.content)
    if(len(temp) > 1):
        temp=temp[1]
        print temp[0], "-", temp[2], temp[1], "imported"
        fn.write(temp[0]+","+temp[1]+","+temp[2]+","+temp[3]+","+temp[5]+","+temp[12]+"\n")

print "That's all folks!"
