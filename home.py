from flask import Flask
from flask import escape

myobj = Flask(__name__)
name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]


#view function
@myobj.route("/")
@myobj.route("/index.html")
def home():

    return '''
    <html>
    <h1>Welcome, ''' + name + '''!</h1>
    
    <a href="https://www.google.com">not google</a>
    
    <ul>
    
    <li>''' + city_names[0] + '''</li>
    <li>''' + city_names[1] + '''</li>
    <li>''' + city_names[2] + '''</li>
    <li>''' + city_names[3] + '''</li>
    
    </ul>
    
    </html>
    '''

#myapp_obj.run()