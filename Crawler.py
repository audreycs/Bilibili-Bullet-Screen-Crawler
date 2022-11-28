#coding:utf-8

import re
import sys
import requests
import  xml.dom.minidom
import os

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
}

def spider(av):
    url = 'https://bilibili.com/video/av' + str(av)

    # Print video address
    print("video address:" + url)

    # Whether this address can be reached
    r = requests.get(url, headers = head, timeout=5)
    code = r.status_code
    if code == 200: 
	    print("Address is valid.")
    else:
	    print("Address is invalid!")
        #print("Program exists!")
	    sys.exit(2)

    # Get the source code of the web page
    html = requests.get(url, headers = head)

    # Write into the source code of the web page
    fw = open(dirpath + "htmlcont.txt","w",encoding="utf-8")
    fw.write(html.text)
    fw.close()

    print("Obtaining the source code of the video page successfully!")

    fr = open(dirpath + "htmlcont.txt","r",encoding="utf-8")
    line = fr.readline()
    while line:
        matchstr = re.search(r"cid=([0-9]*)&aid=",line)
        if matchstr!= None:
            fr.close()
            print("Successfully obtained the bullet screen!")
            return matchstr.group(1)
        line = fr.readline()
        
def getcomments(cid):
    comment_url = 'http://comment.bilibili.com/'+str(cid)+'.xml'
    print("file:"+comment_url)

    html = requests.get(comment_url)
    with open(dirpath + cid + ".xml", "wb") as code:
        code.write(html.content)

    url = dirpath + str(cid)+".xml"
    dom = xml.dom.minidom.parse(url)
    root = dom.documentElement
    comments = root.getElementsByTagName('d')
    print("Parse the contents of the bullet screen...")
    f.writelines("Time(s)"+","+"Comment"+"\n")
    for i in range(len(comments)):
        item = comments[i]
        attrs = item.getAttribute("p")
        time = attrs.split(",")[0]
        comment = comments[i].firstChild.data
        f.writelines(str(int(float(time)))+","+comment.split(",")[0]+"\n")


if __name__ == '__main__':
    av = input('Enter video number:')
    dirpath = "./av"+av+"/"

    if not os.path.exists(dirpath):
        os.mkdir(dirpath)

    # Crawl video web page source files
    comment_id = spider(av)

    f = open(dirpath + comment_id + '.csv', 'w', encoding='utf-8')
    getcomments(comment_id)
    print("End!")
