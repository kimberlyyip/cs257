/*
 * boardgames.js
 * Sydney Nguyen, Kimberly Yip, Sophia Wang 
 * 
 */

window.onload = initialize;

function initialize() {
    loadAuthorsSelector();

    let element = document.getElementById('author_selector');
    if (element) {
        element.onchange = onAuthorsSelectionChanged;
    }
}

// Returns the base URL of the API, onto which endpoint
// components can be appended.
function getAPIBaseURL() {
    let baseURL = window.location.protocol
                    + '//' + window.location.hostname
                    + ':' + window.location.port
                    + '/api';
    return baseURL;
}

function loadAuthorsSelector() {
    let url = getAPIBaseURL() + '/games/';

    // Send the request to the books API /authors/ endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from a JSON string into
    // a Javascript object (in this case, a list of author dictionaries).
    .then((response) => response.json())

    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    .then(function(games) {
        // Add the <option> elements to the <select> element
        let selectorBody = '';
        for (let k = 0; k < games.length; k++) {
            let game = games[k];
            selectorBody += '<option value="' + game['name'] + '">'
                                + game['name'] + ', ' + game['pub_year']
                                + '</option>\n';
        }


        // game = {'rank':row[0],
        // 'bgg_url':row[1],
        // 'game_id':row[2],
        // 'name':row[3],
        // 'min_player':row[4],
        // 'max_player':row[5],
        // 'avg_time':row[6],
        // 'min_time':row[7],
        // 'max_time':row[8],
        // 'pub_year':row[9],
        // 'avg_rating':row[10],
        // 'geek_rating':row[11],
        // 'num_votes':row[12]
        // 'image_url':row[13]
        // 'min_age':row[14]
        // 'mechanic':row[15]
        // 'num_owned':row[16]
        // 'category':row[17]
        // 'designer':row[18]
        // 'weight':row[19]}



        let selector = document.getElementById('author_selector');
        if (selector) {
            selector.innerHTML = selectorBody;
        }
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}

function onAuthorsSelectionChanged() {
    let authorID = this.value; 
    let url = getAPIBaseURL() + '/books/author/' + authorID;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(books) {
        let tableBody = '';
        for (let k = 0; k < books.length; k++) {
            let book = books[k];
            tableBody += '<tr>'
                            + '<td>' + book['title'] + '</td>'
                            + '<td>' + book['publication_year'] + '</td>'
                            + '</tr>\n';
        }

        // Put the table body we just built inside the table that's already on the page.
        let booksTable = document.getElementById('books_table');
        if (booksTable) {
            booksTable.innerHTML = tableBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}

