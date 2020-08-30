from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Place, Image
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
    images = Image.objects.filter(title=place)
    imgs = [image.image.url for image in images]
    place_params = {
        "title": place.title,
        "imgs": imgs,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {"lng": place.lng, "lat": place.lat}
    }
    return JsonResponse(
        place_params,
        safe=False,
        json_dumps_params={'ensure_ascii': False}
    )
