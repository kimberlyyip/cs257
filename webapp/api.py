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


@api.route('/games/<game_name>')
def get_info_for_game(game_id):
    query = '''SELECT game_id, name, avg_rating
               FROM games
               WHERE games.name = %s
               ORDER BY games.pub_year DESC'''
    game_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (game_id,))
        print(game_id)
        for row in cursor:
            game = {'game_id':row[0], 'name':row[1], 'avg_rating':row[2]}
            game_list.append(game)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(game_list)

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

@api.route('/games/category/<category>')
def get_category(category):
    category = category.split("_")
    print(category)
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

@api.route('/search_page/<search>')
def get_game_string(search):
    print(search)
    query = '''SELECT * FROM games WHERE games.name ILIKE CONCAT('%%', %s, '%%')'''

    # search_string = flask.request.args.get('search')           
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
        print(games_list)
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(games_list)

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

