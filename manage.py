from flask.ext.script import Manager
from sched.app import app

manager = Manager(app)
app.config['DEBUG'] = True  # Ensure debugger will load.
app.config['SERVER_NAME'] = 'cgflask.lausanne.ch:5000'
if __name__ == '__main__':
    manager.run()
