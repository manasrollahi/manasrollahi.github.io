__author__ = 'Mohammad ali'


import tornado
from  models import *
import peewee
from datetime import datetime
# import jdate



# import shutil
# import os
from pycket.session import SessionManager

class NewsHandler(tornado.web.RequestHandler):
     def get(self):
         auth=Login.select().get().log
         if auth!=0:
             news = News.select().order_by(News.id.desc())
             self.render('news.html', news = news)
         else:
             self.redirect("/login")


     def post(self,*args):
         self.render("news-new.html")


class NewsEditHandler(tornado.web.RequestHandler):
     def get(self, *args):
       news_id=args[0]
       newsInfo = News.select().where(News.id == news_id).get()
       self.render("news-edit.html",news=newsInfo)


     def post(self, *args):
       news_id=args[0]
       newsInfo = News.select().where(News.id == news_id).get()


       newsInfo.title = self.get_argument("news-title")
       newsInfo.body = self.get_argument("news-body")
       date=datetime.date(datetime.now())
       # dd=datetime.date(datetime.day.now())
       # dm=datetime.date(datetime.monthy.now())
       # dy=datetime.date(datetime.year.now())
       # jd = jdate.gregorian_to_jd(dy,dm,dd)
       # tp=jdate.jd_to_persian(jd)
       # year=int(tp[0])
       # month=int(tp[1])
       # day=int(tp[2])
       # dat=str(year)+"/"+str(month)+"/"+str(day)
       # # datetime.astimezone()
       # print(dat)
       newsInfo.date=str(date)
       # newsInfo.date = self.get_argument("news-date")
       newsInfo.img = self.get_argument("news-img")
       auth=Login.select().get().log
       newsInfo.author=auth
       newsInfo.save()


       self.redirect("/news")



class NewsDeleteHandler(tornado.web.RequestHandler):
     def get(self, *args):
       news_id=args[0]
       newsInfo = News.select().where(News.id == news_id).get().delete_instance()
       self.redirect("/news")



class NewsNewHandler(tornado.web.RequestHandler):
     def get(self, *args):
       self.render("news-new.html")


     def post(self, *args):

       newsTitle = self.get_argument("news-title")
       newsBody=self.get_argument("news-body")
       date=datetime.date(datetime.now())
       # datetime.astimezone()
       # print(date)
       newsDate=str(date)
       # newsDate=self.get_argument("news-date")
       newsImg=self.get_argument("news-img")
       auth=Login.select().get().log
       newsAuthor=auth
       newsInfo = News.create(
           title=newsTitle,
           body=newsBody,
           date=newsDate,
           img=newsImg,
           author=newsAuthor
       )

       self.redirect("/news")


class del_copy:
    src=""
    def copyLargeFile(self,src, dest, buffer_size=16000):
        with open(src, 'rb') as fsrc:
            with open(dest, 'wb') as fdest:
                shutil.copyfileobj(fsrc, fdest, buffer_size)

    def delfile(self,src):
        os.remove(src)