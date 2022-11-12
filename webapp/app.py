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
def home():
    '''route to home'''
    return flask.render_template('index.html')

@app.route('/home_page')
def mockups1():
    '''route to mockups1'''
    return flask.render_template('home_page.html')

@app.route('/boardgame_site') 
def mockups2():
    '''route to mockups2'''
    return flask.render_template('boardgame_site.html')

@app.route('/create_user') 
def mockups3():
    '''route to mockups3'''
    return flask.render_template('create_user.html')

@app.route('/user_home_page') 
def mockups4():
    '''route to mockups4'''
    return flask.render_template('user_home_page.html')

@app.route('/search_page') 
def mockups5():
    '''route to mockups5'''
    return flask.render_template('search_page.html')

@app.route('/login_page') 
def mockups6():
    '''route to mockups6'''
    return flask.render_template('login_page.html')

@app.route('/forgot_password_page')
def mockups7():
    '''route to mockups7'''
    return flask.render_template('forgot_password.html')

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A books-and-authors application, including API & DB')
    parser.add_argument('host', help='the host to run on')
    parser.add_argument('port', type=int, help='the port to listen on')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
