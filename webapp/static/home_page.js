/*
 * home_page.js
 * Sydney Nguyen, Kimberly Yip, Sophia Wang 
 * 
 */

window.onload = initialize;

function initialize() {
    loadGamesSelector();

    let element = document.getElementById('game_display');
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

function get_category(category) {
    var url = getAPIBaseURL() + "/games/" + category;
    var game_display = document.getElementById("catgeory_" + category);
    console.log("category_" + category);
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(jsondata => {
        var games_html = '';
        for (var i = 0; i < 5; i++)
        {
            games = jsondata[i]
            type_item_class = category + '_item'
            type_genre_item = category + '_category_item'
            image_address = game['img_url']
            alt_text = game['name'] + " image"
            game_url = '/boardgame_site/' + game['name']
            animes_html += "<div id = 'img' >"
                        + "<div id = game_img>"
                        + "<img src='" + image_address + "' alt='" + alt_text + "'>"
                        + "<a href='" + game_url + "'>"
                        + "<p>" + game['name'] + "</p>"
                        + "</a>"
        }

        if (game_display)
        {
            game_display.innerHTML += games_html;
        }
    })
    .catch(error => {
        console.log(error);
    });
}

