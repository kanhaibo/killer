#_*_ coding:utf-8 _*_
'''
Created on 2014年9月19日

@author:阚海波
'''
def displayNumType(num):
    print num, 'is',
    if isinstance(num,(int,long,float,complex)):
        print 'a number of type:',type(num).__name__
    else:
        print 'not a number at all!!'
def mean(sorted_list):
    '''
    把列表里面的数据分成两个列表，其中数据相差最少
    :param sorted_list:
    '''
    if not sorted_list:
        return(([],[]))
    big = sorted_list[-1]
    small = sorted_list[-2]
    big_list,small_list = mean(sorted_list[:-2])
    big_list.append(small)
    small_list.append(big)
    big_list_sum = sum(big_list)
    small_list_sum = sum(small_list)
    if big_list_sum > small_list_sum:
        return((big_list,small_list))
    else:
        return((small_list,big_list))


if __name__ == '__main__':
    foorstr=u'阚海波是个好人啊'
    print foorstr
    print foorstr[::-1][0:1]
    displayNumType(2.4353453453)
#     python列表里面排序，并去重复
    list =[1,23,123,123,23,1]
    if list:
        list.sort()
        last = list[-1]
        for i in range(len(list)-2,-1,-1):
            if last==list[i]:
                del list[i]
            else:
                last = list[i]
    print list
    test = [[1,2,3,4,5,6,700,800],[10001,10000,100,90,50,1],range(1,11),[12312,12311,232,210,30,29,3,2,1,1]]
    for i in test:
        i.sort()
        print
        print "Source List:\t",i
        i1,i2 = mean(i)
        print "Result List:\t",i1,i2
        print "Distance:\t",abs(sum(i1)-sum(i2))
