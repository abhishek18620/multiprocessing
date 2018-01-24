# Whats more interesting than Fucking SwimSuit Illustrated Models images...Haha;)
# Let's start multitasking with some web scraping
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
            headers["User-Agent"]="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0"
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
        #home page
        self.url="https://www.si.com/swimsuit/models"
        self.fout=open("output.txt",'w')
        self.fhtml=open("html.txt",'w')
        self.scrape=Scraper()
        self.Years_extractor()

    def Years_extractor(self):
        clean=self.scrape.download_page(self.url)
        try:
            #fhtml.write(str(clean))
            #read pages for each model
            for data in clean.findAll('a' , {"class" : "tile-image"}):
                self.url="https://www.si.com"+data.get('href')
                print("\n\nHead url for model = {0}" .format(self.url))
                cleanedchild=self.scrape.download_page(self.url)
                #read specific year's shoots for each model
                #self.fhtml.write(str(cleanedchild))
                state=False
                for subdata in cleanedchild.find_all("div" , class_ = "model-years"):
                    state=True
                    for a in subdata.find_all('a'):
                    #print(subdata.find('a')["href"])
                        singleurl=self.url + a.get("href")
                        #print("Fetching url = {0}     ......" .format(singleurl))
                        self.image_link_generator(singleurl)

                if not state:
                    #print("Fetching url = {0}     ......" .format(self.url))
                    self.image_link_generator(self.url)

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

    def image_link_generator(self,link):
        ctr=1
        while True:
            link = link + '#' + str(ctr)
            print("Fetching url = {0}     ......" .format(link))
            clean=self.scrape.download_page(link)
            if not clean:
                break
            ctr=ctr+1
            self.fhtml.write(str(clean))


if __name__=='__main__':
    obj=HtmlEditor()

