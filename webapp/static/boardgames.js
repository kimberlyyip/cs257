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
            games_html += '<h3>Reviews</h3> <h4>Review' + str(i+1) + ': </h4> <p>' + review + '</p>'
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
