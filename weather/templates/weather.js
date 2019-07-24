function processResponse(response){
  console.log(response);

  let json = response;
  // let imageUrl = json["data"][0]["images"]["original"]["url"];
  // console.log(imageUrl);

$("#results").append('<img src="' + '"/>')
  //
  //
}

function onButtonClick(){
  console.log("zip code has been recorded");

  let weatherKey="fc1a305754d1452dbe1175203192307";

  let searchTerm = $("#searchterm").val();
  console.log(searchTerm);

  let url_day = "http://api.worldweatheronline.com/premium/v1/weather.ashx?key=" + weatherKey + "&q=" + searchTerm + "&num_of_days=1&tp=3&format=xml"

  console.log(url_day);

  let url_week = "http://api.worldweatheronline.com/premium/v1/weather.ashx?key=" + weatherKey + "&q=" + searchTerm + "&num_of_days=7&tp=3&format=xml"

  console.log(url_week);

  $.get(url_day, null,processResponse);
  $.get(url_week, null,processResponse);


}

function init(){
  $("#click").click(onButtonClick);
}

// window.onLoad = init;
$(document).ready(init);
