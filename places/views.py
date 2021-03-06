from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Place


def index(request):
    places = Place.objects.all()
    places_geojson = {"type": "FeatureCollection", "features": []}
    for place in places:
        places_geojson['features'].append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title, "placeId": place.id,
                "detailsUrl": reverse('api', args=[place.id])
            }
        })
    context = {'value': places_geojson}
    return render(request, 'index.html', context=context)


def api(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    images = place.images.all()
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
