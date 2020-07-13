from django.contrib import admin
from django.urls import path

from group import views

from studentsHW import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('generate-student/', views.generate_student),
    path('generate-students/', views.generate_students),
    path('group/', views.students_group),
    path('teachers/', views.teachers_list),
]
