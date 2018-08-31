# -*- coding: utf-8 -*-

import tornado.web
import main
import os


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("template/main.html", title="TextSimilarityMonitoring")


class CheckHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("template/check.html", title="Check")


class AdminHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("template/admin.html", title="Admin", baseFile=os.listdir('./paper'))


class UpFileHandler(tornado.web.RequestHandler):
    def post(self):
        filesDict = self.request.files
        for inputname in filesDict:
            http_file = filesDict[inputname]
            for fileObj in http_file:
                if fileObj.filename.endswith('.txt'):
                    filePath = os.path.join(os.path.dirname(__file__) + '/paper/', fileObj.filename)
                    with open(filePath, 'wb') as f:
                        f.write(fileObj.body)
                        main.init()
                        self.write('file upload success')
                else:
                    self.write('file is error')


class CheckTextHandler(tornado.web.RequestHandler):
    def post(self):
        info = self.get_argument('needText', '')
        print(info)
        sims = main.checkText(info)
        if len(sims) > 0:
            self.render("template/checkList.html", title="Check", list=sims)
        else:
            self.write('No Similar Articles')

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/check", CheckHandler),
    (r"/checkText", CheckTextHandler),
    (r"/admin", AdminHandler),
    (r"/upFile", UpFileHandler),
])


def initServer():
    port = 9010
    application.listen(port)
    print("run in", port)
    tornado.ioloop.IOLoop.instance().start()
