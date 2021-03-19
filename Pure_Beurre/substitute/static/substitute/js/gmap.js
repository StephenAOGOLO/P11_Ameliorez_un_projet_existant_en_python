let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("gmap-window"), {
    center: { lat: 45.764043, lng: 4.835659 },
    zoom: 11,
  });
    marker = new google.maps.Marker(
  {
      position: { lat: 45.764043, lng: 4.835659},
      map: map
  });
}
/*
//form_sheet.addEventListener("submit", function(event)
//{
//    event.preventDefault();
//    postFormData("/catcher", new FormData(form_sheet))
//    .then(response =>{
//        console.log(response["place"]["lat"])+console.log(response["place"]["lng"]);
//         othermap = new google.maps.Map(document.getElementById("gmap-window"),
//                    {
//                        center: { lat: response["place"]["lat"] , lng: response["place"]["lng"] },
//                        zoom: response["place"]["zoom"]
//                    });
//                    marker = new google.maps.Marker(
//                    {
//                        position: { lat: response["place"]["lat"] , lng: response["place"]["lng"] },
//                        map: othermap
//                    });
//    })
//})
*/
