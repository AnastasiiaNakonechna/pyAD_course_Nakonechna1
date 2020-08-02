import random

from django.core.management.base import BaseCommand

from faker import Faker

from studentsHW.models import Teachers


class Command(BaseCommand):
    help = 'Generate random teachers num50' # noqa

    def handle(self, *args, **options):
        fake = Faker()

    def foo(request):

        count = int(request.GET['count'])

        for _ in range(count):
            Teachers.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=int(random.uniform(17, 51))
            )

