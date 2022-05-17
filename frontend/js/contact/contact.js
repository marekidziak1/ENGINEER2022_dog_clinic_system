$(document).ready(function(){
    var map = L.map('map').setView([52.237049, 21.017532], 12);
    var OpenStreetMap_Mapnik = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    var clinicMarker = new L.marker([52.237049, 21.017532]).addTo(map);
});
