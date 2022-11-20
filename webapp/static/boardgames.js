/*
 * static.js
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
    get_all();
    dropdownbtn();
    get_all_categories();
    get_all_min_age();
    get_all_pub_year();
    get_all_min_player();
    get_all_max_player();
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

function dropdownbtn(){
    /* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict */
  var dropdown = document.getElementsByClassName("dropdown-btn");
  var i;
  
  for (i = 0; i < dropdown.length; i++) {
    dropdown[i].addEventListener("click", function() {
      this.classList.toggle("active");
      var dropdownContent = this.nextElementSibling;
      if (dropdownContent.style.display === "block") {
        dropdownContent.style.display = "none";
      } else {
        dropdownContent.style.display = "block";
      }
    });
  }
}

/* Gets all categories that games can be sorted by
and puts them on the sidebar
*/
function get_all_categories() {
    var url = getAPIBaseURL() + "/games/sidebar/category"
    var game_display = document.getElementById("all_categories");
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(jsondata => {
        var sidebar_html = '';
            for (var i = 0; i < jsondata.length - 1; i++)
            {
                categories = jsondata[i]
                category_name = categories['category']
                sidebar_html += "<div class='form-group'>"
                              + "<input type='checkbox' name='" + category_name + "' class='custom-control-input'>"
                              + "<span class='custom-control-indicator'></span>"
                              + "<span class='custom-control-description'>" + category_name + "</span>"
                              + "</div>"
            }
        if (game_display)
        {
            game_display.innerHTML += sidebar_html;
        }       
    })
    .catch(error => {
        console.log(error);
    });
}

//Gets all the options for min age and puts them into dropdown
function get_all_min_age() {
    var url = getAPIBaseURL() + "/games/sidebar/min_age"
    var game_display = document.getElementById("all_min_age");
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(jsondata => {
        var sidebar_html = '';
            for (var i = 1; i < jsondata.length; i++)
            {
                min_age = jsondata[i]
                min_age_name = min_age['min_age']
                sidebar_html += "<div class='form-group'>"
                              + "<input type='checkbox' name='" + min_age_name + "'class='custom-control-input'>"
                              + "<span class='custom-control-indicator'></span>"
                              + "<span class='custom-control-description'>" + min_age_name + "</span>"
                              + "</div>"
            }
        if (game_display)
        {
            game_display.innerHTML += sidebar_html;
        }       
    })
    .catch(error => {
        console.log(error);
    });
}

//Gets all options for year published and puts them into dropdown
function get_all_pub_year() {
    var url = getAPIBaseURL() + "/games/sidebar/pub_year"
    var game_display = document.getElementById("all_pub_year");
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(jsondata => {
        var sidebar_html = '';
            for (var i = 1; i < jsondata.length; i++)
            {
                pub_year = jsondata[i]
                pub_year_name = pub_year['pub_year']
                sidebar_html += "<div class='form-group'>"
                              + "<input type='checkbox' name='" + pub_year_name + "'class='custom-control-input'>"
                              + "<span class='custom-control-indicator'></span>"
                              + "<span class='custom-control-description'>" + pub_year_name + "</span>"
                              + "</div>"
            }
        if (game_display)
        {
            game_display.innerHTML += sidebar_html;
        }       
    })
    .catch(error => {
        console.log(error);
    });
}

//Gets all options for min player and puts them into dropdown
function get_all_min_player() {
    var url = getAPIBaseURL() + "/games/sidebar/min_player"
    var game_display = document.getElementById("all_min_player");
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(jsondata => {
        var sidebar_html = '';
            for (var i = 1; i < jsondata.length; i++)
            {
                min_player = jsondata[i]
                min_player_name = min_player['min_player']
                sidebar_html += "<div class='form-group'>"
                              + "<input type='checkbox' name='" + min_player_name + "'class='custom-control-input'>"
                              + "<span class='custom-control-indicator'></span>"
                              + "<span class='custom-control-description'>" + min_player_name + "</span>"
                              + "</div>"
            }
        if (game_display)
        {
            game_display.innerHTML += sidebar_html;
        }       
    })
    .catch(error => {
        console.log(error);
    });
}

//Gets all options for max player and puts them into dropdown
function get_all_max_player() {
    var url = getAPIBaseURL() + "/games/sidebar/max_player"
    var game_display = document.getElementById("all_max_player");
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(jsondata => {
        var sidebar_html = '';
            for (var i = 1; i < jsondata.length; i++)
            {
                max_player = jsondata[i]
                max_player_name = max_player['max_player']
                sidebar_html += "<div class='form-group'>"
                              + "<input type='checkbox' name='" + max_player_name + "'class='custom-control-input'>"
                              + "<span class='custom-control-indicator'></span>"
                              + "<span class='custom-control-description'>" + max_player_name + "</span>"
                              + "</div>"
            }
        if (game_display)
        {
            game_display.innerHTML += sidebar_html;
        }       
    })
    .catch(error => {
        console.log(error);
    });
}

//Gets all results of filter and displays them on search page
function get_all() {
    var url = getAPIBaseURL() + "/games/"
    var game_display = document.getElementById("games");
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(jsondata => {
        var games_html = '';
        if (jsondata.length > 500){
            output = 500
        }
        else {
            output = jsondata.length
        }
            for (var i = 0; i < output; i++)
            {
                if (i % 4 == 0) {
                    games_html += "<div id = 'img' >"
                }
                games = jsondata[i]
                image_address = games['image_url']
                alt_text = games['name'] + " image"
                game_url = '/game/' + games['name']
                games_html += "<div id = game_img>"
                            + "<img src='" + image_address + "' alt='" + alt_text + "'>"
                            + "<a href='" + game_url + "'>"
                            + "<p>" + games['name'] + "</p>"
                            + "</a>"
                            + "</div>"
                if ((i + 1) % 4 == 0) {
                    games_html += "</div>"
                }
            }          
        if (game_display)
        {
            game_display.innerHTML = games_html;
        }
    })
    .catch(error => {
        console.log(error);
    });
}

//changes which games show up on clicking submit
function submit_button(){
    search_string = document.getElementById('input').value
    var url = getAPIBaseURL() + "/search_page/" + search_string
    var game_display = document.getElementById("games");
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(jsondata => {
        var games_html = '';
        if (jsondata.length > 500){
            output = 500
        }
        else {
            output = jsondata.length
        }
            for (var i = 0; i < output; i++)
            {
                if (i % 4 == 0) {
                    games_html += "<div id = 'img' >"
                }
                games = jsondata[i]
                image_address = games['image_url']
                alt_text = games['name'] + " image"
                game_url = '/game/' + games['name']
                games_html += "<div id = game_img>"
                            + "<img src='" + image_address + "' alt='" + alt_text + "'>"
                            + "<a href='" + game_url + "'>"
                            + "<p>" + games['name'] + "</p>"
                            + "</a>"
                            + "</div>"
                if ((i + 1) % 4 == 0) {
                    games_html += "</div>"
                }
            }          
        if (game_display)
        {
            game_display.innerHTML = games_html;
        }
    })

    .catch(error => {
        console.log(error);
    });
}


function get_category(category) {
    var url = getAPIBaseURL() + "/games/category/" + category
    var game_display = document.getElementById("category_" + category);
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(jsondata => {
        var games_html = "<div id = 'img' >";
        for (var i = 0; i < 5; i++)
        {
            games = jsondata[i]
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
        if (game_display)
        {
            game_display.innerHTML += games_html;
        }
    })
    .catch(error => {
        console.log(error);
    });
}

function onclick_get_category() {
    var url = getAPIBaseURL() + "/games/category/"
    var boxes = document.querySelectorAll(".custom-control-input");
    for (var j = 0; j < boxes.length; j++) {
        if (boxes[j].checked){
            url += boxes[j].name
            if (j < boxes.length - 1) {
                url += "_"
            } 
        }
    }
    var game_display = document.getElementById("games");
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(jsondata => {
        var games_html = '';
        if (jsondata.length > 500){
            output = 500
        }
        else {
            output = jsondata.length
        }
            for (var i = 0; i < output; i++)
            {
                if (i % 4 == 0) {
                    games_html += "<div id = 'img'>"
                }
                games = jsondata[i]
                image_address = games['image_url']
                alt_text = games['name'] + " image"
                game_url = '/game/' + games['name']
                games_html += "<div id = game_img>"
                            + "<img src='" + image_address + "' alt='" + alt_text + "'>"
                            + "<a href='" + game_url + "'>"
                            + "<p>" + games['name'] + "</p>"
                            + "</a>"
                            + "</div>"
                if ((i + 1) % 4 == 0) {
                    games_html += "</div>"
                }
            }          
        if (game_display)
        {
            game_display.innerHTML = games_html;
        }
    })
    .catch(error => {
        console.log(error);
    });
}

//gets and displays games based on min_age filter
function onclick_get_min_age() {
    var url = getAPIBaseURL() + "/games/min_age/"
    var boxes = document.querySelectorAll(".custom-control-input");
    for (var j = 0; j < boxes.length; j++) {
        if (boxes[j].checked){
            url += boxes[j].name
            if (j < boxes.length - 1) {
                url += "_"
            } 
        }
    }
    var game_display = document.getElementById("games");
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(jsondata => {
        var games_html = '';
        if (jsondata.length > 500){
            output = 500
        }
        else {
            output = jsondata.length
        }
            for (var i = 0; i < output; i++)
            {
                if (i % 4 == 0) {
                    games_html += "<div id = 'img'>"
                }
                games = jsondata[i]
                image_address = games['image_url']
                alt_text = games['name'] + " image"
                game_url = '/game/' + games['name']
                games_html += "<div id = game_img>"
                            + "<img src='" + image_address + "' alt='" + alt_text + "'>"
                            + "<a href='" + game_url + "'>"
                            + "<p>" + games['name'] + "</p>"
                            + "</a>"
                            + "</div>"
                if ((i + 1) % 4 == 0) {
                    games_html += "</div>"
                }
            }          
        if (game_display)
        {
            game_display.innerHTML = games_html;
        }
    })
    .catch(error => {
        console.log(error);
    });
}

//gets and displays games based on pub_year filter
function onclick_get_pub_year() {
    var url = getAPIBaseURL() + "/games/pub_year/"
    var boxes = document.querySelectorAll(".custom-control-input");
    for (var j = 0; j < boxes.length; j++) {
        if (boxes[j].checked){
            url += boxes[j].name
            if (j < boxes.length - 1) {
                url += "_"
            } 
        }
    }
    var game_display = document.getElementById("games");
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(jsondata => {
        var games_html = '';
        if (jsondata.length > 500){
            output = 500
        }
        else {
            output = jsondata.length
        }
            for (var i = 0; i < output; i++)
            {
                if (i % 4 == 0) {
                    games_html += "<div id = 'img'>"
                }
                games = jsondata[i]
                image_address = games['image_url']
                alt_text = games['name'] + " image"
                game_url = '/game/' + games['name']
                games_html += "<div id = game_img>"
                            + "<img src='" + image_address + "' alt='" + alt_text + "'>"
                            + "<a href='" + game_url + "'>"
                            + "<p>" + games['name'] + "</p>"
                            + "</a>"
                            + "</div>"
                if ((i + 1) % 4 == 0) {
                    games_html += "</div>"
                }
            }          
        if (game_display)
        {
            game_display.innerHTML = games_html;
        }
    })
    .catch(error => {
        console.log(error);
    });
}

//gets and displays games based on min_player filter
function onclick_get_min_player() {
    var url = getAPIBaseURL() + "/games/min_player/"
    var boxes = document.querySelectorAll(".custom-control-input");
    for (var j = 0; j < boxes.length; j++) {
        if (boxes[j].checked){
            url += boxes[j].name
            if (j < boxes.length - 1) {
                url += "_"
            } 
        }
    }
    var game_display = document.getElementById("games");
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(jsondata => {
        var games_html = '';
        if (jsondata.length > 500){
            output = 500
        }
        else {
            output = jsondata.length
        }
            for (var i = 0; i < output; i++)
            {
                if (i % 4 == 0) {
                    games_html += "<div id = 'img'>"
                }
                games = jsondata[i]
                image_address = games['image_url']
                alt_text = games['name'] + " image"
                game_url = '/game/' + games['name']
                games_html += "<div id = game_img>"
                            + "<img src='" + image_address + "' alt='" + alt_text + "'>"
                            + "<a href='" + game_url + "'>"
                            + "<p>" + games['name'] + "</p>"
                            + "</a>"
                            + "</div>"
                if ((i + 1) % 4 == 0) {
                    games_html += "</div>"
                }
            }          
        if (game_display)
        {
            game_display.innerHTML = games_html;
        }
    })
    .catch(error => {
        console.log(error);
    });
}

//gets and displays games based on max_player filter
function onclick_get_max_player() {
    var url = getAPIBaseURL() + "/games/max_player/"
    var boxes = document.querySelectorAll(".custom-control-input");
    for (var j = 0; j < boxes.length; j++) {
        if (boxes[j].checked){
            url += boxes[j].name
            if (j < boxes.length - 1) {
                url += "_"
            } 
        }
    }
    var game_display = document.getElementById("games");
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(jsondata => {
        var games_html = '';
        if (jsondata.length > 500){
            output = 500
        }
        else {
            output = jsondata.length
        }
            for (var i = 0; i < output; i++)
            {
                if (i % 4 == 0) {
                    games_html += "<div id = 'img'>"
                }
                games = jsondata[i]
                image_address = games['image_url']
                alt_text = games['name'] + " image"
                game_url = '/game/' + games['name']
                games_html += "<div id = game_img>"
                            + "<img src='" + image_address + "' alt='" + alt_text + "'>"
                            + "<a href='" + game_url + "'>"
                            + "<p>" + games['name'] + "</p>"
                            + "</a>"
                            + "</div>"
                if ((i + 1) % 4 == 0) {
                    games_html += "</div>"
                }
            }          
        if (game_display)
        {
            game_display.innerHTML = games_html;
        }
    })
    .catch(error => {
        console.log(error);
    });
}

function onclick_get_alphabetical(alpha){
    var url = getAPIBaseURL() + "/game/alphabetical/" + alpha
    var game_display = document.getElementById("games");
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(jsondata => {
        var games_html = '';
        if (jsondata.length > 500){
            output = 500
        }
        else {
            output = jsondata.length
        }
            for (var i = 0; i < output; i++)
            {
                if (i % 4 == 0) {
                    games_html += "<div id = 'img'>"
                }
                games = jsondata[i]
                image_address = games['image_url']
                alt_text = games['name'] + " image"
                game_url = '/game/' + games['name']
                games_html += "<div id = game_img>"
                            + "<img src='" + image_address + "' alt='" + alt_text + "'>"
                            + "<a href='" + game_url + "'>"
                            + "<p>" + games['name'] + "</p>"
                            + "</a>"
                            + "</div>"
                if ((i + 1) % 4 == 0) {
                    games_html += "</div>"
                }
            }          
        if (game_display)
        {
            game_display.innerHTML = games_html;
        }
    })
    .catch(error => {
        console.log(error);
    });

}