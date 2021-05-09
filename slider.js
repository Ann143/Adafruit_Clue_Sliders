var broker = 'wss://mqtt.eclipseprojects.io:443/mqtt'; //this is for the broker
var client = mqtt.connect(broker); //initializing variable client which holds the value of broker
var status_header = document.getElementById('status-header') //intializing variable status_header that holds the element id of "status-header"

//this check if connected to the broker
client.on('connect', function() {
    status_header.innerHTML = 'Connected to ' + broker; //display the broker if  connected successfully.
    console.log('Connected to ' + broker) //check if now connected to the broker
})

//Initializing variable sliders that holds the class name of "slider"
var sliders = document.getElementsByClassName("slider");

//initializing variable that handling two events
const events = {
    "mouseup": function(event) { //mouseup event : creating a  function that have a parameter of event 
        console.log(event.target.name, event.target.value); //console log or check 
        client.publish(`clueSlider/${event.target.name}`, event.target.value);
    },
    "input": function(event) { //input element
        document.getElementById(event.target.name).innerHTML = event.target.value;
    }
}

//loop all the sliders   
for (let slider of sliders) {
    for (let key in events) { //loop the events variable to loop 
        slider.addEventListener(key, events[key]);
    }
}