from gevent.wsgi import WSGIServer
from app_html import app_html

app_html.debug = True
WSGIServer(('', 5000), app_html).serve_forever()