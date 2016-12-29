#coding=utf-8

import MySQLdb
import MySQLdb.cursors
import traceback
from warnings import filterwarnings

filterwarnings('error', category= MySQLdb.Warning)

class DBStore(object):
    def __init__(self, params):
        self.conn = self.ConnecttoDB(params)

    def ConnecttoDB(self, params):

        try:
            conn = \
                MySQLdb.connect(host = params[0], \
                                user = params[1], \
                                passwd = params[2], \
                                db = params[3], \
                                port = params[4], \
                                charset = params[5], \
                                cursorclass = MySQLdb.cursors.DictCursor)

            return conn
        except MySQLdb.Warning, w:
            print  "Warning:%s" % str(w)
            return None
        except MySQLdb.Error, e:
            print  "Error:%s" % str(e)
            return None

    def queryDB(self):
        sql = """
                show variables like 'max_connections';
                """
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                print row
        except MySQLdb.Warning, w:
            print  "Warning:%s" % str(w)
            self.close()
        except MySQLdb.Error, e:
            print  "Error:%s" % str(e)
            self.close()

    def storeBasicInfo(self, maindict, detailinfo):
        table_name = 'member_basic_info'
        member_id = ''
        member_name = ''
        member_speciality = ''
        member_location = ''
        member_readnum = 0
        member_replynum = 0

        basicinfosql = """
                        insert into  member_basic_info
                        values(%s, %s, %s, %s, %s, %s)
                        """

        detailinfosql = """
                        insert into  member_reply_info
                        values(%s, %s, %s, %s, %s, %s, %s)
                        """
        try:
            for key in maindict.keys():
                import re
                try:
                    if key == 'host':
                        try:
                            basiclist =  maindict[key].split('[')[1].split(']')
                        except Exception:
                            member_id = maindict[key].encode('utf-8')
                            member_name = maindict[key].encode('utf-8')
                            member_speciality = maindict[key].encode('utf-8')
                            member_location = maindict[key].encode('utf-8')
                            pass


                        member_id = basiclist[0]
                        member_others_info = basiclist[1].split('-')
                        member_name = member_others_info[0].encode('utf-8')
                        try:
                            member_speciality = member_others_info[1].encode('utf-8')
                            member_location = member_others_info[2].encode('utf-8')
                        except:
                            member_speciality = member_others_info[0].encode('utf-8')
                            member_location = member_others_info[0].encode('utf-8')



                    elif key == u'回复':
                        member_replynum = int(maindict[key])
                    elif key == u'阅读':
                        member_readnum = int(maindict[key])
                    else:
                        pass

                    basic_params = (member_id, member_name, member_speciality, member_location, member_readnum,member_replynum)
                except Exception, e:
                    basic_params = (member_id, member_name, member_speciality, member_location, member_readnum,member_replynum)
                    print e
                    pass

            if len(detailinfo):
                detailparams = []
                for details in detailinfo:
                    try:
                        ispost = 1
                        post_id = ''
                        post_member_id =  ''
                        post_name = ''
                        post_time = ''
                        post_context = ''
                        reply_member_id = ''
                        reply_member_name = ''
                        reply_time = ''
                        reply_context = ''

                        post_id = details['post_id']
                        try:
                            post_member_id =  details['gn'].split('[')[1].split(']')[0]
                        except Exception, e:
                            post_member_id =  details['gn'].encode('utf-8')
                            pass

                        try:
                            post_name = details['gn'].split(']')[1].encode('utf-8')
                        except Exception, e:
                            post_name = details['gn'].encode('utf-8').encode('utf-8')
                            pass
                        post_time = details['posttime']
                        post_context = details['message'].encode('utf-8')

                        detailparams.append((post_id, member_id, post_member_id, post_name, post_time, post_context, ispost))

                        if details['reply'] and len(details['reply']):
                            for replys in details['reply']:
                                try:
                                    reply_member_id = replys['reply_person'].split('[')[1].split(']')[0]
                                except Exception, e:
                                    reply_member_id = replys['reply_person'].encode('utf-8')
                                    pass
                                try:
                                    reply_member_name = replys['reply_person'].split(']')[1].encode('utf-8')
                                except Exception, e:
                                    reply_member_name = replys['reply_person'].encode('utf-8')
                                    pass

                                reply_time = replys['reply_time']
                                if ')' in reply_time:
                                    reply_time = replys['reply_time'].split(')')[0].strip()
                                    print reply_time
                                reply_context = replys['reply_context'].encode('utf-8')
                                ispost = 2

                                detailparams.append((post_id, member_id, reply_member_id, reply_member_name, reply_time, reply_context, ispost))
                    except Exception, e:
                        print e
                        pass
        except Exception,e :
            print e
            pass

        commitnum = 0
        for i in detailparams:
            self.insertDB(detailinfosql, i)
            commitnum += 1

            if commitnum == 10:
                self.conn.commit()
                commitnum = 0
        self.insertDB(basicinfosql, basic_params)
        self.conn.commit()




    def insertDB(self, sql, params):
        try:
            print params
            cursor = self.conn.cursor()
            print cursor.execute(sql, params)
        except MySQLdb.Warning, w:
            print  "Warning:%s" % str(w)
            print traceback.print_exc()
            pass
        except MySQLdb.Error, e:
            print  "Error:%s" % str(e)
            print traceback.print_exc()
            pass

    def close(self):
        self.conn.close()


