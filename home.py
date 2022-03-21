from flask import Flask
from flask import escape

myapp_obj = Flask(__name__)

#view function
@myapp_obj.route("/")
@myapp_obj.route("/index.html")
def home():
    name = "Lisa"
    city_names = ["Paris", "London", "Rome", "Tahiti"]
    return '''
    <html>
    <h1>Welcome ''' + name + '''!</h1>
    
    <a href="https://www.google.com">not google</a>
    
    <ul>
    
    <li>''' + city_names[0] + '''</li>
    <li>''' + city_names[1] + '''</li>
    <li>''' + city_names[2] + '''</li>
    <li>''' + city_names[3] + '''</li>
    
    </ul>
    
    </html>
    '''

@myapp_obj.route("/hello")
def hello():
    user = {'username': 'Miguel'}
    return '''
    <html>
    <head>
        <title>Home Page - my blog</title> </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
    </html>'''

@myapp_obj.route("/login")
def login():
    return "Login Page!"

@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return escape(name)
myapp_obj.run()