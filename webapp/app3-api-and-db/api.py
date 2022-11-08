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
                            port='5433')


@api.route('/games/')
def get_games():
    query = '''SELECT * FROM board_game'''
    games_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            game = {'id_board_game':row[0],
                      'board_game_title':row[1],
                      'year_published':row[2],
                      'min_players':row[3],
                      'max_players':row[4],
                      'play_time':row[5],
                      'min_age':row[6],
                      'category_id':row[7],
                      'users_rated':row[8],
                      'rating_avg':row[9],
                      'bgg_rank':row[10],
                      'owned_users':row[11],}
            games_list.append(game)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(games_list)


