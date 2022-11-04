/*
Authors: Sydney Nguyen, Sophia Wang, Kimberly Yip
*/



CREATE TABLE user(
	id SERIAL,
	username text,
	list_of_favorite_games_ids integer,
	password text
);

CREATE TABLE all_users(
	id_user SERIAL
);

CREATE TABLE review(
	id_user SERIAL,
	review text,
	id_board_game integer
);

CREATE TABLE board_game(
	id_board_game integer,
	Board_game_title text,
	Designer_id integer,
	category_id integer,
	weight integer, 
	num_owned integer,
	avg_rating float,
	min_players integer,
	max_players integer,
	min_time float,
	max_time float,
	avg_time float,
	num_votes integer,
	img text,
	age integer
);

CREATE TABLE all_board_games(
	id_board_game integer
);


CREATE TABLE designer(
	id_designer integer,
	designer_name text
);

CREATE TABLE categories(
	id_categories integer,
	categories_name text
);

