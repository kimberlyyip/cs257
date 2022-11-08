/*
Authors: Sydney Nguyen, Sophia Wang, Kimberly Yip
*/

CREATE TABLE game_user(
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

/*
CREATE TABLE board_game(
	id_board_game SERIAL,
	board_game_title text,
	designer_id integer,
	category_id integer,
	num_owned integer,
	avg_rating float,
	min_players integer,
	max_players integer,
	play_time integer,
	num_votes integer,
	age integer
);
*/

CREATE TABLE board_game(
	id_board_game SERIAL,
	board_game_title text,
	year_published integer,
	min_players integer,
	max_players integer,
	play_time integer,
	min_age integer,
	category_id integer,
	users_rated integer,
	rating_avg float,
	bgg_rank integer,
	owned_users integer,
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

