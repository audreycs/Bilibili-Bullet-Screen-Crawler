# Bilibili Bullet Screen Crawler 
用python语言实现了一个简单的哔哩哔哩弹幕爬虫程序。

## 1. 运行环境
python 3 and higher versions.  

运行前你可能实现需要安装如下模块  
```python
import re
import sys
import requests
import xml.dom.minidom
```

## 2. 使用方式
 Directely compile the file 'Crawler.py':
``` python
python Crawler.py
```
 Then it will ask you to input video's av number:
```
请输入av号:         
```
For example you can enter '6393448'. Then it will create a file named 'av6393448' in current directory which contains 3 files: 
- 'htmlcont.txt' stores original web source code.
- 'av_number.xml' stores original bullet screen comments information.
- 'av_number.csv' stores final bullet screen comments lists.

You can get bullet screen comments' information from the '.csv' file, which contains  context and time.
```
时间(s)，内容
314,就一直循环
325,不恐怖
497,山～丹～丹～滴那个开～花儿～哟～～
742,开！炮！！！
779,哈哈哈哈哈哈哈
982,莫名想笑
910,人
1164,又一次想笑
1239,前面情侣分手的我咒你死
1370,有点可爱
1549,这个洞里是眼睛啊！！！
498,蟑螂更可怕。。。
1776,空投成功
791,鬼:你成功吓着我了。
1780,作死关掉弹幕看吓死
1780,感谢弹幕军
918,这哭声
988,这哭声，对不起我笑了
2035,orz
```
