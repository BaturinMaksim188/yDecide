from django.contrib import admin
from .models import *

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'age']
#     # list_filter = [] # there will be filter for courses and mentors
#     search_fields = ['first_name', 'last_name', 'age'] # also need to add courses and mentors fields
#     prepopulated_fields = {'slug': ('first_name', 'last_name',)}
#     # raw_id_fileds = ['mentor']

# @admin.register(Teacher)
# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ['programming_language', 'first_name', 'last_name']
#     search_fields = ['programming_language', 'first_name', 'last_name']
#     prepopulated_fields = {'slug': ("first_name", "last_name", "programming_language", )}

# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ['name', 'rate', 'created']
#     search_fields = ['name', 'rate', 'created']
#
# @admin.register(CourseContent)
# class CourseContentAdmin(admin.ModelAdmin):
#     list_display = ['course']
#     search_fields = ['course']
#
# @admin.register(Schedule)
# class ScheduleAdmin(admin.ModelAdmin):
#     list_display = ['student']
#     search_fields = ['student']
