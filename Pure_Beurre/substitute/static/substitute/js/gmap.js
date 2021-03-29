let map;


function initMap() {
  map = new google.maps.Map(document.getElementById("gmap-window"), {
    center: { lat: lat, lng: lng },
    //center: { lat: 45.7769226, lng: 4.8748023 },
    zoom: 11,
  });
    marker = new google.maps.Marker(
  {
      position: { lat: lat, lng: lng },
      //position: { lat: 45.7769226, lng: 4.8748023},
      map: map
  };
      second = new google.maps.Marker(
  {
      //position: { lat: lat, lng: lng },
      position: { lat: 45.6769226, lng: 4.8748023},
      map: map
  }
  );
}

