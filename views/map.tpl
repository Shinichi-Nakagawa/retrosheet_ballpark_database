<!DOCTYPE html>
<html>
  <head>
    <title>Baseball Park Map</title>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <style>
      html, body, #map-canvas {
        height: 100%;
        margin: 0px;
        padding: 0px
      }
    </style>
    <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&key={{ map_key }}&sensor={{ sensor }}"></script>
    <script>
        var map;
        function attachMessage(marker, msg) {
            google.maps.event.addListener(
                    marker, 'click',
                    function(event) {
                        new google.maps.InfoWindow(
                                {
                                    content: msg
                                }
                        ).open(marker.getMap(), marker);
                    }
            );
        }
        function initialize() {
            var parks = new Array();
        % for i, park in enumerate(parks):
            parks.push(
                    {
                        position: new google.maps.LatLng({{ park.lat }}, {{ park.lon }}),
                        content: '{{ park.name }}({{ park.parkid }})'
                    }
            );
        % end
            var mapOptions = {
                zoom: 3,
                center: new google.maps.LatLng({{ center_lat }}, {{ center_lon }})
            };
            map = new google.maps.Map(
                    document.getElementById('map-canvas'),mapOptions
            );
            for (i = 0; i < parks.length; i++) {
                var myMarker = new google.maps.Marker(
                        {
                            position: parks[i].position,
                            map: map
                        }
                );
                attachMessage(myMarker, parks[i].content);
            }
        }
        google.maps.event.addDomListener(window, 'load', initialize);
    </script>
  </head>
  <body>
    <div id="map-canvas"></div>
  </body>
</html>