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

CREATE TABLE games (
    rank integer NOT NULL,
    bgg_url text,
    game_id integer,
    name text,
    min_player integer,
    max_player integer,
    avg_time integer,
    min_time integer,
    max_time integer,
    pub_year integer,
    avg_rating double precision,
    geek_rating double precision,
    num_votes integer,
    image_url text,
    min_age integer,
    mechanic text,
    num_owned integer,
    category text,
    designer text,
    weight double precision
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

