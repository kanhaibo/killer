#_*_ coding:utf-8 _*_
'''
Created on 2014年9月24日

@author:阚海波
'''
from suds.client import Client
def webservice():
    '''
    创建webservie请求
    '''
    url = "http://appservices.chinatsi.com/app.asmx"
    client = Client(url)
    result = client.service
    return result

if __name__ == '__main__':
    url = "http://appservices.chinatsi.com/app.asmx?wsdl"
    client = Client(url)
    result = client.service.VerifyTel(mobile='')
    print result
#     webserv = webservice()
#     print ws
    pass