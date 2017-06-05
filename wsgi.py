from prodcast import app as application
import os

application.debug = False

try:
    application.secret_key = os.environ['FLASK_SECRET_KEY']
except:
    application.secret_key = 'reallysecretkey'

application.config['SESSION_TYPE'] = 'filesystem'

if __name__ == '__main__':
    application.run()
