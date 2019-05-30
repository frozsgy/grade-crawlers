 # -*- coding: iso8859-9 -*-
import requests
import re
import os
import platform
import time

#regex search pattern
pattern='<td>BONUS <\/td><\/tr><tr><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><\/tr>'

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
    fn=open("219fin30excel.csv","a")
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

def ctoint(x):
    if x == '':
        return 0
    else :
        return float(x.replace(",","."))

fn.write("ID;LASTNAME;FIRSTNAME;SECT;FIN;MT2;MT1;BONUS;TOTAL;NORM;AVG;STD\n")
students=[]
line=1
for i in ids:
    data={
      'id': i,
      'Submit': 'Show Info'
    }
    if not i % 100:
        print "Started new section: ", i

    response=requestIt(headers,data)

    temp=re.findall(pattern, response.content)
    if(len(temp) == 1):
        temp=temp[0]
        print temp[0], "-", temp[2], temp[1], "imported"
        totalisc=ctoint(temp[29])+0.3*(ctoint(temp[27])+ctoint(temp[22]))+0.4*ctoint(temp[11])
        students.append((temp[0],temp[1],temp[2],temp[3],temp[11],temp[22],temp[27],temp[29],totalisc))
        line+=1
print "\nDownloaded all the data, now doing stat magic... \n"
sts=sorted(students, key=lambda x: x[8], reverse=True)
wh=1
for i in sts:
    if(i[8] > 10) :
        wh+=1
    else :
        break
l=2
for i in sts:
    nn="\"=NORM.DAĞ(I"+str(l)+";K"+str(l)+";L"+str(l)+";YANLIŞ)\""
    av="=ORTALAMA(I2:I"+str(wh)+")"
    std="=STDSAPMA.P(I2:I"+str(wh)+")"
    totalis="=E"+str(l)+"*0,4"+"+(F"+str(l)+"+G"+str(l)+")*0,3+H"+str(l)
    fn.write(i[0]+";"+i[1]+";"+i[2]+";"+i[3]+";"+i[4]+";"+i[5]+";"+i[6]+";"+i[7]+";"+totalis+";"+nn+";"+av+";"+std+"\n")
    l+=1
print "\nMicrosoft Excel should be able to read your csv file happily, give it a go;) \n"
print "You can create a normal distribution graph using the I'th and J'th columns, until the "+str(wh)+"'th line, since it's the latest grade that is greater than 10.\n"
print "That's all folks!"
