# encoding=utf-8
'''
Created on 2014年9月9日

@author: Administrator
'''
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define,options
define("port",default=8888,help="run on the given port",type=int)



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'hello')
        self.write(greeting+', friendly user!')
#         self.write("Hello, world")


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([(r"/",MainHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
#     c = '%u8FD9%u662F%u4E00%u4E32%u6587%u5B57'
#     print "".join([(len(i)>0 and unichr(int(i,16)) or "") for i in c.split('%u')])
#     print "".join([ (len(i)>0 and unichr(int(i,16)) or "") for i in c.split('%u')])
#     print "".join(["1","2"])
    pass