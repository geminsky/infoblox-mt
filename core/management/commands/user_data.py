import json
import uuid

from django.core.management.base import BaseCommand
from core.models import Users, Data


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        with open(options['json_file'], encoding='utf-8') as f:
            data_list = json.load(f)

        for data in data_list:
            data['id'] = data.pop('id')
            user_data_list = data['data']
            Data.objects.get_or_create(guid=uuid.UUID(user_data_list[0]['guid']), enabled=user_data_list[0]['enabled'])
            user_data = Data.objects.get(guid=uuid.UUID(user_data_list[0]['guid']))
            u, created = Users.objects.get_or_create(first_name=data['first_name'],
                                                     last_name=data['last_name'], city=data['city'])
            u.data.add(user_data)
            u.save()
