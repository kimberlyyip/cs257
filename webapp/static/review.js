window.onload = initialize;

function initialize() {
  var submit_review_button = document.getElementById('review'); 
  submit_review_button.addEventListener('click', submit_review);
}

function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}

function submit_review(){
  var baseURL = getAPIBaseURL()
  var api_url = baseURL + '/add/review';
  var review_textarea = document.getElementById('write_a_review'); 
  var review_text = review_textarea.value;
  fetch (api_url, {
    method: 'POST',
    body: JSON.stringify({
      review_text: review_text,
      anime_name: anime_name
    }),
    headers: {
      "Content-type" : "application/json; charset=UTF-8"
    }
  })
  .then (response => response.json())
  .then (jsonData => {
       window.location.reload(true);
  })
}