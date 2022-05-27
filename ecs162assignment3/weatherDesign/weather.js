"strict mode";

// Do a CORS request to get Davis weather hourly forecast

// Create the XHR object.
function createCORSRequest(method, url) {
  let xhr = new XMLHttpRequest();
  xhr.open(method, url, true);  // call its open method
  return xhr;
}

// Make the actual CORS request.
function makeCorsRequest() {

    let url = "https://api.openweathermap.org/data/2.5/weather?lat=37.035065&lon=-95.651588&appid=a24ab317f7892ce504859e3fec615749"
  // let url = "pro.openweathermap.org/data/2.5/forecast/hourly?lat={38.5449}&lon={121.7405}&appid={a24ab317f7892ce504859e3fec615749}"

  let xhr = createCORSRequest('GET', url);

  // checking if browser does CORS
  if (!xhr) {
    alert('CORS not supported');
    return;
  }

  // Load some functions into response handlers.
  xhr.onload = function() {
      let responseStr = xhr.responseText;  // get the JSON string 
      let object = JSON.parse(responseStr);  // turn it into an object
      console.log(JSON.stringify(object, undefined, 2));  // print it out as a string, nicely formatted
  };

  xhr.onerror = function() {
    alert('Woops, there was an error making the request.');
  };

  // Actually send request to server
  xhr.send();
}

// run this code to make request when this script file gets executed 
makeCorsRequest();
