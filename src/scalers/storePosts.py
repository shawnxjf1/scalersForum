#encoding=utf-8
'''
Created on 2015年10月13日

@author: shawn
'''
## env 环境：python2.7
## 运行场景：在2.7 的场景下运行出来生成文件，3.4运行下有编码问题-2016年09月04日

## 改进：通过协成调度改进 （或者多线程调度）- 参考：http://www.pythontab.com/html/2014/pythonhexinbiancheng_0107/660.html

## pip3 install requests
## import urllib2
import requests   ###requests 比urllib2简单,可以通过状态码和head对返回值进行处理
## import Cookie
import os
import  sys
sys.path.append('..')

from ..util import getCookie


# 登录之后的cookie
# cookieStr 获取方式：1.打开chrom浏览器登录 scalers 群论坛。 2.打开开发者工具 输入 document.cookie 输出的字符串即对应的qq论坛cookie
cookieStr = "pgv_pvi=626233344; RK=GIduA/ujHf; pgv_si=s5752286208; ptui_loginuin=shawn_angel_xjf@foxmail.com; pgv_pvid=8881124850; pgv_info=ssid=s2615254016; verifysession=h015194e386fcaea0c1d74c071fa87ed6c347b38bf94b49570e55f2fcd430ac1a3ff4b6f898e14b288b; qzone_check=3559404996_1482637909; rv2=80C69B1234D7CD70806C93562EA688A1F701073928EA25F82B; property20=906CCC5C3E5D46C2CA1B3AC05797DBCA4B88DF334EAC64C5EA1B6CED42581479E2C211129239CF1D; uniqueuid=a7badc8eca57a3ce3a1964bb58fb9ea4; ptisp=ctc; ptcz=d369ce2a5d647ef540b32663c157e8545c5014e262e56a0bf7ba68752d943226; pt2gguin=o0004865368; uin=o0004865368; skey=MvacvXU893; p_uin=o0004865368; p_skey=VJ4bsJz8O*gpYwa5y1hYc-NeCM9SWDZUMQmCJOcgP4Y_; pt4_token=7kCyGVcaXd*gtCytlUJD9CF6IPebzli0lxa*4LUm0gw_; MANYOU_SESSIONID_bf895=7effa33452c602be5968895351ab0fda; qqUser=%7B%22uin%22%3A4865368%2C%22nickName%22%3A%22shawn%22%7D; security_cookiereport=1482850125"

##attention  convertCookieStrToDict 使用这个函数前必须定义
cookies = getCookie.convertCookieStrToDict(cookieStr)



##打开论坛存储网页到文件
def openForumAndStoreToFile(start,sliceLength,mutex,rootdir):
    
    # cookies = dict({"o_cookie":"4865368","_ga":"GA1.2.2096652587.1443268803","pgv_pvid":"6712657600","RK":"TAdmR9u4E9","pt_clientip":"fcb48be356bbf5d6","pt_serverip":"572d0abf0664b253","ptui_loginuin":"4865368","ptisp":"cnc","ptcz":"26a7968648ebdc84b4d9c10c3edfd1839326f206f404a5ad124408c5d865f2f8","pt2gguin":"o0004865368","uin":"o0004865368","skey":"@8564cOheA","p_uin":"o0004865368","p_skey":"LL7Ix4NaHgY582l6tAKG7E1tDvni4GkAjr6qZnR3pHE_","pt4_token":"YoIIRpRzEfp4w5D1Cj9eCg__","MANYOU_SESSIONID_bf895":"a82f802c7ead744a7fc6ba6a6ee75c41","qqUser":"%7B%22uin%22%3A4865368%2C%22nickName%22%3A%22shawn%22%7D","uniqueuid":"a7badc8eca57a3ce3a1964bb58fb9ea4","security_cookiereport":"1445177599"})
    #cookies = dict({"o_cookie":"4865368", "_ga":"GA1.2.2096652587.1443268803", "pgv_pvid":"6712657600", "uniqueuid":"a7badc8eca57a3ce3a1964bb58fb9ea4", "ptui_loginuin":"4865368", "ptisp":"ctc", "RK":"TAdmR9u4E9", "ptcz":"26a7968648ebdc84b4d9c10c3edfd1839326f206f404a5ad124408c5d865f2f8", "pt2gguin":"o0004865368", "uin":"o0004865368", "skey":"@xM8f1imhc", "p_uin":"o0004865368", "p_skey":"FP45yfAxSOwPPIuFTpgWLKsk7LfaAZfHadzu4CmY82A_", "pt4_token":"8Ou9Lkvkxzc1RKvK3B*2lA__", "MANYOU_SESSIONID_bf895":"a82f802c7ead744a7fc6ba6a6ee75c41", "qqUser":"%7B%22uin%22%3A4865368%2C%22nickName%22%3A%22shawn%22%7D", "security_cookiereport":"1445654814"})
    # 为啥输出没有反应呢。
    # cookies = dict({"o_cookie":"4865368","_ga":"GA1.2.2096652587.1443268803","uniqueuid":"a7badc8eca57a3ce3a1964bb58fb9ea4","pgv_pvid":"6712657600","qm_sid":"71b3946af329f576ac6acfe03374595f,cmUooF9Z9EoE.","qm_username":"4865368","pt_clientip":"5ff2b4a61c4456f6","pt_serverip":"bc3a0abf0659585d","ptui_loginuin":"4865368","ptisp":"ctc","RK":"TAdmR9u4E9","ptcz":"26a7968648ebdc84b4d9c10c3edfd1839326f206f404a5ad124408c5d865f2f8","pt2gguin":"o0004865368","uin":"o0004865368","skey":"@Kzirr9L8u","p_uin":"o0004865368","p_skey":"ZP7UtB-rTMXdSuAXNIe4QLa5Am897YfSpNyspEVpiXk_","pt4_token":"8AH2JIes4c8lQpotLs5DBw__"})
    baseurl = "http://qgc.qq.com/309916014/t/"
    # baseurl1 = "http://qgc.qq.com/298172004/t/2?page=2"

    # FIXME 目录存在的还就需要删除 －－－－－－完善
    ## 
    for i in range(start, start + sliceLength):  # 成长会成员数
         memberdir = "member" + str(i)
         curDir = "/Users/shawn/eclipse_workspace_pdev_group/pdev_v1/scalerforum/src/scalers/scalersForumPost/"

         if mutex.acquire(1): ## 如果不加锁会出现,member1/member02/member03/member05的情况
              if not os.path.exists(memberdir):
                  os.mkdir(memberdir)
              os.chdir(memberdir)
              curDir = curDir + "/" + memberdir +"/"
              os.chdir("..")
         mutex.release()

         url = baseurl + str(i)

         content = getOnePage(url, cookies)

         ## finished.md 做完成员爬取完的标识,不需要重新爬一次
         finishedFileName = curDir + 'finished.md'
         if os.path.isfile(finishedFileName):
             print('member' + str(i) + 'is finised,dont need to get again')
             continue

         for j in range(1, 100):
            if j == 1:
                 url = baseurl + "/" + str(i)
                 #print "url = %s" % url
                 content = getOnePage(url, cookies)
                 fileName = curDir + 'page_' + str(j) + ".html"
                 if os.path.isfile(fileName):
                     continue
                 ##把内容写入文件
                 writePage(content,j,fileName)
            else:
                 fileName = curDir + 'page_' + str(j) + ".html"
                 if os.path.isfile(fileName):
                     continue
                 url = baseurl + "/" + str(i) + "/?page=" + str(j)
                 print('write url=' + url)
                 content = getOnePage(url, cookies)
                 writePage(content,j,fileName)
                 if not isHasNextPage(content):
                     writePage("finished...",j,finishedFileName)
                     j = 1000
         print('write page Ok,curDir' + curDir)

def writePage(content,i,fullName):
     f = open(fullName, 'w')
     f.write(content)
     f.close()


    
def getOnePage(url, cookies):
    r = requests.get(url, cookies=cookies)
    ##probelm TypeError: must be str, not bytes request  返回的是bytes么？
    ## website.encode(encoding="gb2312")
    return (r.content.decode(encoding="utf-8")) ## r.content.decode(encoding="utf-8") -> bytes 解码成 str


def isHasNextPage(content):
    if content.count('<span>下一页</span>') > 0:
        return True
    else:
        return False

if __name__ == '__main__':
    openForumAndStoreToFile()
    
    print (u'\u65e0\u5e8f\u5217\u8868')
