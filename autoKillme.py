# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------__----
# Name:        濞村鐦痮racle閸滃ongodb娑擃厾娈戦柧鐐复閿涘本娓舵稉鐑樻付閸掓繄娈戦弫鐗堝祦鐎电厧鍙嗗Ο鈩冩緲
# Purpose:f
#
# Author:      闂冩碍鎹ｅ▔?
#
# Created:     25/03/2014
# Copyright:   (c) 闂冩碍鎹ｅ▔?2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import threading
import urllib2

import pymongo
import json
import urllib
import time
import os
import os.path
import math
import ctypes
##reload(sys)
##sys.setdefaultencoding('utf-8')
##print sys.getdefaultencoding()
def _async_raise(tid,exctype):
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid),ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res >1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid),0)
        raise SystemError("PyThreadState_SetAsyncExc failed")
class Thread(threading.Thread):
    def raise_exc(self,excobj):
        assert self.isAlive(),"thread must be started"
        for tid,tobj in threading._active.items():
            if tobj is self:
                _async_raise(tid,excobj)
                return
    def terminate(self):
        self.raise_exc(SystemExit)


##澶氱嚎绋嬫洿鏂扮粡搴︾含搴︼紝閫氳繃璋冪敤鐧惧害鍦板浘鐨刟pi
def enterpriseImport(vthreadsNum,vstart,vCount):
    '''
    
    :param vthreadsNum: use threads count
    :param vstart: use update memo begin id(mongodb's collection enterprise)
    :param vCount: use update memo end id(mongodb's collection enterprise)
    '''
    vContinute = True
    vPerPage = vCount/vthreadsNum
    vlist = []
    tempDic = {}
    for ppp in range(vthreadsNum):
        tempDic.update({'b':vstart+ppp*vPerPage+1,'e':vstart+ppp*vPerPage+vPerPage})
        vlist.append(tempDic.copy())
    threads = []
    #        print "Begin......"
    while vContinute:
        for i in range(vthreadsNum):
        #        time.sleep(1)
    ##鍒版湇鍔″櫒涓婃墽琛屽懡浠�##            a=threading.Thread(target=searchAddress,args=(ip,username,passwd,cmd))
            b = vlist[i]['b']
            e = vlist[i]['e']
#             a=threading.Thread(target=searchCity,args=(b,e))
            a=Thread(target=searchCity,args=(b,e))
#配合主线程，如果主线程崩溃，子线程也被杀死
            a.setDaemon(True) 
            a.start()
            threads.append(a)
        time.sleep(60)
        for x in threads:
            try:
                if x.isAlive():
                    x.terminate()
            finally:
                threads =[]
        try:
            conn = pymongo.Connection("192.168.0.17:27050")
            db = conn.chinatsi
            db.authenticate("chinatsi","chinatsi")
            content = db.chinatsi.find({"_id":{"$gte":vstart,"$lte":vstart+vCount},'PROVINCE':{'$exists':False}},fields=["_id","coordinates"]).count()
#             print type(content)
#             for l in content:
#                 print l  
#             vContinute = False
            if (content>=1):
                vContinute = True
            else:
                vContinute = False
        finally:
            conn.close()   
        
        
##    for iii in threads:
##        iii.join()
#    print time.localtime(time.time())
#            threads.append(a)


def searchCity(vSmallId,vBigId):
    conn = pymongo.Connection("192.168.0.17:27050")
    db = conn.chinatsi
    db.authenticate("chinatsi","chinatsi")
    content = db.chinatsi.find({"_id":{"$gte":vSmallId,"$lte":vBigId},'PROVINCE':{'$exists':False}},timeout=False,fields=["_id","coordinates"])
##    ,"PROVINCE":{"$exists":False}
    for i in content:
        try:
            mm = i["_id"]
            location = str(i["coordinates"]["lat"]) + ','+str(i["coordinates"]["lng"])
            params ={"location":location,'output':'json','ak':'E453317471b1e79dad35e1caaef8bc83'}
            url = 'http://api.map.baidu.com/geocoder?'+urllib.urlencode(params)
            rawreply = urllib2.urlopen(url).read()
            reply = json.loads(rawreply)
            db.chinatsi.update({"_id":mm},{"$set":{"CITY":reply["result"]["addressComponent"]["city"],"PROVINCE":reply["result"]["addressComponent"]["province"]}})
        finally:
            conn.close()

def searchAddress(vSmallId,vBigId):
    try:
        conn = pymongo.Connection("192.168.0.17:27050")
        db = conn.chinatsi
        db.authenticate("chinatsi","chinatsi")
#        content = db.enterprise.find({"_id":{"$gte":vSmallId,"$lte":vBigId},"coordinates":{"lat":29.660708518368,"lng":105.74762640461}},timeout=False,fields = ["_id","COMPANY","COMPANY_ADDRESS"])
        content = db.chinatsi.find({"_id":{"$gte":vSmallId,"$lte":vBigId}},fields = ["_id","COMPANY","COMPANY_ADDRESS"])
#        print content.count()
        for i in content:
            try:
##                鐩墠鏇存柊涓夌鏂瑰紡1锛氬叕鍙稿悕绉�鍏徃鍦板潃3鍏徃鍖哄煙+鍏徃鍦板潃
                ll =  i['COMPANY'].encode('gbk')
                mm =  i['_id']
                params ={'address':ll,'output':'json','ak':'E453317471b1e79dad35e1caaef8bc83'}
##                params.update({'address':ll})
##                print params
                url = 'http://api.map.baidu.com/geocoder/v2/?'+urllib.urlencode(params)
                rawreply = urllib2.urlopen(url).read()
                reply = json.loads(rawreply)
##                print reply['result']['location']
                db.chinatsi.update({"_id":mm},{"$set":{"coordinates":reply['result']['location']}})
##鏇存柊鍥炴暟鎹簱锛岄�杩囧垰鎵嶅緱鍒扮殑绮惧害鍜岀含搴�lat:绾害lng:缁忓害)
            except:
                try:
                    ll = i["COMPANY_ADDRESS"].encode('gbk')
                    mm =  i['_id']
                    params ={'address':ll,'output':'json','ak':'E453317471b1e79dad35e1caaef8bc83'}
                    url = 'http://api.map.baidu.com/geocoder/v2/?'+urllib.urlencode(params)
                    rawreply = urllib2.urlopen(url).read()
                    reply = json.loads(rawreply)
                    db.chinatsi.update({"_id":mm},{"$set":{"coordinates":reply['result']['location']}})
                except:
                    pass
    finally:
        conn.close()
def main():
##    searchCity(10001,20000)
    print time.localtime(time.time())
    vAllCount = 90000.0
    vPerPage = 90000
    vThreads = 200
    vStart = 0
    for p in range(int(math.ceil(vAllCount/vPerPage))):
        print time.localtime(time.time())
        ##        vStart = vStart + vPerPage
        print vStart
        enterpriseImport(vThreads,vStart,vPerPage)
        print time.localtime(time.time())
    

if __name__ == '__main__':
    main()
