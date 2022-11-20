AUTHORS: Kimberly Yip, Sophia Wang, Sydney Nguyen

DATA: Board Game database, consists of name, id, rating, recommended minimum age,ect. 

Copyright info: CC0: Public Domain
Link for DATA: https://www.kaggle.com/datasets/andrewmvd/board-games


STATUS:
- List all board games (default alphabetical)
- All board games have a designated site 
- Sort board games by categories 
- Homepage is working with working links
- All links work 
- Search by string in board game name
- Filter by one board game attribute (genre, year published, min players, etc)
- Anoyone is able to post an anonymous review 

_______________________________________________________________________________

Note: 
Users are unable to sort the data by two different types i.e categories and age can not currently be searched at the same time.
We dropped the idea of having a user with username and password due to time constraints.
Since the data set is so large users are able to sort by alphabet to access all the data.
Note to see the review once a user has posted the page needs to be reloaded!

How to run:

1. Install PostgresSQL on your computer(via Homebrew or directly from website)

2. Create a database in Postgres that you would like to dump the anime data into. Call it something like "boardgames" or whatever you'd like.

3. After cloning this repository, cd into "webapp/data" and run the following command: "psql -U yourUsername yourDatabaseName < data.sql". "yourUsername" is your Postgres username and "yourDatabaseName" is the name of the Postgres database that you just created.

4. Create a file called "config.py" within "webapp" as follows:
    
    user = "yourUsername"
    password = "yourPassword"
    database = "yourDatabaseName"
    port = "yourPort" (usually 5432, but sometimes 5433)
    
5. Run the following command: python3 app.py localhost 5000. Then, go to http://localhost:5000 to see the website!


