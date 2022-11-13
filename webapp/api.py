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
    query = '''SELECT * FROM games'''
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
                      'designer_id':row[13],
                      'pub_year':row[14],
                      'weight':row[15]
                      }
            games_list.append(game)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(games_list)


@api.route('/games/<game_id>')
def get_info_for_game(game_id):
    query = '''SELECT game_id, name, avg_rating
               FROM games
               WHERE games.game_id = %s
               ORDER BY games.pub_year DESC'''
    game_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (game_id,))
        print(game_id)
        for row in cursor:
            game = {'game_id':row[0], 'name':row[1], 'avg_rating':row[8]}
            game_list.append(game)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(game_list)

@api.route('/games/<category>')
def get_info_for_game(genre):
    query = '''SELECT game.game_id, games.name, categories.category, games.avg_rating
               FROM games, categories, game_categories
               WHERE categories.category = %s
               AND game_categories.game_id = game.game_id
               AND game_categories.category_id = categories.id
               ORDER BY avg_rating DESC'''
    game_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (category,))
        for row in cursor:
            game = {'game_id':row[0], 'name':row[1], 'avg_rating':row[8]}
            game_list.append(game)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(game_list)

