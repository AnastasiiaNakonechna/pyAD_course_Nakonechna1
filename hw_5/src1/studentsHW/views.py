import random

from django.http import HttpResponse

from faker import Faker

from studentsHW.models import Group, Student, Teachers


def generate_student(request):
    fake = Faker()
    student = Student.objects.create(first_name=fake.first_name(), last_name=fake.last_name(), age=int(random.uniform(1, 100)))
    response = f'Student {student.id} <br/> first_name: {student.first_name} <br/> last_name: {student.last_name} <br/>  age: {student.age} <br/>'
    # print(student.id, student.first_name, student.last_name, student.age)
    return HttpResponse(response)


def generate_students(request):

    fake = Faker()
    fake.first_name()
    fake.last_name()

    count = int(request.GET['count'])

    f = ''
    for _ in range(count):
        student = Student.objects.create(first_name=fake.first_name(), last_name=fake.last_name(), age=int(random.uniform(17, 51)))
        f += f'Student N{student.id}: first_name: {student.first_name}; last_name: {student.last_name}; age: {student.age} <br/>'
        # print(f)

    return HttpResponse(f)


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


def teachers_list(request):
    fake = Faker()
    fake.first_name()
    fake.last_name()

    f = ''
    for _ in range(0, 16):
        teachers = Teachers.objects.create(first_name=fake.first_name(), last_name=fake.last_name(), age=int(random.uniform(17, 51)))
        f += f'N{teachers.id} Teacher: first_name: {teachers.first_name}; last_name: {teachers.last_name}; age: {teachers.age} <br/>'
        # print(f)

    return HttpResponse(f)


def teachers(request):

    params = [
        'first_name',
        'last_name',
        'age',
    ]

    teachers_queryset = Teachers.objects.all()

    for param in params:
        value = request.GET.get(param)
        if value:
            teachers_queryset = teachers_queryset.filter(**{param: value})

    response = f'teachers: {teachers_queryset.count}<br/>'

    for teachers in teachers_queryset:
        response += teachers.teach_info() + '<br/>'

    return HttpResponse(response)
