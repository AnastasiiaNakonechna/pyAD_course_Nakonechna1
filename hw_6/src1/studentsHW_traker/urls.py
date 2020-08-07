from django.contrib import admin
from django.urls import path

# from group import views # noqa

from studentsHW import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('generate-student/', views.generate_student),
    path('generate-students/', views.generate_students),
    path('group/', views.students_group),
    path('teachers/', views.teachers_list),
    path('teachersf/', views.teachers),
    path('', views.index),
    path('create-teachers/', views.create_teachers),
    path('new', views.index1),
    path('create-group/', views.create_group),
]
