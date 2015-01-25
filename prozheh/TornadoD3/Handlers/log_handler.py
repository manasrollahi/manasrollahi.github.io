__author__ = 'Mohammad ali'

import tornado
from  models import *
import peewee
from pycket.session import SessionManager


class LogHandler(tornado.web.RequestHandler):
    def get(self):
            self.render('login.html',UN= "Hello!")

    def post(self,*args):
        user = self.get_argument("user")
        password = self.get_argument("password")
        u=Author.select().where(Author.username==user).get().username
        # print(list)
        if u==user:
            p_info = Author.select().where(Author.username==user).get().password
            if p_info==password:
                idd=Author.select().where(Author.username==user).get().id
                Info = Login.select().where(Login.id == 1).get()
                Info.log = idd
                Info.save()
                self.redirect("/news",idd)
            else:
                self.render('login.html')
        else:
            self.render('login.html')

class LogoutHandler(tornado.web.RequestHandler):

    def get(self):
        Info = Login.select().where(Login.id == 1).get()
        Info.log = 0
        Info.save()
        self.redirect("/")