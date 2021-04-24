from flask_script import Manager,Server
from app import create_app,db

app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)


if __name__ == '__main__':
  app.run(debug=True)