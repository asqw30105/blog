from django.shortcuts import render
from django.http import HttpResponse
def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    return HttpResponse('Hello world!')
    '''
    Render the main page
    '''
    html = '''
    <!doctype html>
    <html>
    <head>
    <title>部落格</title>
    <meta charset="utf-8">
    </head>
    <body>
    <p>這是 HTML 版的 Hello world!</p>
    </body>
    </html>
    return HttpResponse(html)
    '''
    return HttpResponse('Hello world!')