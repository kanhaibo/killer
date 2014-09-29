#_*_ coding:utf-8 _*_
'''
Created on 2014年9月16日

@author:阚海波
'''
import cx_Oracle

if __name__ == '__main__':
    for x in range(215996/30+1):
        vbgin = 30*x
        vend = 30*(x+1)
        DB = cx_Oracle.connect('ele_steel','cqmygdsx2s','114.113.152.44/MAIN')
        cursor = DB.cursor()
        cursor.callproc('test_dump',(vbgin,vend))
        DB.close()
        pass
    print 'over'