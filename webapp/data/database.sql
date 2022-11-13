CREATE TABLE categories(
    id integer,
    category text
);

CREATE TABLE designer(
    id integer, 
    designer text
);

CREATE TABLE games (
    game_id integer,
    name text,
    rank integer,
    min_player integer,
    max_player integer,
    avg_time integer,
    min_time integer,
    max_time integer,
    avg_rating float,
    num_votes integer,
    image_url text,
    min_age integer,
    num_owned integer,
    designer_id integer,
    pub_year integer,
    complexity float
);

CREATE TABLE game_categories(
    game_id integer, 
    category_id integer
);

\copy categories from 'categories.csv' DELIMITER ',' CSV NULL as 'NULL'

\copy designer FROM 'designer.csv' DELIMITER ',' CSV NULL AS 'NULL'

\copy games FROM 'games.csv' DELIMITER ',' CSV NUll AS 'NULL'

\copy game_categories FROM 'game_categories.csv' DELIMITER ',' CSV NULL AS 'NULL'