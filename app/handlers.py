#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Main handlers.
# Copyright (c) 2009 happychickoo.
#
# The MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import configuration
from gaefy.db.datastore_cache import DatastoreCachingShim
from google.appengine.ext import db, webapp
from google.appengine.api import memcache
from google.appengine.ext.webapp.util import run_wsgi_app
from gaefy.jinja2.code_loaders import FileSystemCodeLoader
from haggoo.template.jinja2 import render_generator
import logging

# Set up logging.
logging.basicConfig(level=logging.DEBUG)

render_template = render_generator(loader=FileSystemCodeLoader, builtins=configuration.TEMPLATE_BUILTINS)

# Handlers
class IndexHandler(webapp.RequestHandler):
    """Handles the home page requests."""
    def get(self):
        response = render_template('index.html')
        self.response.out.write(response)
        
class FleetServiceHandler(webapp.RequestHandler):
    """Handles the home page requests."""
    def get(self):
        response = render_template('fleet.html')
        self.response.out.write(response)
        
class LogisticsServiceHandler(webapp.RequestHandler):
    """Handles the home page requests."""
    def get(self):
        response = render_template('logistics.html')
        self.response.out.write(response)                        
        
class ConstructionServiceHandler(webapp.RequestHandler):
    """Handles the home page requests."""
    def get(self):
        response = render_template('construction.html')
        self.response.out.write(response)            

class DrillingServiceHandler(webapp.RequestHandler):
    """Handles the home page requests."""
    def get(self):
        response = render_template('drilling.html')
        self.response.out.write(response)
        
class QHSEServiceHandler(webapp.RequestHandler):
    """Handles the home page requests."""
    def get(self):
        response = render_template('qhse.html')
        self.response.out.write(response)

class OfficesContactHandler(webapp.RequestHandler):
    """Handles the home page requests."""
    def get(self):
        response = render_template('contacts.html')
        self.response.out.write(response)
                        
class CareerHandler(webapp.RequestHandler):
    """Handles the home page requests."""
    def get(self):
        response = render_template('careers.html')
        self.response.out.write(response)

class TourHandler(webapp.RequestHandler):
    """Handles the home page requests."""
    def get(self):
        response = render_template('tour.html')
        self.response.out.write(response)
        
class PolicyHandler(webapp.RequestHandler):
    """Handles the home page requests."""
    def get(self):
        response = render_template('policy.html')
        self.response.out.write(response)
        
class PressReleaseHandler(webapp.RequestHandler):
    """Handles the home page requests."""
    def get(self):
        response = render_template('press_release.html')
        self.response.out.write(response)          

# URL-to-request-handler mappings.
urls = (
    ('/', IndexHandler),
    ('/careers/?', CareerHandler),
    ('/policy/?', PolicyHandler),
    ('/press_release/?', PressReleaseHandler),
    ('/careers/tour/?', TourHandler),
    ('/services/fleet/?', FleetServiceHandler),
    ('/services/logistics/?', LogisticsServiceHandler),
    ('/services/construction/?', ConstructionServiceHandler),
    ('/services/drilling/?', DrillingServiceHandler),
    ('/services/qhse/?', QHSEServiceHandler),
    ('/contact/offices/?', OfficesContactHandler),
)

# Web application entry-point.
def main():
    application = webapp.WSGIApplication(urls, debug=configuration.DEBUG)
    DatastoreCachingShim.Install()
    run_wsgi_app(application)
    DatastoreCachingShim.Uninstall()

if __name__ == '__main__':
    main()

