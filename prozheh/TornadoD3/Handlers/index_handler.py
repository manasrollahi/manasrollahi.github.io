import tornado

__author__ = 'mojtaba.banaie'
# from pycket.session import SessionManager
from models import *
from datetime import datetime
import khayyam3

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        news = News.select().order_by(News.id.desc())
        cnt=0
        list1=[]
        kh=khayyam3.JalaliDate.today()
        week=datetime.weekday(datetime.today())
        if week==0:
            week="دوشنبه"
        elif week==1:
            week="سه شنبه"
        elif week==2:
            week="چهار شنبه"
        elif week==3:
            week="پنج شنبه"
        elif week==4:
            week="جمعه"
        elif week==5:
            week="شنبه"
        else:
            week="یکشنبه"
        # print(week)
        kh=str(kh)
        list2=[]
        for k in kh.split("-"):
            list2.append(k)
        kh='%s/%s/%s'%(list2[0],list2[1],list2[2])+ "   " + week
        for n in news:
            n1=Author.select().where(Author.id==n.author).get().fn
            n2=Author.select().where(Author.id==n.author).get().ln
            n3=n1+" "+n2
            tp=(n.title,n.body,n.date,n.img,n3)
            list1.append(tp)
            cnt+=1
            if cnt==10:
                break
        self.render('index.html',UN= "Hello!",list1=list1,kh=kh)
