#encoding=UTF-8
'''
Created on 2016年9月3日

@author: shawn
'''

def convertCookieStrToDict(cookieStr):
    ##注意由于cookie中带有,所以通过把=替换成: ;替换成,的方式不对。
    strArray = cookieStr.split(';')
    tempDict = {}
    for i  in strArray:
        iArray = i.split('=')
        tempDict[iArray[0]]=iArray[1]
    return  tempDict
