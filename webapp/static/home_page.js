/*
 * home_page.js
 * Sydney Nguyen, Kimberly Yip, Sophia Wang 
 * 
 */

window.onload = initialize;

function initialize() {
    get_category('Card Game');
    get_category('Wargame');
    get_category('Fantasy');
    get_category('Economic');
    get_category('Fighting');
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

//Gets top 5 games of each category from the endpoint and 
//then turns it into a list of game dictionaries, then puts it
//into the html
function get_category(category) {
    var url = getAPIBaseURL() + "/games/category/" + category
    var game_display = document.getElementById("category_" + category);
    console.log("category_" + category);
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(jsondata => {
        var games_html = "<div id = 'img' >";
        for (var i = 0; i < 5; i++)
        {
            games = jsondata[i]
            console.log(jsondata)
            type_item_class = category + '_item'
            type_genre_item = category + '_category_item'
            image_address = games['image_url']
            alt_text = games['name'] + " image"
            game_url = '/game/' + games['name']
            games_html +="<div id = game_img>"
                        + "<img src='" + image_address + "' alt='" + alt_text + "'>"
                        + "<a href='" + game_url + "'>"
                        + "<p>" + games['name'] + "</p>"
                        + "</a>"
                        + "</div>"
        }
        games.html = "</div>"
        console.log(game_display)
        if (game_display)
        {
            game_display.innerHTML += games_html;
        }
    })
    .catch(error => {
        console.log(error);
    });
}

