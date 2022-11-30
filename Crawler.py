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
    print(f"video address: {url}")

    # Whether the video address is valid
    r = requests.get(url, headers = head, timeout=5)
    code = r.status_code
    assert code == 200, "Address is invalid!"

    # Get the source code of the web page
    html = requests.get(url, headers = head)

    # Write the source code
    with open(dirpath + "htmlcont.txt","w",encoding="utf-8") as fw:
        fw.write(html.text)
	print("Obtaining the source code of the video page successfully!")

    # Read the source code
    with open(dirpath + "htmlcont.txt","r",encoding="utf-8") as fr:
        line = fr.readline()
        while line:
            matchstr = re.search(r"cid=([0-9]*)&aid=",line)
            if matchstr!= None:
                print("Successfully obtained the bullet screen!")
                return matchstr.group(1)
            line = fr.readline()
        
def getcomments(cid, dirpath, comment_id):
    comment_url = 'http://comment.bilibili.com/'+str(cid)+'.xml'
    print(f"file: {comment_url}")

    html = requests.get(comment_url)
    with open(dirpath + cid + ".xml", "wb") as code:
        code.write(html.content)

    url = dirpath + str(cid)+".xml"
    dom = xml.dom.minidom.parse(url)
    root = dom.documentElement
    comments = root.getElementsByTagName('d')
    print("Parse the contents of the bullet screen...")

    with open(dirpath + comment_id + '.csv', 'w', encoding='utf-8') as f:
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
    # Parse the video comments
    getcomments(comment_id, dirpath, comment_id)
    print("End!")
