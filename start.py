import os

cwd = os.getcwd()
os.environ["FLASK_APP"] = 'server.py'
os.environ["FLASK_DEBUG"] = '1'

os.system('flask run')
