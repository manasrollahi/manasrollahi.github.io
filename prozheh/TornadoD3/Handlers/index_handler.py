import tornado

__author__ = 'mojtaba.banaie'
# from pycket.session import SessionManager
from models import *

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        news = News.select().order_by(News.id.desc())
        cnt=0
        list1=[]
        for n in news:
            n1=Author.select().where(Author.id==n.author).get().fn
            n2=Author.select().where(Author.id==n.author).get().ln
            n3=n1+" "+n2
            tp=(n.title,n.body,n.date,n.img,n3)
            list1.append(tp)
            cnt+=1
            if cnt==10:
                break
        self.render('index.html',UN= "Hello!",list1=list1)
