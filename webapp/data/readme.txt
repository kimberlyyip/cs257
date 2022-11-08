Setting up the board games database
CS257 Software Design
Fall 2020
Sophia Wang, Kimberly Yip, Sydney Nguyen
How to set up our board games data so you can run our sample web application.

1. Creating the database.

    $ psql -U YOUR_PSQL_USER_NAME postgres
    postgres=# CREATE DATABASE boardgames;

or just

    $ createdb boardgames

(where $ is a Unix prompt, and postgres=# is a psql prompt).

2. Populating the database.

    $ psql -U YOUR_PSQL_USER_NAME boardgames < database-schema.sql

