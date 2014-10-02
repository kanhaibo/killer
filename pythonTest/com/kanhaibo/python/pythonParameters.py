#-*-coding:utf-8-*-
'''
Created on 2014-10-2

@author: 阚海波
'''
def funTuplePar(*keys):
    print "*keys tpye=%s" % type(keys)
    print "*keys=%s"  % str(keys)
    for i in range(0,len(keys)):
        print "keys["+str(i)+"]=%s" % str(keys[i])

def fun2(**keys):
    print "keys type=%s" % type(keys)
    print "keys=%s" % str(keys)
    print "name=%s" % str(keys['name'])

def fun3(*tup,**dicc):
    print "*tup=%s" % type(tup)
    print "*tup=%s" % str(tup)
    print "*dicc=%s" % type(dicc)
    print "*dicc=%s" % str(dicc)
if __name__ == '__main__':
    fun3(1231,12313,1231234,'ssdfsd',mm=1231,ll=1231,lll=3453)
#    funTuplePar(1,12,123123,231)
#    fun2(name="dfsfs",lll="sdfsdf")