import tornado

__author__ = 'mojtaba.banaie'


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
            self.render('index.html',UN= "Hello!")
        # else :
        #     session.set('LoggedIn', {"_id":"12222222","name":"ali"})
        #     self.render('index.html',UN="U Are Not Logged In..")
