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
    query = '''SELECT * FROM games'''
    games_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            game = {'rank':row[0],
                      'bgg_url':row[1],
                      'game_id':row[2],
                      'name':row[3],
                      'min_player':row[4],
                      'max_player':row[5],
                      'avg_time':row[6],
                      'min_time':row[7],
                      'max_time':row[8],
                      'pub_year':row[9],
                      'avg_rating':row[10],
                      'geek_rating':row[11],
                      'num_votes':row[12],
                      'image_url':row[13],
                      'min_age':row[14],
                      'mechanic':row[15],
                      'num_owned':row[16],
                      'category':row[17],
                      'designer':row[18],
                      'weight':row[19]
                      }
            games_list.append(game)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(games_list)

