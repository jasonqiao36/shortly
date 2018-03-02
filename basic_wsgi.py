from werkzeug.wrappers import Response, Request


def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return [b'hello jason']


def resp_app(environ, start_response):
    resp = Response('hello jason', mimetype='text/plain')
    return resp(environ, start_response)


def req_app(environ, start_response):
    request = Request(environ)
    text = 'hello {}'.format(request.args.get('name'))
    resp = Response(text, mimetype='text/plain')
    return resp(environ, start_response)
