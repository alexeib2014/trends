from django.http import HttpResponse


def index(request):
    '''
    Proxy for index.html
    '''
    file = open('frontend/build/index.html', 'rt')
    html = file.read()
    file.close()

    return HttpResponse(html, content_type='text/html')
