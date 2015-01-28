import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from pycket.session import SessionManager
from tornado.options import define, options
from urls import urlList

define("port", default=8190, help="run on the given port", type=int)

# Your app launch code here..
class MedxApplication(tornado.web.Application):

    def __init__(self):
        # self.db = ["Medex"]
        handlers = urlList
        settings = dict(
            debug=True,
            cookie_secret="61oETz3455545gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path= os.path.join(os.path.dirname(__file__), "static"),
            # **{
            #     'pycket': {
            #         'engine': 'redis',
            #         'storage': {
            #             'host': sh_connection.auth_system['redis']['host'],
            #             'port': sh_connection.auth_system['redis']['port'],
            #             'password': sh_connection.auth_system['redis']['password'],
            #             'db_sessions': sh_connection.auth_system['redis']['db_sessions'],
            #             'db_notifications': sh_connection.auth_system['redis']['db_notifications'],
            #             'max_connections': 2 ** 31,
            #         },
            #         'cookies': {
            #             'expires_days': 120,
            #         },
            #     },
            # }
        )
        tornado.web.Application.__init__(self,handlers,**settings)

if __name__ == '__main__':
    tornado.options.parse_command_line()


    http_server = tornado.httpserver.HTTPServer(MedxApplication())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()