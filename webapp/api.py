'''
    api.py
    Sydney Nguyen, Sophia Wang, and Kimberly Yip
    Code borrowed from Jeff Ondich, 25 April 2016
    Updated 9 November 2022

    Sample Flask API to support the tiny board games web application.
'''
import sys
import flask
import json
import config
import psycopg2

api = flask.Blueprint('api', __name__)

def get_connection():
    ''' Returns a connection to the database described in the
        config module. May raise an exception as described in the
        documentation for psycopg2.connect. '''
    return psycopg2.connect(database=config.database,
                            user=config.user,
                            password=config.password,
                            port=config.port)

''' Route that returns all games in alphabetical order'''
@api.route('/games/')
def get_games():
    query = '''SELECT * FROM games ORDER BY games.name ASC'''
    games_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        print(cursor.query)
        for row in cursor:
            game = {'game_id':row[0],
                      'name':row[1],
                      'rank': row[2],
                      'min_player':row[3],
                      'max_player':row[4],
                      'avg_time':row[5],
                      'min_time':row[6],
                      'max_time':row[7],
                      'avg_rating':row[8],
                      'num_votes':row[9],
                      'image_url':row[10],
                      'min_age':row[11],
                      'num_owned':row[12],
                      'pub_year':row[13],
                      'complexity':row[14]
                      }
            games_list.append(game)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(games_list)

'''Route that returns all the categories'''
@api.route('/games/sidebar/category')
def get_all_category():
    query = '''SELECT * FROM categories ORDER BY categories.category ASC'''
    category_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            category = {'category_id':row[0], 'category': row[1]}
            category_list.append(category)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(category_list)

'''Route that gets all the discrete minimum ages'''
@api.route('/games/sidebar/min_age')
def get_all_min_age():
    query = '''SELECT games.min_age FROM games GROUP BY games.min_age ORDER BY games.min_age ASC'''
    min_age_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            min_age = {'min_age': row[0]}
            min_age_list.append(min_age)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(min_age_list)

'''Route that gets all the discrete publish years'''
@api.route('/games/sidebar/pub_year')
def get_all_pub_year():
    query = '''SELECT games.pub_year FROM games GROUP BY games.pub_year ORDER BY games.pub_year ASC'''
    pub_year_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            pub_year = {'pub_year': row[0]}
            pub_year_list.append(pub_year)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(pub_year_list)

'''Route that gets all the discrete minimum players'''
@api.route('/games/sidebar/min_player')
def get_all_min_player():
    query = '''SELECT games.min_player FROM games GROUP BY games.min_player ORDER BY games.min_player ASC'''
    min_player_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            min_player = {'min_player': row[0]}
            min_player_list.append(min_player)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(min_player_list)

'''Route that gets all the discrete maximum players'''
@api.route('/games/sidebar/max_player')
def get_all_max_player():
    query = '''SELECT games.max_player FROM games GROUP BY games.max_player ORDER BY games.max_player ASC'''
    max_player_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            max_player = {'max_player': row[0]}
            max_player_list.append(max_player)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(max_player_list)

'''Route that returns game search results by filtered category'''
@api.route('/games/category/<category>')
def get_category(category):
    category = category.split("_")
    query = '''SELECT games.game_id, games.name, categories.category, games.avg_rating, games.image_url
               FROM games, categories, game_categories
               WHERE categories.category = %s
               AND game_categories.game_id = games.game_id
               AND game_categories.category_id = categories.id
               ORDER BY avg_rating DESC'''
    game_category_list = []
    try:
        for item in category:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute(query, (item,))
            for row in cursor:
                game = {'game_id':row[0], 'name':row[1], 'category': row[2], 'image_url': row[4]}
                if game not in game_category_list:
                    game_category_list.append(game)
            cursor.close()
            connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(game_category_list)

'''Route that returns game search results by filtered min age'''
@api.route('/games/min_age/<min_age>')
def get_min_age(min_age):
    min_age = min_age.split("_")
    query = '''SELECT games.game_id, games.name, games.min_age, games.avg_rating, games.image_url
               FROM games
               WHERE games.min_age = %s
               ORDER BY avg_rating DESC'''
    game_min_age_list = []
    try:
        for item in min_age:
            item = int(item)
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute(query, (item,))
            for row in cursor:
                game = {'game_id':row[0], 'name':row[1], 'min_age': row[2], 'image_url': row[4]}
                if game not in game_min_age_list:
                    game_min_age_list.append(game)
            cursor.close()
            connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(game_min_age_list)

'''Route that returns the game search results by filtered published year'''
@api.route('/games/pub_year/<pub_year>')
def get_pub_year(pub_year):
    pub_year = pub_year.split("_")
    print(pub_year)
    query = '''SELECT games.game_id, games.name, games.min_age, games.avg_rating, games.image_url
               FROM games
               WHERE games.pub_year = %s
               ORDER BY avg_rating DESC'''
    game_pub_year_list = []
    try:
        for item in pub_year:
            item = int(item)
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute(query, (item,))
            for row in cursor:
                game = {'game_id':row[0], 'name':row[1], 'min_age': row[2], 'image_url': row[4]}
                if game not in game_pub_year_list:
                    game_pub_year_list.append(game)
            cursor.close()
            connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(game_pub_year_list)

'''Route that returns the game search results by filtered min player'''
@api.route('/games/min_player/<min_player>')
def get_min_player(min_player):
    min_player = min_player.split("_")

    query = '''SELECT games.game_id, games.name, games.min_age, games.avg_rating, games.image_url
               FROM games
               WHERE games.min_player = %s
               ORDER BY avg_rating DESC'''
    game_min_player_list = []
    try:
        for item in min_player:
            item = int(item)
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute(query, (item,))
            for row in cursor:
                game = {'game_id':row[0], 'name':row[1], 'min_age': row[2], 'image_url': row[4]}
                if game not in game_min_player_list:
                    game_min_player_list.append(game)
            cursor.close()
            connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(game_min_player_list)

'''Route that returns the game search results by filtered max player'''
@api.route('/games/max_player/<max_player>')
def get_max_player(max_player):
    max_player = max_player.split("_")

    query = '''SELECT games.game_id, games.name, games.min_age, games.avg_rating, games.image_url
               FROM games
               WHERE games.max_player = %s
               ORDER BY avg_rating DESC'''
    game_max_player_list = []
    try:
        for item in max_player:
            item = int(item)
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute(query, (item,))
            for row in cursor:
                game = {'game_id':row[0], 'name':row[1], 'min_age': row[2], 'image_url': row[4]}
                if game not in game_max_player_list:
                    game_max_player_list.append(game)
            cursor.close()
            connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(game_max_player_list)

'''Route that returns the game search results by filtered search string in game name'''
@api.route('/search_page/<search>')
def get_game_string(search):
    query = '''SELECT * FROM games WHERE games.name ILIKE CONCAT('%%', %s, '%%')'''
    games_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (search,))
        for row in cursor:
            game = {'game_id':row[0],
                      'name':row[1],
                      'rank': row[2],
                      'min_player':row[3],
                      'max_player':row[4],
                      'avg_time':row[5],
                      'min_time':row[6],
                      'max_time':row[7],
                      'avg_rating':row[8],
                      'num_votes':row[9],
                      'image_url':row[10],
                      'min_age':row[11],
                      'num_owned':row[12],
                      'pub_year':row[13],
                      'complexity':row[14]
                      }
            games_list.append(game)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(games_list)

'''Route that returns the game search results by filtered alphabet'''
@api.route('game/alphabetical/<alpha>')
def get_alphabetical(alpha):
    query = '''SELECT * FROM games ORDER BY games.name ASC'''
    games_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        print(cursor.query)
        for row in cursor:
            game = {'game_id':row[0],
                      'name':row[1],
                      'rank': row[2],
                      'min_player':row[3],
                      'max_player':row[4],
                      'avg_time':row[5],
                      'min_time':row[6],
                      'max_time':row[7],
                      'avg_rating':row[8],
                      'num_votes':row[9],
                      'image_url':row[10],
                      'min_age':row[11],
                      'num_owned':row[12],
                      'pub_year':row[13],
                      'complexity':row[14]
                      }
            if alpha.isalpha() and game['name'][0].lower() == alpha.lower():
                games_list.append(game)
            elif alpha == '~':
                if game['name'][0].isalpha() == False:
                    games_list.append(game)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(games_list)

'''Route that adds a user's review to a game's site'''
@api.route('/game/<game_name>/add/<review>', methods=['POST'])
def add_review_text(game_name, review):
  game_id = ''
  game_name = game_name.strip()
  try:
    connection = get_connection()
    cursor = connection.cursor() 
    query = "SELECT game_id FROM games WHERE games.name = %s"
    cursor.execute(query, (game_name,))
    for row in cursor:
      game_id = row[0]
      break

    query = "INSERT INTO game_reviews (game_id, review) VALUES (%s, %s)"
    cursor.execute(query, ( int(game_id), review))
    connection.commit()
    cursor.close()
    connection.close()
    return json.dumps(True) 
  except Exception as e:
    return json.dumps(False)
    
#Credit to Quocodile


'''Connects to database and initializes the cursor.'''
def cursor_init():
    try:
      connection = psycopg2.connect(database=config.database,
                            user=config.user,
                            password=config.password,
                            port=config.port)
      cursor = connection.cursor()
      return connection, cursor
    except Exception as e:
      print(e)
      exit()

