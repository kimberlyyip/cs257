/*
 * boardgames.js
 * Sydney Nguyen, Kimberly Yip, Sophia Wang 
 * 
 */

window.onload = initialize;

function initialize() {
    loadGamesSelector();

    let element = document.getElementById('game_selector');
    if (element) {
        element.onchange = onGamesSelectionChanged;
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

function loadGamesSelector() {
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
            selectorBody += '<option value="' + game['rank'] + '">'
                                + game['name'] + ', ' + game['pub_year']
                                + '</option>\n';
        }

        let selector = document.getElementById('game_selector');
        if (selector) {
            selector.innerHTML = selectorBody;
        }
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}

function onGamesSelectionChanged() {


    let element = document.getElementById('game_selector');

    if (!element) {
        console.log('no element')
        return;
    }

    let gameRank = element.value; 
    let url = getAPIBaseURL() + '/games/' + gameRank;

    console.log('gameRank:' + gameRank)
    console.log('element:' + element)

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(gameinfo) {
        let tableBody = '';
        console.log('gameinfo length:' + gameinfo.length)
        for (let k = 0; k < gameinfo.length; k++) {
            let game = gameinfo[k];
            tableBody += '<tr>'
                            + '<td>' + game['rank'] + '</td>'
                            + '<td>' + game['name'] + '</td>'
                            + '</tr>\n';
        }

        // Put the table body we just built inside the table that's already on the page.
        let gameinfoTable = document.getElementById('gameinfo_table');
        if (gameinfoTable) {
            gameinfoTable.innerHTML = tableBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}


function submit_review(){
    var baseURL = getAPIBaseURL()
    var game_name = document.getElementById('game_game_name').innerHTML;
    var review_text = document.getElementById('input').value; 

    var url = baseURL + '/game/' + game_name + '/add/' + review_text;
    fetch (url, {
      method: 'POST',
      body: JSON.stringify({
        review_text: review_text,
        game_name: game_name,
      }),
      headers: {
        "Content-type" : "application/json; charset=UTF-8"
      }
    })
    .then (response => response.json())

  }

function all_reviews(){
    var baseURL = getAPIBaseURL()
    var game_name = document.getElementById('game_game_name').innerHTML;
    var url = baseURL + '/game/' + game_name + '/review';
    var reference = document.getElementById('reference');
    fetch(url,{ method: 'get'})
    .then((response) =>response.json())
    .then (jsondata => {
        var games_html = '';
        for( var i = 0; i < jsondata.length; i++){
            review = jsondata[i]
            games_html += '<h3>Reviews</h3> <h4>Review' + str(i+1) + '</h4>  <p>' + review + '</p>'
        }
   

   if (reference)
   {
       reference.innerHTML += games_html;
   }       
    })
    .catch(error => {
   console.log(error);
    });

}
