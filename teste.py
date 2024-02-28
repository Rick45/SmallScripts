import json

markers_string = """
new google.maps.Marker({
            position: {lat: 38.7663, lng: -9.30041},
            map: map,
            title: "387407",
            icon: 'https://appcdn.radaresdeportugal.pt/api_content/img_static_map/web/sign_max_p_speed_30.png'
        });
                new google.maps.Marker({
            position: {lat: 38.68553, lng: -9.31033},
            map: map,
            title: "387408",
            icon: 'https://appcdn.radaresdeportugal.pt/api_content/img_static_map/web/sign_max_p_speed_50.png'
        });
"""

markers_json = json.loads(markers_string)

print(markers_json)