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

def pageable(games_list, page_number):
    page_number = int(page_number)
    page_games_list = []
    remainder = len(games_list)%500
    if remainder == 0:
        num_pages = len(games_list)//500
        start = 500 * (page_number - 1)
        end = 500 * page_number
        page_games_list = games_list[start:end]
    elif remainder < 500:
        num_pages = len(games_list)//500
        if num_pages == 0:
            page_games_list = games_list[0:len(games_list)]
        else:
            if page_number <= num_pages:
                start = 500 * (page_number -1)
                end = 500 * page_number
                page_games_list = games_list[start:end]
            else:
                start = 500 * (page_number -1)
                page_games_list = games_list[start:len(games_list)]
    return page_games_list


@api.route('/games/')
def get_games():
    page_number = flask.request.args.get('page')
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
        page_games_list = pageable(games_list, page_number)
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(page_games_list)


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

@api.route('/games/category/<category>')
def get_category(category):
    page_number = flask.request.args.get('page')
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
            page_games_list = pageable(game_category_list, page_number)
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(page_games_list)

@api.route('/games/min_age/<min_age>')
def get_min_age(min_age):
    page_number = flask.request.args.get('page')
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
            page_games_list = pageable(game_min_age_list, page_number)
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(page_games_list)

@api.route('/games/pub_year/<pub_year>')
def get_pub_year(pub_year):
    page_number = flask.request.args.get('page')
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
            page_games_list = pageable(game_pub_year_list, page_number)
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(game_pub_year_list)

@api.route('/search_page/<search>')
def get_game_string(search):
    page_number = flask.request.args.get('page')
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
        page_games_list = pageable(games_list, page_number)
    except Exception as e:
        print(e, file=sys.stderr)

    return json.dumps(page_games_list)

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
@api.route('/game/<game_name>/review')
def get_all_reviews(game_name):
   query = "SELECT review FROM game_reviews, games WHERE game_reviews.game_id = games.game_id AND games.name = %s"
   
   output = []
   try:
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query,(game_name,))
    print(cursor.query)
    for row in cursor:
        output.append(row[0])
   except Exception as e:
    return json.dumps(output)
