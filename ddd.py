#-*-coding:utf-8-*-
'''
Created on 2014年8月27日
@author: 阚海波
'''
import pymongo
from bson.code import Code
 
def calc_freq_distribution(collection_handler):
    out_collection_name = collection_handler.name+'_freqdist'
    map = Code("function () {"
                "emit(this.freq, {count:1});"
                "}")
 
    reduce = Code("function (key, values) {"
                   "  var total = 0;"
                   "  for (var i = 0; i < values.length; i++) {"
                   "    total += values[i].count;"
                   "  }"
                   "  return {count:total};"
                   "}")
    result = collection_handler.map_reduce(map, reduce, out = out_collection_name)
    fname = out_collection_name+'.csv'
    with open(fname, 'w') as f:
        for doc in result.find():
            f.write(','.join([str(doc['_id']), str(doc['value']['count'])])+'\n') 

if __name__ == '__main__':
    print u'阚海波'
    along = 99999L
    print along
#     conn = pymongo.Connection(['192.168.1.1'], 27018)
#     input_collection= conn.cname.things
#     print calc_freq_distribution(merge_spam)
#  
#     merge_ham = conn.antispam.mergeham
#     print calc_freq_distribution(merge_ham) 