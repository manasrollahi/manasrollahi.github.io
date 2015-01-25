__author__ = 'Mohammad ali'

from Handlers.index_handler import IndexHandler
from Handlers.news_handler import NewsHandler,NewsEditHandler,NewsDeleteHandler,NewsNewHandler
from Handlers.log_handler import LogHandler,LogoutHandler

urlList  = [
    (r'/', IndexHandler),
    (r'/news$', NewsHandler),
    (r'/news/edit/(\d+)$', NewsEditHandler),
    (r'/news/delete/(\d+)$', NewsDeleteHandler),
    (r'/news/new$', NewsNewHandler),
    (r'/login$', LogHandler),
    (r'/logout$',LogoutHandler)
]