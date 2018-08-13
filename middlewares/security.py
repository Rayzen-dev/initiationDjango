import re

from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from urllib.parse import quote
from django.conf import settings

from api.apps import ApiConfig

class ApiRequestMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        url = request.path_info.lstrip('/').split('/')
        if request.method.upper() == 'GET' and url[0].lower() == 'api':
            raise Http404

        response = self.get_response(request)
        # not for production or production like environment
        if not settings.DEBUG:
            return response

        # do nothing for actual ajax requests
        if request.is_ajax() or not request.GET.get('_debug'):
            return response

        # only do something if this is a json response
        if response['Content-Type'].lower().startswith('application/json'):
            title = (
                    'JSON as HTML Middleware for: %s' %
                    quote(request.get_full_path())
            )
            content = response.content
            content = content.replace('<', '&lt;').replace('>', '&gt;')
            response.content = (
                    '<!doctype html>\n<html><head><title>%s</title>'
                    '<meta content="text/html; charset=UTF-8" '
                    'http-equiv="Content-Type">'
                    '</head>\n<body>\n%s\n</body></html>'
                    % (title, content)
            )
            response['Content-Type'] = 'text/html'

        return response
