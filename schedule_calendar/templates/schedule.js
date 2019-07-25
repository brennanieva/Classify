function processResponse(response){
  console.log(response);

  let json = response;
}

function onButtonClick(){
  console.log("blah");


  let scheduleKey="2469d3563444d6fbd6ecd75255587c3e46ed187b";

  let searchTerm = $("#searchterm").val();
  console.log(searchTerm);

  let url = "https://calendarific.com/api/v2/holidays?&api_key=" + scheduleKey + "&country=" + searchTerm + "&year=2019"

  console.log(url);

}

function init(){
  $("#click").click(onButtonClick);
}

// window.onLoad = init;
$(document).ready(init);
