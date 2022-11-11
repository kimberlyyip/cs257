'''
    CS.257 Software Design
    Syndey Nguyen, Sophia Wang, Kimberly Yip
    Professor Jeff Ondich

    This program borrows data from kaggle to populate the csv files created here.
    Go to https://www.kaggle.com/datasets/mrpantherson/board-game-data/versions/6?resource=download for the source data. 
    This program assumes you have a copy of the bgg_db_1806.csv.
'''

import csv

def dictionary_map():
    category_list = {}
    with open('bgg_db_1806.csv') as original_data_file,\
      open('categories', 'w') as category_file:
      reader = csv.reader(original_data_file)
      writer = csv.writer(category_file)
      heading_row = next(reader) # skips the first line
      for row in reader:
        category = row[17]
        if category not in category_list:
            category_id = len(category_list) + 1
            category_list[category] = category_id
            writer.writerow([category_id, category])

    designer_list = {}
    with open('bgg_db_1806.csv') as original_data_file,\
      open('designer', 'w') as designer_file:
      reader = csv.reader(original_data_file)
      writer = csv.writer(designer_file)
      heading_row = next(reader) # skips the first line
      for row in reader:
        designer = row[18]
        if designer not in designer_list:
            designer_id = len(designer_list) + 1
            designer_list[designer] = designer_id
            writer.writerow([designer_id, designer])

    with open('bgg_db_1806.csv') as original_data_file,\
      open('games', 'w') as games_file:
      reader = csv.reader(original_data_file)
      writer = csv.writer(games_file)
      heading_row = next(reader) # skips the first line
      for row in reader:
        rank = row[0]
        game_id = row[2]
        name = row[3]
        min_player = row[4]
        max_player = row[5]
        avg_time = row[6]
        min_time = row[7]
        max_time = row[8]
        year_published = row[9]
        avg_rating = row[10]
        num_votes = row[12]
        image_url = row [13]
        min_age = row[14]
        num_owned = row[16]
        weight = row[19]
        designer_id = designer_list[row[18]]
        category_id = category_list[row[17]]
        writer.writerow([game_id, name, rank, category_id, min_player, max_player, avg_time, min_time, max_time, avg_rating, num_votes, image_url, min_age, num_owned, designer_id, year_published, weight])
    
if __name__ == '__main__':
   dictionary_map()