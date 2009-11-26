#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Utility functions. 
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
from functools import partial
from haggoo.template.jinja2.filters import datetimeformat
from haggoo.template.jinja2.loaders import PythonLoader
from jinja2 import Environment, FileSystemLoader
from urllib import urlencode

# Set up the Jinja2 Environment to use the correct loader.
# Also add a few custom filters for templates.
template_directories = configuration.TEMPLATE_DIRS
if configuration.DEPLOYMENT_MODE == configuration.MODE_PRODUCTION:
    template_loader = PythonLoader
else:
    template_loader = FileSystemLoader

jinja_env = Environment(loader=template_loader(template_directories))
jinja_env.filters['datetimeformat'] = datetimeformat
jinja_env.filters['urlencode'] = urlencode

def render_template_generator(template_builtins=configuration.TEMPLATE_BUILTINS):
    def render_template(template_name, **context):
        """
        Fills a template with values provided as context.
    
        The function also includes a few template builtins that are available to all 
        rendered templates.
    
        """
        template = jinja_env.get_template(template_name)
        new_context = {}
        new_context.update(template_builtins)
        new_context.update(context)
        return template.render(new_context)
    return render_template

render_template = render_template_generator()

# Conveninence wrapper to make sure int conversion uses a decimal base. 
dec = partial(int, base=10)

