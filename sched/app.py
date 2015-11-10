from flask import Flask
from flask import url_for, request, make_response, g
import random
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from sched.models import Base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sched.db'
# postgresql://user:pass@localhost:5432/database_name
# pip install psycopg2
# mysql://user:pass@localhost:3306/database_name
# pip install mysql-python

# Use Flask-SQLAlchemy for its engine and session
# configuration. Load the extension, giving it the app object,
# and override its default Model class with the pure
# SQLAlchemy declarative Base class.
db = SQLAlchemy(app)
db.Model = Base


@app.route('/')
def hello_world():
    return 'Welcome to the Flask World!' + url_for('static', filename='img/flask_logo.png')


@app.route('/string/')
def return_string():
    return make_response('Welcome to the Flask World handling string !', 200)


@app.route('/object/')
def return_object():
    headers = {'Content-Type': 'text/plain'}
    return make_response('Hello, world!', 200, headers)


@app.route('/tuple/')
def return_tuple():
    return 'Hello, world!', 200, {'Content-Type':
                                      'text/plain'}


@app.route('/appointments/')
def appointment_list():
    return 'Listing of all appointments we have.'


@app.route('/appointments/<int:appointment_id>/')
def appointment_detail(appointment_id):
    edit_url = url_for('appointment_edit', appointment_id=appointment_id)
    return edit_url


@app.route('/appointments/<int:appointment_id>/edit/', methods=['GET', 'POST'])
def appointment_edit(appointment_id):
    return 'Form to edit appointment #.'.format(appointment_id)


@app.route('/appointments/create/', methods=['GET', 'POST'])
def appointment_create():
    return 'Form to create a new appointment.'


@app.route('/appointments/<int:appointment_id>/delete/', methods=['DELETE'])
def appointment_delete(appointment_id):
    raise NotImplementedError('DELETE')


def dump_request_detail(request):
    request_detail = """
# Before Request #
request.endpoint: {request.endpoint}
request.method: {request.method}
request.view_args: {request.view_args}
request.args: {request.args}
request.form: {request.form}
request.user_agent: {request.user_agent}
request.files: {request.files}
request.is_xhr: {request.is_xhr}

## request.headers ##
{request.headers}
  """.format(request=request).strip()
    return request_detail


@app.before_request
def callme_before_every_request():
    x = random.randint(0, 9)
    app.logger.debug('before request: g.x is {x}'.format(x=x))
    g.x = x  # Demo only: the before_request hook.
    app.logger.debug(dump_request_detail(request))


@app.after_request
def callme_after_every_response(response):
    # Demo only: the after_request hook.
    app.logger.debug('# After request: g.x is {g.x}'.format(g=g))
    app.logger.debug('# After Request #\n' + repr(response))
    return response


if __name__ == '__main__':
    app.run()
