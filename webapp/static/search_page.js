/*
 * static.js
 * Sydney Nguyen, Kimberly Yip, Sophia Wang 
 * 
 */

window.onload = initialize;

function initialize() {
    get_all();
    dropdownbtn();
    get_all_categories();
    get_all_min_age();
    get_search_string();
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

function get_all_categories() {
    var url = getAPIBaseURL() + "/games/sidebar/category"
    var game_display = document.getElementById("all_categories");
    console.log("all_categories");
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(jsondata => {
        var sidebar_html = '';
            for (var i = 0; i < jsondata.length - 1; i++)
            {
                categories = jsondata[i]
                category_name = categories['category']
                sidebar_html += "<div class='form-group'>"
                              + "<input type='checkbox' class='custom-control-input'>"
                              + "<span class='custom-control-indicator'></span>"
                              + "<span class='custom-control-description'>" + category_name + "</span>"
                              + "</div>"
            }
        console.log(sidebar_html)
        console.log(game_display)
        if (game_display)
        {
            game_display.innerHTML += sidebar_html;
        }       
    })
    .catch(error => {
        console.log(error);
    });
}

function get_all_min_age() {
    var url = getAPIBaseURL() + "/games/sidebar/min_age"
    var game_display = document.getElementById("all_min_age");
    console.log("all_min_age");
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(jsondata => {
        var sidebar_html = '';
            for (var i = 1; i < jsondata.length; i++)
            {
                min_age = jsondata[i]
                min_age_name = min_age['min_age']
                sidebar_html += "<div class='form-group'>"
                              + "<input type='checkbox' class='custom-control-input'>"
                              + "<span class='custom-control-indicator'></span>"
                              + "<span class='custom-control-description'>" + min_age_name + "</span>"
                              + "</div>"
            }
        console.log(sidebar_html)
        console.log(game_display)
        if (game_display)
        {
            game_display.innerHTML += sidebar_html;
        }       
    })
    .catch(error => {
        console.log(error);
    });
}

function get_search_string(){
    var url = getAPIBaseURL() + "/search_page/"
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
            game_display.innerHTML += games_html;
        }
    })
    .catch(error => {
        console.log(error);
    });

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
            game_display.innerHTML += games_html;
        }
    })
    .catch(error => {
        console.log(error);
    });
}

