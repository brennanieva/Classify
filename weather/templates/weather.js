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

  var x = new XMLHttpRequest();
  x.open("GET", url_day, true);
  x.onreadystatechange = function () {
    if (x.readyState == 4 && x.status == 200)
    {
      var doc = x.responseXML;
      // console.log(doc);
      var title_1 = doc.getElementsByTagName("temp_C")[0];
      console.log(title_1.childNodes[0]);
      $("#temp_C_value").html(title_1.childNodes[0]);
      var title_2 = doc.getElementsByTagName("temp_F")[0];
      console.log(title_2.childNodes[0]);
      $("#temp_F_value").html(title_2.childNodes[0]);
      var title_3 = doc.getElementsByTagName("date")[0];
      console.log(title_3.childNodes[0]);
      $("#date_value").html(title_3.childNodes[0]);
      var title_4 = doc.getElementsByTagName("maxtempF")[0];
      console.log(title_4.childNodes[0]);
      $("#maxtempF_value").html(title_4.childNodes[0]);
      var title_5 = doc.getElementsByTagName("maxtempC")[0];
      console.log(title_5.childNodes[0]);
      $("#maxtempC_value").html(title_5.childNodes[0]);
      var title_6 = doc.getElementsByTagName("mintempC")[0];
      console.log(title_6.childNodes[0]);
      $("#mintempC_value").html(title_6.childNodes[0]);
      var title_7 = doc.getElementsByTagName("mintempF")[0];
      console.log(title_7.childNodes[0]);
      $("#mintempF_value").html(title_7.childNodes[0]);
      var title_8 = doc.getElementsByTagName("chanceofrain")[0];
      console.log(title_8.childNodes[0]);
      $("#chanceofrain_value").html(title_8.childNodes[0]);
      var title_9 = doc.getElementsByTagName("chanceofovercast")[0];
      console.log(title_9.childNodes[0]);
      $("#chanceofovercast_value").html(title_9.childNodes[0]);
      var title_10 = doc.getElementsByTagName("chanceofsunshine")[0];
      console.log(title_10.childNodes[0]);
      $("#chanceofsunshine_value").html(title_10.childNodes[0]);
      var title_11 = doc.getElementsByTagName("chanceofsnow")[0];
      console.log(title_11.childNodes[0]);
      $("#chanceofsnow_value").html(title_11.childNodes[0]);
      var title_12 = doc.getElementsByTagName("chanceofthunder")[0];
      console.log(title_12.childNodes[0]);
      $("#chanceofthunder_value").html(title_12.childNodes[0]);

    }
};
x.send(null);


}

function init(){
  $("#click").click(onButtonClick);
}

// window.onLoad = init;
$(document).ready(init);
