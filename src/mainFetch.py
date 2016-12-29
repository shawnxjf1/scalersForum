#coding=utf-8
import threading
#import  traceback
import os
import  sys

'''
1).注意 main.py 一定要放在外面。
2).最开始放在scalers那一层的话出现了SystemError: Parent module '' not loaded, cannot perform relative import 错误。
'''

'''
1).需要完善的,多线程设置钩子,主线程结束的话子线程也跟着结束。
'''

from src.scalers.storePosts import openForumAndStoreToFile ##.storePosts就是当前目录
# import csv
# import xlwt
'''import chardet'''
## 统计信息
## 1.爬取网页  2.存取网页  3.把结果导入mysql 4.把结果导入excel

if __name__ == "__main__":
    threads = []

    rootdir = "scalersForumPost"

    ## 创建互斥锁
    mutex = threading.Lock()

    ##判断目录是否存在
    if not os.path.exists(rootdir):
        os.mkdir(rootdir)

    os.chdir(rootdir)

    #  从第一个帖子爬到到 484 个,没5个帖子一个线程。
    stepLength = 20
    for i in range(1, 1169, stepLength):
        temp_thread = threading.Thread(target=openForumAndStoreToFile, args=(i, i + stepLength,mutex,rootdir))
        threads.append(temp_thread)

    for t in threads:
        t.setDaemon(True)
        t.start()

    for tj in threads:
        tj.join()

    # exitFlag = False
    # while exitFlag:
    #     for tj in threads:
    #         if not (tj.is_alive()):
    #             exitFlag = False
    #         else:
    #             exitFlag = True

    print ("Finished!")