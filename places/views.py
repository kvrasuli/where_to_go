from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Place
import pprint
import copy


def index(request):
    places = Place.objects.all()
    places_geojson = {"type": "FeatureCollection", "features": []}
    place_feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [None, None]
        },
        "properties": {
            "title": None,
            "placeId": "moscow_legends",
            "detailsUrl": "/static/places/moscow_legends.json",
        }
    }
    for place in places:
        temp_feature = copy.deepcopy(place_feature)
        temp_feature['geometry']['coordinates'][0] = place.lng
        temp_feature['geometry']['coordinates'][1] = place.lat
        temp_feature['properties']['title'] = place.title
        places_geojson['features'].append(temp_feature)

    context = {'value': places_geojson}
    return render(request, 'index.html', context=context)


def api(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    return HttpResponse(place.title)
