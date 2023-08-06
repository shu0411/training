import mapboxgl from "mapbox-gl";

mapboxgl.accessToken = 'pk.eyJ1Ijoia2FzYW1pbiIsImEiOiJjbGt6ZXNsODgwMmZuM2VvNnQwazd4NGRiIn0.8Pd6lOXnhbpNeI5FVx1Z2A';

window.addEventListener('load', () => {
    const map: mapboxgl.Map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/streets-v11',
        center: [139.7670516, 39],
        zoom: 5
    });
});