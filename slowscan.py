#coding:utf-8
import requests
import time
import sys

with open('D:/backup/document/bug/python/slowscan/dicc.txt','r',encoding='UTF-8') as dic:
    for dirs in dic.readlines():
        url="https://www.target.com"+dirs.strip('\n')
        resp=requests.get(url)
        strlen=len(resp.text)
        print(url+'---'+str(resp.status_code)+'---'+str(strlen))
        if(resp.status_code==200 or resp.status_code==403 or resp.status_code==301 or resp.status_code==500):
            with open('D:/backup/document/bug/python/slowscan/write.txt','a',encoding='UTF-8') as writefile:
                writefile.write(url+'---'+str(resp.status_code)+'---'+str(strlen)+'\n')
        time.sleep(0.5)
