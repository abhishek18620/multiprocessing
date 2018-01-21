# Whats more interesting than Fucking SwimSuit Illustrated Models images...Haha;)
# Let's start multitasking with some web scraping
# I'll scrape through my router page and grab active clients with all  information possible
# coding: UTF-8
try:
    from urllib import request as req
    from urllib.request import URLError
except ImportError:
    print("Couln't find Urllib.Request , will use urllib2")
    import urllib3 as req

import sys
from bs4 import BeautifulSoup as bs
import json
import time #for timings of download and fetching
import requests
print("Import Succesfull")
class Scraper():
    def __init__(self,parent=None):
        self.websites=[]
        print("HI")
    def download_page(self,url):
        try:
            headers={}
            headers["User-Agent"]='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0'
            prereq=req.Request(url,None,headers=headers)
            #print(prereq)
            requ=req.urlopen(prereq)
            resp=requ.read().decode()
            #print(type(resp))
            return self.CleanHtml(resp)
            #f.write(resp)
        except:
            print("page not found")
        #f.write(print(resp))

    def CleanHtml(self,html):
        try:
            return bs(html,'html.parser')
        except:
            print(" BS Error ")


class HtmlEditor():
    def __init__(self,parent=None):
        self.url="https://www.si.com/swimsuit/models"
        fout=open("output.txt",'w')
        fhtml=open("html.txt",'w')
        scrape=Scraper()
        clean=scrape.download_page(self.url)
        try:
            #fhtml.write(str(clean))
            for data in clean.findAll('a' , {"class" : "tile-image"}):
                self.url="https://www.si.com"+data.get('href')
                print("Fetching url = {0}......" .format(self.url))
                cleanedchild=scrape.download_page(self.url)
                fhtml.write(str(cleanedchild))
                # ctr = 0
                # while True:
                    # try:
                        # ctr=ctr+1
                        # new_url=self.url + '#' + str(ctr)
                        # print("Fetching url = {0}......" .format(new_url))
                        # photos = scrape.download_page(new_url)
                        # fhtml.write("ctr  = \n\n\n {0}\n\n" .format(ctr))
                        # fhtml.write(str(photos))
                    # except:
                        # print("BS Error")
                        # break
        except:
            print("BS Error")
if __name__=='__main__':
    obj=HtmlEditor()

