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
                              + "<input type='checkbox' name='" + category_name + "' class='custom-control-input'>"
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
                              + "<input type='checkbox' name='" + min_age_name + "'class='custom-control-input'>"
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


function get_all() {
    var url = getAPIBaseURL() + "/games/"
    var game_display = document.getElementById("games");
    console.log("games");
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

function submit_button(){
    search_string = document.getElementById('input').value
    alert(search_string)
    var url = getAPIBaseURL() + "/search_page/" + search_string
    var game_display = document.getElementById("games");

    console.log("games");
    fetch(url, {method: 'get'})
    .then((response) => response.json())
    .then(jsondata => {
        var games_html = '';
            for (var i = 0; i < 650; i++)
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
            for (var i = 0; i < jsondata.length; i++)
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

function onclick_get_min_age() {
    alert("submit");
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
        console.log(jsondata)
            for (var i = 0; i < jsondata.length; i++)
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

