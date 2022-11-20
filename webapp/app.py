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
    return flask.render_template('home_page.html')

@app.route('/home_page') 
def homepage():
    '''route to homepage'''
    return flask.render_template('home_page.html')

@app.route('/search_page') 
def search_page():
    '''route to search page'''
    return flask.render_template('search_page.html')

@app.route('/game/<name>')
def gamedata(name):
    '''route to individual board game site'''
    connection, cursor = cursor_init()

    query = "SELECT rank, name, avg_rating, min_player, max_player, min_time, max_time, min_age, pub_year, complexity, image_url FROM games WHERE games.name = %s"
    cursor.execute(query, (name,))

    for row in cursor:
        rank = row[0]
        name = row[1]
        avg_rating = round(row[2],2)
        min_players = row[3]
        max_players = row[4]
        min_time = row[5]
        max_time = row[6]
        min_age = row[7]
        pub_year = row[8]
        complexity = round(row[9],2)
        image_url = row[10]

    game_data =(rank, name, avg_rating, min_players, max_players,min_time,max_time,min_age,pub_year,complexity,image_url)


    query = "SELECT DISTINCT category FROM games, game_categories, categories WHERE games.game_id = game_categories.game_id AND categories.id = game_categories.category_id AND games.rank = %s"
    cursor.execute(query, (rank,))

    categories = ''
    for row in cursor:
        categories += str(row).strip('\'(),') 
        categories += ', '

    categories = categories[:-2]

    query = "SELECT DISTINCT designer FROM games, game_designers, designer WHERE games.game_id = game_designers.game_id AND designer.id = game_designers.designer_id AND games.rank = %s"
    cursor.execute(query, (rank,))

    designers = ''
    for row in cursor:
        designers += str(row).strip('\'(),') 
        designers += ', '

    designers = designers[:-2]

    query = "SELECT DISTINCT review FROM game_reviews, games WHERE game_reviews.game_id = games.game_id AND games.name ILIKE CONCAT('%%', %s, '%%')"
    output = []
    
    cursor.execute(query,(name,))
    print(cursor.query)
    for row in cursor:
        
        output.append(row[0])

        
    cursor.close()
    connection.close()

    #take id, do search, hand back info 

    return flask.render_template('boardgame_site.html', game_data=game_data, categories=categories,designers=designers, output=output)

@app.route('/api/help')
def help():
    return flask.render_template('help.html')

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A board games application, including API & DB')
    parser.add_argument('host', help='the host to run on')
    parser.add_argument('port', type=int, help='the port to listen on')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
