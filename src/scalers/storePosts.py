#encoding=utf-8
'''
Created on 2015年10月13日

@author: shawn
'''
##env 环境：python2.7
##运行场景：在2.7 的场景下运行出来生成文件，3.4运行下有编码问题-2016年09月04日

##改进：通过协成调度改进 （或者多线程调度）- 参考：http://www.pythontab.com/html/2014/pythonhexinbiancheng_0107/660.html 

##pip3 install requests 
#import urllib2
import requests   ###requests 比urllib2简单,可以通过状态码和head对返回值进行处理
#import Cookie
import os
from util import cookieUtil


# 登录之后的cookie
# cookieStr 获取方式：1.打开chrom浏览器登录 scalers 群论坛。 2.打开开发者工具 输入 document.cookie 输出的字符串即对应的qq论坛cookie
cookieStr = "pgv_pvid=8411115300; o_cookie=4865368; h_uid=H071608093a1; ptui_loginuin=shawn_angel@qq.com; pt2gguin=o0004865368; uin=o0004865368; skey=@R7plcYzq6; RK=PJcmRfuSHd; ptcz=f4ed2bdc97d0125ef7f6ade9566df37e9c50692755edaa9e668cbd977da0d45d; MANYOU_SESSIONID_bf895=f72b33e492abcff67eb75af754dee04d; qqUser=%7B%22uin%22%3A4865368%2C%22nickName%22%3A%22shawn%22%7D; uniqueuid=a7badc8eca57a3ce3a1964bb58fb9ea4; security_cookiereport=1472906994"

##attention  convertCookieStrToDict 使用这个函数前必须定义
cookies = cookieUtil.convertCookieStrToDict(cookieStr)



##打开论坛存储网页到文件
def openForumAndStoreToFile():
    
    # cookies = dict({"o_cookie":"4865368","_ga":"GA1.2.2096652587.1443268803","pgv_pvid":"6712657600","RK":"TAdmR9u4E9","pt_clientip":"fcb48be356bbf5d6","pt_serverip":"572d0abf0664b253","ptui_loginuin":"4865368","ptisp":"cnc","ptcz":"26a7968648ebdc84b4d9c10c3edfd1839326f206f404a5ad124408c5d865f2f8","pt2gguin":"o0004865368","uin":"o0004865368","skey":"@8564cOheA","p_uin":"o0004865368","p_skey":"LL7Ix4NaHgY582l6tAKG7E1tDvni4GkAjr6qZnR3pHE_","pt4_token":"YoIIRpRzEfp4w5D1Cj9eCg__","MANYOU_SESSIONID_bf895":"a82f802c7ead744a7fc6ba6a6ee75c41","qqUser":"%7B%22uin%22%3A4865368%2C%22nickName%22%3A%22shawn%22%7D","uniqueuid":"a7badc8eca57a3ce3a1964bb58fb9ea4","security_cookiereport":"1445177599"})
    #cookies = dict({"o_cookie":"4865368", "_ga":"GA1.2.2096652587.1443268803", "pgv_pvid":"6712657600", "uniqueuid":"a7badc8eca57a3ce3a1964bb58fb9ea4", "ptui_loginuin":"4865368", "ptisp":"ctc", "RK":"TAdmR9u4E9", "ptcz":"26a7968648ebdc84b4d9c10c3edfd1839326f206f404a5ad124408c5d865f2f8", "pt2gguin":"o0004865368", "uin":"o0004865368", "skey":"@xM8f1imhc", "p_uin":"o0004865368", "p_skey":"FP45yfAxSOwPPIuFTpgWLKsk7LfaAZfHadzu4CmY82A_", "pt4_token":"8Ou9Lkvkxzc1RKvK3B*2lA__", "MANYOU_SESSIONID_bf895":"a82f802c7ead744a7fc6ba6a6ee75c41", "qqUser":"%7B%22uin%22%3A4865368%2C%22nickName%22%3A%22shawn%22%7D", "security_cookiereport":"1445654814"})
    # 为啥输出没有反应呢。
    # cookies = dict({"o_cookie":"4865368","_ga":"GA1.2.2096652587.1443268803","uniqueuid":"a7badc8eca57a3ce3a1964bb58fb9ea4","pgv_pvid":"6712657600","qm_sid":"71b3946af329f576ac6acfe03374595f,cmUooF9Z9EoE.","qm_username":"4865368","pt_clientip":"5ff2b4a61c4456f6","pt_serverip":"bc3a0abf0659585d","ptui_loginuin":"4865368","ptisp":"ctc","RK":"TAdmR9u4E9","ptcz":"26a7968648ebdc84b4d9c10c3edfd1839326f206f404a5ad124408c5d865f2f8","pt2gguin":"o0004865368","uin":"o0004865368","skey":"@Kzirr9L8u","p_uin":"o0004865368","p_skey":"ZP7UtB-rTMXdSuAXNIe4QLa5Am897YfSpNyspEVpiXk_","pt4_token":"8AH2JIes4c8lQpotLs5DBw__"})
    baseurl = "http://qgc.qq.com/309916014/t/"
    # baseurl1 = "http://qgc.qq.com/298172004/t/2?page=2"
    rootdir = "scalersForumPost"
    
    ##判断目录是否存在
    if not os.path.exists(rootdir):
        os.mkdir(rootdir)
    
    os.chdir(rootdir)
    # 目录存在的还就需要删除 －－－－－－完善
    ## 
    for i in range(577, 1169):  # 成长会成员数
         memberdir = "merber" + str(i)
         
         ##从第577只写第一页
         ##attention 判断目录是否存在
         if not os.path.exists(memberdir):
             os.mkdir(memberdir)
         os.chdir(memberdir)
         url = baseurl + "/" + str(i)
         #print "url = %s" % url
         content = getOnePage(url, cookies) 
         ##把内容写入文件
         f = open('page_' + str(1) + ".html", 'w')
         f.write(content)
         f.close()       
         
#          for j in range(1, 20):
#             if j == 1:
#                  url = baseurl + "/" + str(i)
#                  #print "url = %s" % url
#                  content = getOnePage(url, cookies)
#                  
#                  ##把内容写入文件
#                  f = open('page_' + str(j) + ".html", 'w')
#                  f.write(content)
#                  f.close()
#             else:
#                  url = baseurl + "/" + str(i) + "/?page=" + str(j)
#                  content = getOnePage(url, cookies)
#                  f = open('page_' + str(j) + ".html", 'w')
#                  f.write(content)
#                  f.close()
#                  if not isHasNextPage(content):
#                      break
         os.chdir("..")


    
def getOnePage(url, cookies):
    r = requests.get(url, cookies=cookies)
    ##probelm TypeError: must be str, not bytes request  返回的是bytes么？

    return (r.content)


def isHasNextPage(content):
    if content.count('<span>下一页</span>') > 0:
        return True
    else:
        return False

if __name__ == '__main__':
    openForumAndStoreToFile()
    
    print (u'\u65e0\u5e8f\u5217\u8868')
