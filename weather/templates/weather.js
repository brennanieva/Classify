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


  // $.get(url_day, null,processResponse);
  // $.get(url_week, null,processResponse);

  var x = new XMLHttpRequest();
  x.open("GET", url_day, true);
  x.onreadystatechange = function () {
    if (x.readyState == 4 && x.status == 200)
    {
      var doc = x.responseXML;
      // console.log(doc);
      var title = doc.getElementsByTagName("temp_C")[0];
      console.log(title.childNodes[0]);
      var title = doc.getElementsByTagName("temp_F")[0];
      console.log(title.childNodes[0]);
      var title = doc.getElementsByTagName("date")[0];
      console.log(title.childNodes[0]);
      var title = doc.getElementsByTagName("maxtempF")[0];
      console.log(title.childNodes[0]);
      var title = doc.getElementsByTagName("maxtempC")[0];
      console.log(title.childNodes[0]);
      var title = doc.getElementsByTagName("mintempC")[0];
      console.log(title.childNodes[0]);
      var title = doc.getElementsByTagName("mintempF")[0];
      console.log(title.childNodes[0]);
      var title = doc.getElementsByTagName("chanceofrain")[0];
      console.log(title.childNodes[0]);
      var title = doc.getElementsByTagName("chanceofovercast")[0];
      console.log(title.childNodes[0]);
      var title = doc.getElementsByTagName("chanceofsunshine")[0];
      console.log(title.childNodes[0]);
      var title = doc.getElementsByTagName("chanceofsnow")[0];
      console.log(title.childNodes[0]);
      var title = doc.getElementsByTagName("chanceofthunder")[0];
      console.log(title.childNodes[0]);
    }
};
x.send(null);




  // let weatherKey="fc1a305754d1452dbe1175203192307";

  // let searchTerm = $("#searchterm").val();
  // console.log(searchTerm);

  let url_week = "http://api.worldweatheronline.com/premium/v1/weather.ashx?key=" + weatherKey + "&q=" + searchTerm + "&num_of_days=7&tp=3&format=xml"


  console.log(url_week);

  var x = new XMLHttpRequest();
  x.open("GET", url_week, true);
  x.onreadystatechange = function () {
    if (x.readyState == 4 && x.status == 200)
    {
      var doc = x.responseXML;
      // console.log(doc);
      var title = doc.getElementsByTagName("temp_C")[0];
      console.log(title.childNodes[0]);
      var title = doc.getElementsByTagName("temp_F")[0];
      console.log(title.childNodes[0]);
      var title = doc.getElementsByTagName("date")[0];
      console.log(title.childNodes[0]);
      var title = doc.getElementsByTagName("maxtempF")[0];
      console.log(title.childNodes[0]);
      var title = doc.getElementsByTagName("maxtempC")[0];
      console.log(title.childNodes[0]);
      var title = doc.getElementsByTagName("mintempC")[0];
      console.log(title.childNodes[0]);
      var title = doc.getElementsByTagName("mintempF")[0];
      console.log(title.childNodes[0]);
      var title = doc.getElementsByTagName("chanceofrain")[0];
      console.log(title.childNodes[0]);
      var title = doc.getElementsByTagName("chanceofovercast")[0];
      console.log(title.childNodes[0]);
      var title = doc.getElementsByTagName("chanceofsunshine")[0];
      console.log(title.childNodes[0]);
      var title = doc.getElementsByTagName("chanceofsnow")[0];
      console.log(title.childNodes[0]);
      var title = doc.getElementsByTagName("chanceofthunder")[0];
      console.log(title.childNodes[0]);

    }
  };
  x.send(null);

}

function init(){
  $("#click").click(onButtonClick);
}

// window.onLoad = init;
$(document).ready(init);
