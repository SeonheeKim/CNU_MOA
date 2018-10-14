import requests
from bs4 import BeautifulSoup
import urllib.request
import sqlite3
DEPART=0
BOARD=1
TITLE=2
WRITER=3
YEAR=4
MONTH=5
DAY=6
VIEWS=7
LINK=8
urls={}
urls[11] = "http://computer.cnu.ac.kr/index.php?mid=notice" #학사공지
urls[12] = "http://computer.cnu.ac.kr/index.php?mid=gnotice" #일반소식
urls[13] = "http://computer.cnu.ac.kr/index.php?mid=saccord" #사업단소식
urls[14] = "http://computer.cnu.ac.kr/index.php?mid=job" #취업정보
urls[21] = "https://dorm.cnu.ac.kr/_prog/_board/?code=sub05_0501&site_dvs_cd=kr&menu_dvs_cd=0501" #기숙사 은행사
urls[22] = "https://dorm.cnu.ac.kr/_prog/_board/?code=sub05_0506&site_dvs_cd=kr&menu_dvs_cd=0506" #기숙사 백행사

data_list=[]
def id_1x(_url,_board): #컴공 통합
        html=urllib.request.urlopen(_url)
        bs_obj = BeautifulSoup(html, "html.parser")
        times = bs_obj.findAll("td",{"class":"time"})
        titles = bs_obj.findAll("td", {"class": "title"})
        writers=bs_obj.findAll("td",{"class","author"})
        views = bs_obj.findAll("td",{"class","m_no"})
        
        a_href = bs_obj.findAll("td",{"class":"title"})
        links = [td.find("a")['href'] for td in a_href]
        
        print(len(times))
        print(len(titles))
        for i in range(0,len(times)):
            data={}
            data[DEPART]=1
            data[BOARD]=_board
            data[TITLE]=filtering(titles[i].text)
            data[WRITER]=filtering(writers[i].text)
            data[YEAR]=int(filtering(times[i].text[0:4]))
            data[MONTH]=int(filtering(times[i].text[5:7]))
            data[DAY]=int(filtering(times[i].text[8:10]))
            data[VIEWS]=int(filtering(views[i].text))
            data[LINK]=filtering(links[i])
            data_list.append(data)
def id_2x(_url,_board): #기숙사 통합
        html=urllib.request.urlopen(_url)
        bs_obj = BeautifulSoup(html, "html.parser")
        times = bs_obj.findAll("td",{"class":"date"})
        titles = bs_obj.findAll("td", {"class": "title"})
        writers=bs_obj.findAll("td",{"class","center"})
        views = bs_obj.findAll("td",{"class","hits"})
        for td in writers:
                if "\xa0" in td.text:
                        writers.remove(td)
        a_href = bs_obj.findAll("td",{"class":"title"})
        links = [td.find("a")['href'] for td in a_href]
        print(len(times))
        print(len(titles))
        
        for i in range(0,len(times)):
            data={}
            data[DEPART]=2
            data[BOARD]=_board
            data[TITLE]=filtering(titles[i].text)
            data[WRITER]=filtering(writers[i].text)
            data[YEAR]=int(filtering(times[i].text[0:4]))
            data[MONTH]=int(filtering(times[i].text[5:7]))
            data[DAY]=int(filtering(times[i].text[8:10]))
            data[VIEWS]=int(filtering(views[i].text))
            data[LINK]="https://dorm.cnu.ac.kr/_prog/_board" + filtering(links[i][1:])
            data_list.append(data)
        

def save(): # sqlite3 저장
    conn=sqlite3.connect("db.sqlite3")
    with conn:
        cur=conn.cursor()
        cur.execute("DELETE FROM CNU_MOA_crawlingdata")
        conn.commit()
        for data in data_list:
            query="INSERT INTO CNU_MOA_crawlingdata('depart','board','title','writer','link','views','year','month','day') VALUES(?,?,?,?,?,?,?,?,?)"
            cur.execute(query,(data[DEPART],data[BOARD],data[TITLE],data[WRITER],data[LINK],data[VIEWS],data[YEAR],data[MONTH],data[DAY]))
        conn.commit()
        del data_list[:]
def filtering(_str):
    return _str.strip()
def run(): #main에서 주기적으로 호출
    ##컴공
    for i in range(1,5):
        id_1x(urls[10+i],i)
    ##기숙사
    for i in range(1,3):
        id_2x(urls[20+i],i)
    save() 
