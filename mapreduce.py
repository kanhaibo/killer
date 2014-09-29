#-*-coding:utf-8-*-
'''
Created on 2014年8月29日

@author: Administrator
'''
import pymongo
import time
from bson.code import Code

def calc_freq_distribution(collecton_hadler):
    out_collection_name = collecton_hadler.name +'_freqdist'
    map = Code("function() { emit(this.BUSINESS_SCOPE,{count:1});}")
    reduce = Code("function (key,values){ var total = 0; for (var i=0; i<values.length;i++) { total += values[i].count;} return {count:total};}")
    result = collecton_hadler.map_reduce(map,reduce,out=out_collection_name)
#     fname = out_collection_name+'.csv'
#     with open(fname, 'w') as f:
#         for doc in result.find():
#             f.write(','.join([str(doc['_id']), str(doc['value']['count'])])+'\n') 
    return result


if __name__ == '__main__':
    print time.localtime(time.time())
    conn = pymongo.Connection("192.168.0.17:27050")
    db = conn.chinatsi
    db.authenticate("chinatsi","chinatsi")
#     input_collection = 
    print calc_freq_distribution(db.enterprise)
    print time.localtime(time.time())
    pass