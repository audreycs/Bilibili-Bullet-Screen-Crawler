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

    #输出视频地址
    print("视频地址是:" + url)

    #查看视频地址是否能访问
    r = requests.get(url, headers = head, timeout=5)
    code = r.status_code
    if code == 200: 
	    print("查看网页能否正常访问: OK 网站访问正常")
    else:
	    print("查看网页能否正常访问: Error 网站不能访问！")
        #print("程序退出!")
	    sys.exit(2)

    #获取网页源代码
    html = requests.get(url, headers = head)

    #写进网页源代码
    fw = open(dirpath + "htmlcont.txt","w",encoding="utf-8")
    fw.write(html.text)
    fw.close()

    print("获取视频网页源代码成功!")

    fr = open(dirpath + "htmlcont.txt","r",encoding="utf-8")
    line = fr.readline()
    while line:
        matchstr = re.search(r"cid=([0-9]*)&aid=",line)
        if matchstr!= None:
            fr.close()
            print("获取视频弹幕成功!")
            return matchstr.group(1)
        line = fr.readline()
        
def getcomments(cid):
    comment_url = 'http://comment.bilibili.com/'+str(cid)+'.xml'
    print("弹幕文件为:"+comment_url)

    html = requests.get(comment_url)
    with open(dirpath + cid + ".xml", "wb") as code:
        code.write(html.content)

    url = dirpath + str(cid)+".xml"
    dom = xml.dom.minidom.parse(url)
    root = dom.documentElement
    comments = root.getElementsByTagName('d')
    print("解析弹幕的时间与内容中......")
    f.writelines("时间(s)"+","+"评论内容"+"\n")
    for i in range(len(comments)):
        item = comments[i]
        attrs = item.getAttribute("p")
        time = attrs.split(",")[0]
        comment = comments[i].firstChild.data
        f.writelines(str(int(float(time)))+","+comment.split(",")[0]+"\n")


if __name__ == '__main__':
    av = input('请输入av号:')
    dirpath = "./av"+av+"/"

    if not os.path.exists(dirpath):
        os.mkdir(dirpath)

    #爬取视频网页源文件
    comment_id = spider(av)

    f = open(dirpath + comment_id + '.csv', 'w', encoding='utf-8')
    getcomments(comment_id)
    print("结束!")