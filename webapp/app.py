'''
    app.py
    Authors: Sydney Nguyen, Sophia Wang, Kimberly Yip 

    A small Flask application that provides a barelywebsite with an accompanying
    API (which is also tiny) to support that website.
'''
import flask
import argparse
import api
from api import cursor_init

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

@app.route('/game/<rank>')
def gamedata(rank):
    connection, cursor = cursor_init()

    query = "SELECT rank, name, avg_rating, min_player, max_player, min_time, max_time, min_age, pub_year, weight FROM games WHERE games.rank = %s"
    cursor.execute(query, (rank,))

    for row in cursor:
        rank = row[0]
        name = row[1]
        avg_rating = row[2]
        min_players = row[3]
        max_players = row[4]
        min_time = row[5]
        max_time = row[6]
        min_age = row[7]
        pub_year = row[8]
        complexity = row[9]


       

    game_data =(rank, name, avg_rating, min_players, max_players,min_time,max_time,min_age,pub_year,complexity)


    #take id, do search, hand back info 
    '''route to mockups7'''
    return flask.render_template('boardgame_site.html', game_data=game_data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('A board games application, including API & DB')
    parser.add_argument('host', help='the host to run on')
    parser.add_argument('port', type=int, help='the port to listen on')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
