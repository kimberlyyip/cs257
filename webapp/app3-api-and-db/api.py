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
    return psycopg2.connect(database='boardgames',
                            user='loaner',
                            password='',
                            port='5433')

@api.route('/authors/') 
def get_authors():
    ''' Returns a list of all the authors in our database. See
        get_author_by_id below for description of the author
        resource representation.

        By default, the list is presented in alphabetical order
        by surname, then given_name. You may, however, use
        the GET parameter sort to request sorting by birth year.

            http://.../authors/?sort=birth_year

@api.route('/board_games/') 
def get_board_games():
    ''' A JSON list of dictionaries. Each dictionary will represent a single board game, 
    alphabetized by board game name.
        Returns an empty list if there's any database failure.
    '''
    query = '''SELECT id_board_game, Board_game_title, Designer_id, category_id, weight, 
    num_owned, avg_rating, min_players, max_players, min_time, max_time, avg_time, num_votes, img, age
               FROM board_game ORDER BY Board_game_title'''

    sort_argument = flask.request.args.get('sort')
    if sort_argument == 'birth_year':
        query += 'birth_year'
    else:
        query += 'surname, given_name'

    author_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple())
        for row in cursor:
            author = {'id':row[0],
                      'given_name':row[1],
                      'surname':row[2],
                      'birth_year':row[3],
                      'death_year':row[4]}
            author_list.append(author)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(author_list)


@api.route('/games/')
def get_games():
    query = '''SELECT * FROM board_game'''

    # sort_argument = flask.request.args.get('sort')
    # if sort_argument == 'birth_year':
    #     query += 'birth_year'
    # else:
    #     query += 'surname, given_name'

    #author_list = []



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

@api.route('/books/author/<author_id>')
def get_books_for_author(author_id):
    query = '''SELECT books.id, books.title, books.publication_year
               FROM books, authors, books_authors
               WHERE books.id = books_authors.book_id
                 AND authors.id = books_authors.author_id
                 AND authors.id = %s
               ORDER BY books.publication_year'''
    book_list = []
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (author_id,))
        for row in cursor:
            book = {'id':row[0], 'title':row[1], 'publication_year':row[2]}
            book_list.append(book)
        cursor.close()
        connection.close()
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(book_list)


