import os
import xmlrpclib
import datetime
import json

from base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self):
        self.render("index.html")

class RSDHandler(BaseHandler):
    def get(self):
        self.render("rsd.html")

class ServiceWordpressHandler(BaseHandler):
    def post(self):
        see = xmlrpclib.loads(self.request.body)
        print(see)
        #(('1', '', '', {'number': 30, 'offset': 0}, ['post', 'terms', 'custom_fields', 'enclosure']), u'wp.getPosts')
        if see[1] == 'wp.getPosts':
            p = Post()
            p.post_mime_type = ""
            p.short_url = "http://localhost:5000/first-post"
            p.post_date_gmt = datetime.datetime.utcnow()
            p.sticky = False 
            p.post_date = datetime.datetime.utcnow() 
            p.post_type = "post" 
            p.post_modified = datetime.datetime.utcnow() 
            p.menu_order = 0
            p.guid = "http://localhost:5000/first-post"
            p.enclosure = []
            p.custom_fields = []
            p.post_title = "First Psot"
            p.post_status = "publish"
            p.post_content = "He y there."
            p.post_parent = "0" 
            p.post_password = ""
            p.terms = []
            p.post_thumbnail = [] 
            p.ping_status = "closed"
            p.post_id = "1" 
            p.link = "http://localhost:5000/first-post"
            p.post_author = "1"
            p.comment_status = "closed" 
            p.post_format = "standard" 
            p.post_name = "first-post"
            p.post_modified_gmt = datetime.datetime.utcnow()
            p.post_excerpt = ""

            response = (([p.__dict__,]), )
            xml_response = xmlrpclib.dumps(response)
            self.set_header("Content-Type", 'application/xml; charset="utf-8"')
            self.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            self.write('<methodResponse>\n')
            self.write(xml_response)
            self.write('</methodResponse>\n')
            print('<?xml version="1.0" encoding="UTF-8"?>')
            print(xml_response)
        
class Post:
    def __init__(self):
        self.post_mime_type = ""
        self.short_url = ""
        self.post_date_gmt = None
        self.sticky = False 
        self.post_date = None
        self.post_type = "post" 
        self.post_modified = None
        self.menu_order = 0
        self.guid = ""
        self.enclosure = []
        self.custom_fields = []
        self.post_title = ""
        self.post_status = ""
        self.post_content = ""
        self.post_parent = "", 
        self.post_password = "", 
        self.terms = []
        self.post_thumbnail = [] 
        self.ping_status = ""
        self.post_id = "" 
        self.link = ""
        self.post_author = ""
        self.comment_status = "" 
        self.post_format = "" 
        self.post_name = ""
        self.post_modified_gmt = None
        self.post_excerpt = ""

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)



