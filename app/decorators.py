# -*- coding: utf-8 -*-
"""Decorators, especially view decorators."""
from functools import wraps
import json
import pprint

from flask import request, render_template, make_response

def templated(template=None):
    """Render a template using the decorated function as the context."""
    #pylint: disable-msg=C0111
    def decorator(view_fn):
        @wraps(view_fn)
        def decorated_function(*args, **kwargs):
            template_name = template
            if template_name is None:
                template_name = request.endpoint.replace('.', '/') + '.html'
            ctx = view_fn(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx
            return render_template(template_name, **ctx)
        return decorated_function
    return decorator

def json_response(json_fn):
    """
    Take a function that yields a JSON string and wrap it in
    the proper response.
    """
    @wraps(json_fn)
    def decorated_function(*args, **kwargs):
        response = make_response(json_fn(*args, **kwargs))
        response.headers['Content-Type'] = 'application/json'
        return response
    return decorated_function


def pprint_json_response(view_fn):
    """Decorator that makes a JSON view more human-readble."""
    #pylint: disable-msg=C0111
    @wraps(view_fn)
    def wrapped(*args, **kwargs):
        return pprint_json(view_fn(*args, **kwargs))
    return wrapped

def pprint_json(json_string):
    """Take a JSON string and pretty-format with some HTML."""
    return (pprint.pformat(
        json.loads(json_string), indent=2)
            .replace('\n','<br>')
            .replace('  ', '&nbsp;&nbsp;')
            .replace("u'", "'"))
