import os
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

def Mrank():
    url =requests.get('https://movie.naver.com/movie/running/current.nhn')
    html=url.text
    soup=BeautifulSoup(html, 'lxml')
    result=soup.find_all('dl','lst_dsc')

    moviedata= []

    for temp in result:
        mdata={}
        # 제목
        tdata=temp.find('dt','tit')
        tdata=tdata.find('a').text
        mdata['title']=tdata
        # 평점
        star=temp.find('div','star_t1')
        star=star.find('span','num')
        mdata['star']=star.text
        # 장르
        genre=temp.find('dl','info_txt1')
        genre=genre.find('span','link_txt').text
        genre=genre.replace('\n','').replace('\t','').replace('\r','')
        mdata['genre']=genre
        moviedata.append(mdata)

    imgresult = soup.find_all('div','thumb')
    imgurl = []
    for temp in imgresult:
        url= temp.find('img')
        imgurl.append(url['src'])

    i=0
    for temp in moviedata:
        temp['img']=imgurl[i]
        i+=1

    return moviedata
