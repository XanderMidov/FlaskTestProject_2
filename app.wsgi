import sys
activate_this = 'C:/Users/Xander/PycharmProjects/FlaskTestProject_2/venv/Scripts/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

sys.path.insert(0, 'C:/Users/Xander/PycharmProjects/FlaskTestProject_2')
from app import app as application