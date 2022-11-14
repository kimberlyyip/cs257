/*
 * static.js
 * Sydney Nguyen, Kimberly Yip, Sophia Wang 
 * 
 */

window.onload = initialize;

function initialize() {
    get_all();
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

function get_all() {
    var url = getAPIBaseURL() + "/games/"
    var game_display = document.getElementById("all_games");
    console.log("all_games");
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(jsondata => {
        var games_html = '';
            for (var i = 0; i < 625; i++)
            {
                if (i % 4 == 0) {
                    games_html += "<div id = 'img' >"
                }
                games = jsondata[i]
                console.log(jsondata)
                image_address = games['image_url']
                alt_text = games['name'] + " image"
                game_url = '/boardgame_site/' + games['name']
                games_html += "<div id = game_img>"
                            + "<img src='" + image_address + "' alt='" + alt_text + "'>"
                            + "<a href='" + game_url + "'>"
                            + "<p>" + games['name'] + "</p>"
                            + "</a>"
                            + "</div>"
                if ((i + 1) % 4 == 0) {
                    console.log("end")
                    games_html += "</div>"
                }
            }          
            console.log(games_html)
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

