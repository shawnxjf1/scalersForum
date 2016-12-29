#coding=utf-8
##review by xujianfeng 2016-09-03
import smtplib
from email.mime.text import MIMEText
import exceptions
import urllib
import os
import requests
from lxml import etree
from multiprocessing.dummy import Pool
from bs4 import BeautifulSoup
import sys
import threading
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy
import urllib2
import re
## 导入的时候一定要代入package名字
import util.getCookie.convertCookieStrToDict

# reload(sys)
# #
# #html=requests.get(url,cookies = cook).content
# ##cook = {'Cookie': 'RK=Xrt2Bj7nc5; pgv_pvi=8592594934; pgv_pvid=823172100; o_cookie=1379588730; uniqueuid=e807943e6a64aef50a63ffee0b016beb; security_cookiereport=1462930072; ptui_loginuin=1379588730@qq.com; ptisp=ctc; ptcz=9308196a49ee7830db0b6bd72fb98794f2c9cc93dc401b81394f239b718ea6d8; pt2gguin=o1379588730; uin=o1379588730; skey=@RFZvvxjTW; p_uin=o1379588730; p_skey=oAOb7U5LrleJjtT3WEnMtKjhWNuOvyVvHEuFNS1wOW4_; pt4_token=qmmVWpgURB4gVRVX4WQXyzH1wuRJJD1txUAgkSoLgEY_; MANYOU_SESSIONID_bf895=113a191494333968db021ffa0f87f3f6; qqUser=%7B%22uin%22%3A1379588730%2C%22nickName%22%3A%22%5Cu5f6d%5Cu8001%5Cu5e08%22%7D'}
# url = 'http://qgc.qq.com/309916014/t/198?page=%d'
# url = 'http://qgc.qq.com/309916014/t/1'
#
# cookieStr = "pgv_pvid=8411115300; o_cookie=4865368; h_uid=H071608093a1; ptui_loginuin=shawn_angel@qq.com; pt2gguin=o0004865368; uin=o0004865368; skey=@R7plcYzq6; RK=PJcmRfuSHd; ptcz=f4ed2bdc97d0125ef7f6ade9566df37e9c50692755edaa9e668cbd977da0d45d; MANYOU_SESSIONID_bf895=f72b33e492abcff67eb75af754dee04d; qqUser=%7B%22uin%22%3A4865368%2C%22nickName%22%3A%22shawn%22%7D; uniqueuid=a7badc8eca57a3ce3a1964bb58fb9ea4; security_cookiereport=1472906994"
# ##attention  util.cookieUtil.convertCookieStrToDict 必须要带上util.cookieUtil.convertCookieStrToDict
# cook=util.cookieUtil.convertCookieStrToDict(cookieStr)
#
# def isNewNotification(url):
#     a = 1
#     url = url%a
#     ##cook = {'Cookie': 'RK=Xrt2Bj7nc5; pgv_pvi=8592594944; pgv_pvid=823172100; o_cookie=1379588730; uniqueuid=e807943e6a64aef50a63ffee0b016beb; ptui_loginuin=1379588730@qq.com; ptisp=ctc; ptcz=9308196a49ee7830db0b6bd72fb98794f2c9cc93dc401b81394f239b718ea6d8; pt2gguin=o1379588730; uin=o1379588730; skey=@gmu6daiaI; p_uin=o1379588730; p_skey=TrqZ7p9zyBgEdBou*SP8OOR0USgAfdZES8LUoyM-3xk_; pt4_token=08PsybdJCDN8fazNaP29O63WO6Rc5VYhniI0RdEGJ54_; MANYOU_SESSIONID_bf895=113a191494333968db021ffa0f87f3f6; qqUser=%7B%22uin%22%3A1379588730%2C%22nickName%22%3A%22%5Cu5f6d%5Cu8001%5Cu5e08%22%7D; security_cookiereport=1462700499'}
#     html = requests.get(url, cookies=cook).content
#     soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
#     title = soup.title.text
#     print title
#     if (title.find("新消息"))>0:
#         print "发送邮件, 微信收到推送消息..."
#         #send_mail(mailto_list,'您收到新的留言','请点击回复!')
#
#
#
# def autoPush(content):
# # 从28个字节长度开始,  这时一个汉字按8个字节计算
#     headers = {
#     'Host': 'qgc.qq.com',
#     'Connection': 'keep-alive',
#     'Content-Length': '57',
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'Origin': 'http://qgc.qq.com',
#     'X-Requested-With': 'XMLHttpRequest',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.4 Safari/537.36',
#     'Content - Type': 'application / x - www - form - urlencoded',
#     'Referer': 'http://qgc.qq.com/309916014/t/198',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept-Language': 'zh-CN,zh;q=0.8',
#     'Cookie': cookieStr
#     }
#     data = {
#         'CSRFToken':'98bda78e',
#     'replysubmit':'true',
#     'fContent':'test after 10h'
#     }
#     url2 = 'http://qgc.qq.com/309916014/r/new/submit?tId=198&response_type=json&isAjax=1'
#
#     body = urllib.urlencode(data)
#
#     request = urllib2.Request(url=url2,data=body,headers=headers)
#     r = urllib2.urlopen(request)
#     print r
#
#
# # 得到即时消息
# def getNoticeByAjax(url):
#     url = 'http://qgc.qq.com/notice/box?page=1&response_type=json&isAjax=1'
#     cook = {'Cookie': 'RK=Xrt2Bj7nc5; pgv_pvi=8592594944; pgv_pvid=823172100; o_cookie=1379588730; uniqueuid=e807943e6a64aef50a63ffee0b016beb; ptui_loginuin=1379588730@qq.com; ptisp=ctc; ptcz=9308196a49ee7830db0b6bd72fb98794f2c9cc93dc401b81394f239b718ea6d8; pt2gguin=o1379588730; uin=o1379588730; skey=@gmu6daiaI; p_uin=o1379588730; p_skey=TrqZ7p9zyBgEdBou*SP8OOR0USgAfdZES8LUoyM-3xk_; pt4_token=08PsybdJCDN8fazNaP29O63WO6Rc5VYhniI0RdEGJ54_; MANYOU_SESSIONID_bf895=113a191494333968db021ffa0f87f3f6; qqUser=%7B%22uin%22%3A1379588730%2C%22nickName%22%3A%22%5Cu5f6d%5Cu8001%5Cu5e08%22%7D; security_cookiereport=1462700499'}
#     html = requests.get(url, cookies=cook).content
#     print html
#
# def getPages(url):
#     print '-------'
#     html = requests.get(url, cookies=cook).content
#     selector = etree.HTML(html)
#     pagea = selector.xpath('/html/body/div[5]/div[1]/div[7]/p/a[@class="c_tx"]')
#     print  pagea
#     return len(pagea)+1
#
# #爬取每个从帖子的阅读量和回复量, 注意回复量是自己打卡记录数量+别人留言量(此数据可计算互动量)
# def getVCcount(url,id,pageIndex):
#     total = 0
#     poplist=[]
#     pages = getPages(url %(id,pageIndex))
#     poplist.append(id)
#     print url
#     for i in range(1,pages+1):
#         a =  url % (id, i)
#         print a
#
#         html = requests.get(a, cookies=cook).content
#
#         soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
#
#         num = 1
#         try:
#             links = soup.find_all('span', attrs={"class": re.compile(r'gn(.*?)')})
#             # print len(links)
#
#             for link in links:
#                 strIndex=filter(str.isdigit,str(link.text))
#                 if strIndex == '002':
#                     print strIndex
#                     num +=1
#             total += num
#
#
#         except:
#             print 0
#     print '------------' + str(total)
#     poplist.append(total-1)
#     return poplist
#
#
#
# def getSelfPublish(url,index):
#     url =  url%index
#     print url
#     poplist = []
#     html = requests.get(url, cookies=cook).content
#     selector = etree.HTML(html)
#
#     try:
#         links = selector.xpath('//span[@class="gn "]/text()')
#         #print len(links)
#
#         for link in links:
#             if str(index) in link :
#                 print link
#
#
#     except:
#         poplist.append(index)
#         poplist.append('NULL')
#
#
#     return poplist
#
# def getPopByXpath(url,index):
#     print url
#     poplist = []
#     html = requests.get(url, cookies=cook).content
#     selector = etree.HTML(html)
#     try:
#         link2 = selector.xpath('//*[@id="vcount"]/text()')  #阅读量
#         link = selector.xpath('//*[@id="rcount"]/text()')   #回复量
#         print link[0] + ":" + link2[0]
#         poplist.append(index)
#         poplist.append(link2[0])
#         poplist.append(link[0])
#     except:
#         poplist.append(index)
#         poplist.append('NULL')
#         poplist.append('NULL')
#
#
#     return poplist
#
# def getPop(url):
#     poplist=[]
#     html = requests.get(url, cookies=cook).content
#
#     soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
#     links = soup.find_all('span', attrs={"class": "xs5"})
#     for link in links:
#         print link.text
#
#
#
#
# def getCrapInfo(url,num):
#
#      listInfo = []
#      html = requests.get(url,cookies=cook).content
#
#      soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
#      links = soup.find_all('div',attrs={"class":"pctmessage mbm"})
#      listInfo.append(num)
#      for link in links:
#          #if (link.text.upper().find('OFFICE')>0):  #先搜索关键词
#         b = (link.text).find('你的称呼')
#         info = (link.text)[b: b + 12]
#         listInfo.append(info)
#         print info
#
#         b = (link.text).find('所在地区')
#         info = (link.text)[b: b + 16]
#         listInfo.append(info)
#
#         b = (link.text).find('你的行业')
#         info =  (link.text)[b: b + 12]
#         listInfo.append(info)
#
#         b = (link.text).find('你的QQ')
#         info =  (link.text)[b: b + 18]
#         listInfo.append(info)
#
#         b = (link.text).find('你的微信')
#         info =  (link.text)[b: b + 18]
#         listInfo.append(info)
#
#               # b = (link.text).find('如果你是成长会2015成员，请评估一下去年写这个题目时所说的想法与完成度。')
#               # c = (link.text).find('在过去的一年甚至')
#               #
#               # info = (link.text)[b: c]
#               #listInfo.append(info)
#      return  listInfo
#
# #写多数据信息到Excel -- 标题,链接,阅读量,评论,喜欢 articlelist []
# def write2ExcelArticleInfo(articlelist,line):
#     book = xlwt.Workbook(encoding='utf-8', style_compression=0)
#     sheet = book.add_sheet('hot', cell_overwrite_ok=True)
#     x = line
#     y = 1
#     for article in articlelist:
#
#         sheet.write(x, y, article)
#         y +=1
#     book.save("/Users/mac/Documents/sbbs.xls")
#
# #追加一行写入Excel
# def append2Excel(filename,datas,line):
#     rb = open_workbook(filename)
#     wb = copy(rb)
#     sheet = wb.get_sheet(0)
#     x = line
#     y = 1
#     for article in datas:
#         sheet.write(x, y, article)
#         y +=1
#     wb.save(filename)
#
# index = 1
# for i in range(876,1200):
#      al = getCrapInfo('http://qgc.qq.com/309916014/t/%d'%i,i)
#      append2Excel('/Users/mac/Documents/sbbs.xls',al,index)
#      index +=1
#
# #getNoticeByAjax(url)
#
# #自动发贴
# #autoPush('')
# #isNewNotification(url)
#
#
#
# #getPop(url)
# #getCrapInfo(url,1)
# #getPopByXpath(url,198)
#
# #print getVCcount('http://qgc.qq.com/309916014/t/%d?page=%d',457,1)
#
# #getPages('http://qgc.qq.com/309916014/t/249?page=1')
#
# # 检出每个人的帖子有多少页?
# # '''
# # <a class="c_tx" href="/309916014/t/198?page=4" target="_top"><span>4</span></a>
# #
# # '''
#
#
# #成长贴人气榜, 更新TOP排行数据采集
# #for i in range(2,1200):
#     #vcs = getVCcount('http://qgc.qq.com/309916014/t/%d?page=%d', i, 1)
#     #print vcs
#     #append2Excel('/Users/mac/Documents/sbbs.xls', vcs, index)
#     #index += 1
#
# #getVCcount('http://qgc.qq.com/309916014/t/%d?page=%d', 2, 1)





