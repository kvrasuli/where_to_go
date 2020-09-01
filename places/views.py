from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Place, Image
import copy


def index(request):
    places = Place.objects.all()
    places_geojson = {"type": "FeatureCollection", "features": []}
    place_feature = {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [None, None]},
        "properties": {"title": None, "placeId": None, "detailsUrl": None}
    }
    for place in places:
        temp_feature = copy.deepcopy(place_feature)
        temp_feature['geometry']['coordinates'][0] = place.longitude
        temp_feature['geometry']['coordinates'][1] = place.latitude
        temp_feature['properties']['title'] = place.title
        temp_feature['properties']['placeId'] = place.id
        temp_feature['properties']['detailsUrl'] = reverse('api', args=[place.id])
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
        "coordinates": {"lng": place.longitude, "lat": place.latitude}
    }
    return JsonResponse(
        place_params,
        safe=False,
        json_dumps_params={'ensure_ascii': False}
    )
