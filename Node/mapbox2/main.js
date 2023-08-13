
mapboxgl.accessToken = 'pk.eyJ1Ijoia2FzYW1pbiIsImEiOiJjbGt6ZXNsODgwMmZuM2VvNnQwazd4NGRiIn0.8Pd6lOXnhbpNeI5FVx1Z2A';

window.addEventListener('load', loadEvent);

function loadEvent(){
    const map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/streets-v11',
        center: [135, 35.6811673],
        zoom: 10
    });
}