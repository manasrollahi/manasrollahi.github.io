import tornado
from  models import *
import peewee

__author__ = 'mojtaba.banaie'

class CategoryHandler(tornado.web.RequestHandler):
     def get(self):
        categories = Category.select()
        self.render('categories.html', categories = categories)



class CategoryEditHandler(tornado.web.RequestHandler):
     def get(self, *args):
       cat_id=args[0]
       catInfo = Category.select().where(Category.id == cat_id).get()
       self.render("category-edit.html",category=catInfo)


     def post(self, *args):
       cat_id=args[0]
       catInfo = Category.select().where(Category.id == cat_id).get()


       catInfo.name = self.get_argument("category-name")
       catInfo.save()


       self.redirect("/category")



class CategoryDeleteHandler(tornado.web.RequestHandler):
     def get(self, *args):
       cat_id=args[0]
       catInfo = Category.select().where(Category.id == cat_id).get().delete_instance()
       self.redirect("/category")



class CategoryNewHandler(tornado.web.RequestHandler):
     def get(self, *args):
       self.render("category-new.html")


     def post(self, *args):

       catName = self.get_argument("category-name")
       catInfo = Category.create(
           name=catName
       )

       self.redirect("/category")