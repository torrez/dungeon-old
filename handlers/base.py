import os
import random
import string

import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        super(BaseHandler, self).initialize()
