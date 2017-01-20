
function initMap() {
    var centerLatLng = new google.maps.LatLng(41.288575, 69.271459);
    var mapOptions = {
        center: centerLatLng, 
        zoom: 13               
    };
 
    var map = new google.maps.Map(document.getElementById("map"), mapOptions);

    var marker = new google.maps.Marker({
        position: latLng(41.297620,69.262444),
        map: map                          
    });
}

google.maps.event.addDomListener(window, "load", initMap);

