How to run:

1. Install PostgresSQL on your computer(via Homebrew or directly from website)

2. Create a database in Postgres that you would like to dump the anime data into. Call it something like "animeCentral" or whatever you'd like.

3. After cloning this repository, cd into "webapp" and run the following command: "psql -U yourUsername yourDatabaseName < data.sql". "yourUsername" is your Postgres username and "yourDatabaseName" is the name of the Postgres database that you just created.

4. Create a file called "config.py" within "webapp" as follows:
    
    user = "yourUsername"
    password = "yourPassword"
    database = "yourDatabaseName"
    
5. Run the following command: python3 app.py localhost 5000. Then, go to http://localhost:5000 to see the website!

_______________________________________________________________________________

AUTHORS: Kimberly Yip, Sophia Wang, Sydney Nguyen

DATA: Board Game database, consists of name, id, rating, rec age,ect. 

Copyright info: CC0: Public Domain
Link for DATA: https://www.kaggle.com/datasets/andrewmvd/board-games


FEATURES CURRENTLY WORKING:
- List all board games (default alphabetical)
- All board games have a designated cite 
- Sort board games by categories 
- Homepage is working with working links
- All links work 
- Search by string


FEATURES NOT YET WORKING:
- Anoyone is able to post an anyonymous review 
- Users can create an account
- Login page is functional 
- User is able to have favorite boardgames 
- User is able to view favorite boardgames
- User is able to make a review associated with their account 


Note: 
Users are unable to sort the data by two different types i.e categories and age can not currently be searched at the same time
