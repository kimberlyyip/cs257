'''
    app.py
    Authors: Sydney Nguyen, Sophia Wang, Kimberly Yip 

    A small Flask application that provides a barelywebsite with an accompanying
    API (which is also tiny) to support that website.
'''
import flask
import argparse
import api

app = flask.Flask(__name__, static_folder='static', template_folder='templates')
app.register_blueprint(api.api, url_prefix='/api')


@app.route('/') 
'''route to home'''
def home():
    return flask.render_template('index.html')

@app.route('/mockups1') 
'''route to mockups1'''
def mockups1():
    return flask.render_template('mocksup1.html')

@app.route('/mocksup2') 
'''route to mockups2'''
def mockups2():
    return flask.render_template('mockups2.html')

@app.route('/mockups3') 
'''route to mockups3'''
def mockups3():
    return flask.render_template('index.html')

@app.route('/mockups4') 
'''route to mockups4'''
def mockups4():
    return flask.render_template('mockups4.html')

@app.route('/mockups5') 
'''route to mockups5'''
def mockups5():
    return flask.render_template('mocksup5.html')

@app.route('/mockups6') 
'''route to mockups6'''
def mockups6():
    return flask.render_template('mockups6.html')

@app.route('/mockups7')
'''route to mockups7'''
def mockups7():
    return flask.render_template('mockups7.html')

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A books-and-authors application, including API & DB')
    parser.add_argument('host', help='the host to run on')
    parser.add_argument('port', type=int, help='the port to listen on')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
