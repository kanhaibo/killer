#_*_ coding:utf-8 _*_
'''
Created on 2014年9月15日

@author:阚海波
'''
import os


if __name__ == '__main__':
    ls = os.linesep
#     get filename
    while True:
        fname = raw_input('>>')
        if os.path.exists(fname):
            print "Error:"
        else:
            break
    all = []
    print "\nEnter lines('.' by itself to quit).\n"
    while True:
        entry = raw_input('> ')
        if entry =='.':
            break
        else:
            all.append(entry)
    fobj = open(fname,'w')
    fobj.writelines(['%s%s' % (x,ls) for x in all])
    fobj.close()
    print 'DONE!'
    pass