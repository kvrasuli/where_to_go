from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Image, Place
import requests


class Command(BaseCommand):
    help = ''

    def add_arguments(self, parser):
        parser.add_argument('json', help='Place json url')

    def handle(self, *args, **options):
        response = requests.get(options['json'])
        response.raise_for_status()
        new_place = response.json()

        place, created = Place.objects.get_or_create(
            title=new_place['title'],
            description_short=new_place['description_short'],
            description_long=new_place['description_long'],
            latitude=new_place['coordinates']['lat'],
            longitude=new_place['coordinates']['lng'],
        )
        if created:
            for pic_name, image_url in enumerate(new_place['imgs']):
                response = requests.get(image_url)
                response.raise_for_status()

                with open(f'media/{pic_name}.jpg', 'wb') as image:
                    image.write(response.content)

                image = Image.objects.create(title=place)
                image.image.save(f'media/{pic_name}.jpg', ContentFile(response.content), save=True)
            self.stdout.write(f'New place {place.title} has been loaded!')
        else:
            self.stdout.write(f'The place {place.title} already exists!')