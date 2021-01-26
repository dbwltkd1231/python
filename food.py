import requests
from bs4 import BeautifulSoup
import csv
import os
def smu():
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
    url="https://www.smu.ac.kr/lounge/notice/notice.do?mode=list&&articleLimit=10&srCampus=smu&article.offset=0"
    res=requests.get(url,headers=headers)
    res.raise_for_status()
    print(res.status_code) #200이면정상
    soup = BeautifulSoup(res.text, "lxml")

    
    data1=soup.find_all("dl",attrs={"board-thumb-content-wrap board-thumb-content-wrap-v01 noti"})
    for row in data1:
        rows=row.find_all("td")
        data=[rows2.get_text().strip() for rows2 in rows]
        print(data)
    
def computer():
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
    url="https://cs.smu.ac.kr/cs/community/notice.do"
    res=requests.get(url,headers=headers)
    res.raise_for_status()
    print(res.status_code) #200이면정상
    soup = BeautifulSoup(res.text, "lxml")
    data1=soup.find_all("dl",attrs={"class":"board-thumb-content-wrap board-thumb-content-wrap-v01 noti"})
    for row in data1:
        rows=row.find_all("dt")
        data=[rows2.get_text().strip() for rows2 in rows]
        print(data)
   
    #with open("smu_notice.html", "w", encoding='utf8')as f:
        #f.write(res.text)

def eco():
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
    url="https://econo.smu.ac.kr/economic/community/notice.do"
    res=requests.get(url,headers=headers)
    res.raise_for_status()
    print(res.status_code) #200이면정상
    soup = BeautifulSoup(res.text, "lxml")
    data1=soup.find_all("dl",attrs={"class":"board-thumb-content-wrap board-thumb-content-wrap-v01 noti"})
    for row in data1:
        rows=row.find_all("dt")
        data=[rows2.get_text().strip() for rows2 in rows]
        print(data)
    
print("경제학과")
eco()
print("통합공지")
smu()
print("컴퓨터과학과")
computer()

os.system('pause')
#soup=BeautifulSoup(res.text,"lxml") #해당사이트를 beautiful 객체로만듬
#print(soup.title)
#print(soup.find(attrs={"class":"root mt16 pl10"}))