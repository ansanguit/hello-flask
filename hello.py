#we are creating a local server.For that, we copy the starting code from Flask and then, in the console we input
# $ export FLASK_APP=nameofthefile.py and the run $ flask run.
# We will get the local IP server address where we can find the server.
# The same can be done when we use dthe built in attribute __main__
# __main__ denotes the file that is running from and not the imported module.
# if __name__ == "__main__":
#     # execute only if run as a script
#     app.run()

from flask import Flask
app = Flask(__name__)


@app.route('/') #This is called a Python decorator. It's a way to add something to a function. The sintax is @name_of_decorator
def hello_world():
    return 'Hello, World!'
@app.route('/ciao')
def say_ciao():
    return 'Ciao Bella'


if __name__ == "__main__":
     # execute only if run as a script
    app.run()
