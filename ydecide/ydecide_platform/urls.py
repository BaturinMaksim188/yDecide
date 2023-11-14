from django.contrib import admin
from django.urls import path, include
from represent import views as represent_views

urlpatterns = [
    path('', represent_views.main, name='main'),
    path('news/', represent_views.news, name='news'),
    path('lesson_schedule/', represent_views.lesson_schedule, name='lesson_schedule'),

    path('admin/', admin.site.urls),
    path('represent/', include('represent.urls'))
    # path('<slug:slug>', teacher_profile, name='TeacherProfile'),
]

handler404 = "represent.views.page_not_found_view"
