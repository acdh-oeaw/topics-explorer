import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from whitenoise import WhiteNoise
from application.views import web as application
web = application
web.wsgi_app = WhiteNoise(web.wsgi_app, root='application/static/')
