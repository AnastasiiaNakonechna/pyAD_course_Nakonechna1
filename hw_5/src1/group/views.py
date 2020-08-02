import random

from django.http import HttpResponse

from faker import Faker

from studentsHW.models import Group, Student # noqa


def students_group(request):
    fake = Faker()
    fake.first_name()
    fake.last_name()

    f = ''
    for _ in range(0, 31):
        students = Group.objects.create(first_name=fake.first_name(), last_name=fake.last_name(), scores_in_group=int(random.uniform(17, 51)))
        f += f'Student N{students.id}: first_name: {students.first_name}; last_name: {students.last_name}; total scores: {students.scores_in_group} <br/>'
        # print(f)

    return HttpResponse(f)
