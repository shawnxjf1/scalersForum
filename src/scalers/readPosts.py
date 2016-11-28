#encoding=utf-8
##attention : python 版本号变化比较大经常网上有一些错误的代码，所以自己写代码的时候一定要表明自己开发的版本号
'''
Created on 2016年9月4日

@author: shawn
'''
from bs4 import BeautifulSoup
import sys
from xlrd import open_workbook
from xlutils.copy import copy

def readAndParseHtml(fileName):
    listInfo = []
    ##problem UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 411: ordinal not in range(128)
    f = open(fileName,'r', encoding='UTF-8')  ##一定要加上encoding=utf-8 才能定位到某个参数，不然它会按顺序解析的
    fileContent = f.read()
    soup = BeautifulSoup(fileContent,'html.parser',from_encoding='utf-8')
    links = soup.find_all('div',attrs={"class":"pctmessage mbm"})
    for link in links:
        ##problem:    b = (link.text).find('你的称呼')
        ##UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 0: ordinal not in range(128)
        b = (link.text).find('你的称呼')
        info = (link.text)[b: b + 12]
        listInfo.append(info)
        print (info)

        b = (link.text).find('所在地区')
        info = (link.text)[b: b + 16]
        listInfo.append(info)

        b = (link.text).find('你的行业')
        info =  (link.text)[b: b + 12]
        listInfo.append(info)

        b = (link.text).find('你的QQ')
        info =  (link.text)[b: b + 18]
        listInfo.append(info)

        b = (link.text).find('你的微信')
        info =  (link.text)[b: b + 18]
        listInfo.append(info)
        
        b = (link.text).find('所处阶段')
        info =  (link.text)[b: b + 18]
        listInfo.append(info)
    return  listInfo

#追加一行写入Excel
def append2Excel(filename,datas,line):
    rb = open_workbook(filename)
    wb = copy(rb)
    sheet = wb.get_sheet(0)
    x = line
    y = 1
    for article in datas:
        sheet.write(x, y, article)
        y +=1
    wb.save(filename)

##执行任务
def runWork():
    index = 1
    for i in range(2,1169):
        #AttributeError: 'str' object has no attribute 'decode'
        al = readAndParseHtml("scalersFormPost/merber" + str(i) + "/page_1.html") ##attention scalersFormPost 首先为中文有异常
        ##遇到的场景1：al遇到问题就直接跳出runWork，程序直接跳出结束
        append2Excel('scalersFormPost/scalersForum.xls',al,index)
        index +=1
        
if __name__ == '__main__':
    print("default encoding()=" +sys.getdefaultencoding()) ##3.4输出 default encoding()=utf-8，2.7输出ascii
    ##sys.setdefaultencoding('utf8')  
    runWork()