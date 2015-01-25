import tornado

__author__ = 'mojtaba.banaie'
# from pycket.session import SessionManager
from models import *

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        news = News.select().order_by(News.id.desc())
        # auth=Author.select(Author.ln)
        # idd=News.select().get().author
        # print(idd)
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
            # n.author=n3
            # print(tp)
            # fn=Author.select().where(Author.id==int(n.id)).get().fn
            # ln=Author.select().where(Author.id==int(n.id)).get().ln
            # auth=fn+" "+ln
            # list1.append(auth)
        # fn=Author.select().where(Author.id==idd).get().fn
        # ln=Author.select().where(Author.id==idd).get().ln
        # auth=fn+" "+ln
        self.render('index.html',UN= "Hello!",list1=list1)
        # else :
        #     session.set('LoggedIn', {"_id":"12222222","name":"ali"})
        #     self.render('index.html',UN="U Are Not Logged In..")
