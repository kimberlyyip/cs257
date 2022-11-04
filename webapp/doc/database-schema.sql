/*
Authors: Sydney Nguyen, Sophia Wang, Kimberly Yip
*/



CREATE TABLE user(
	Id_user,
	username,
	list of favorite game ids,
password 
);

CREATE TABLE all_users(
	id_user
);

CREATE TABLE review(
	id_user,
	text
);

CREATE TABLE board_game(
	id board_game,
	Board_game_title,
	Designer_id,
	category_id,
	weight, 
	owned,
  avg_rating,
  min_player,
  Max_player,
  min_time,
  Max_time,
  Avg_time,
  Num_votes,
  Img,
  Age

);

CREATE TABLE all_board_games(
	id board_game
);


CREATE TABLE designer(
	id designer,
	designer_name
);

CREATE TABLE categories(
	id categories,
	categories_name

);

