import urllib2
import requests
from bs4 import BeautifulSoup
import os


def main():
    file_object = open('content.txt',"w")

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
    for i in range(1,25):
        '''
        try:
        '''
        if i == 1:
            request = urllib2.Request("http://www.javlibrary.com/cn/vl_mostwanted.php?&mode=")
        else:
            request = urllib2.Request("http://www.javlibrary.com/cn/vl_mostwanted.php?&mode="+"&page="+str(i))
        request.add_header('User-Agent',user_agent)
        respon = urllib2.urlopen(request)
        contents = respon.read()
        start = contents.find("div class=\"video\"")
        while (start != -1):
            astart = contents.find("<a href",start)
            aend = contents.find("title",astart)
            mstart = contents.find('div class="id"',start)
            mend = contents.find('/d',mstart)
            name = contents[mstart+15:mend-1]
            answer = contents[astart+10:aend-2]
            answer = "http://www.javlibrary.com/cn"+answer
            areq = urllib2.Request(answer)
            areq.add_header('User-Agent',user_agent)
            arespon = urllib2.urlopen(areq)
            acon = arespon.read()
            aims = acon.find('<img id="video_jacket_img"')
            aims = acon.find('src="',aims)
            aime = acon.find('"',aims+5)
            asrc = acon[aims+5:aime]
            name = name
            tor = 'https://www.torrentkitty.tv/search/'
            tor = tor + name+'/'
            print tor
            torreq = urllib2.Request(tor)
            torreq.add_header('User-Agent',user_agent)
            torres = urllib2.urlopen(torreq)
            print name
            '''
                os.chdir('/Zhou/scrapy/Himage_mostwant')
                with open(name,'wb') as f:
                    res = urllib2.urlopen(asrc)
                    img = res.read()
                    f.write(img)
                start = contents.find("div class=\"video\"",start+10)
            '''
        '''
        except Exception as e:
            print e
        '''
if __name__ == '__main__':
    main()
