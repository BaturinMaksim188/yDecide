from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    pass

# class Student(models.Model):
#     first_name = models.CharField(max_length=30, verbose_name="First name", blank=False)
#     last_name = models.CharField(max_length=30, verbose_name="Last name", blank=False)
#     age = models.PositiveIntegerField(null=False, validators=[MinValueValidator(3), MaxValueValidator(120)],
#                                       verbose_name="Age", blank=False)
#     # date of creating a student account
#     created = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         # new students will go first
#         ordering = ['-created']
#         indexes = [
#             models.Index(fields=['-created']),
#         ]
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}, {self.age} y.o."
#
#     def get_absolute_url(self):
#         return reverse('Student', kwargs={'slug': ('first_name', 'last_name', 'age',)})
#
#
# class Teacher(models.Model):
#     first_name = models.CharField(max_length=30, verbose_name="First name", blank=False)
#     last_name = models.CharField(max_length=30, verbose_name="Last name", blank=False)
#     programming_language = models.CharField(max_length=50, verbose_name="Programming language", blank=False)
#     email = models.EmailField(max_length=250, verbose_name="Email", blank=False)
#     students = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(300)],
#                                    verbose_name="Number of students")
#     slug = models.SlugField(max_length=255, unique=True, blank=False, verbose_name="URL")
#     # date of creating a teacher account
#     created = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ['programming_language', 'first_name', 'last_name']
#         indexes = [
#             models.Index(fields=['programming_language', 'first_name', 'last_name']),
#         ]
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}, преподаватель по {self.programming_language}."
#
#     def get_absolute_url(self):
#         return reverse('TeacherProfile', kwargs={'slug': self.slug})
#
#
# class Course(models.Model):
#     name = models.CharField(max_length=30, verbose_name="Course name", blank=False)
#     entrant = models.IntegerField(verbose_name="Members")
#     rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], verbose_name="Course rating")
#     # date of creating a student account
#     created = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ['-created']
#         indexes = [
#             models.Index(fields=['-created']),
#         ]
#
#     def __str__(self):
#         return f"Курс {self.name}"
#
#     def get_absolute_url(self):
#         return reverse('Course', kwargs={'slug': ('name',)})
#
#
# # class CourseContent(models.Model):
# #     course = models.ForeignKey(Course, on_delete = models.SET_NULL)
# #     #Insert your course components here.
#
#
# class Schedule(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     lessons = models.CharField(max_length=10000, verbose_name="Lessons")
#
#     # lessons format -
#     # {"Monday" : "Python lesson 1", "Tuesday" : "Python lesson 2", ...}
#     # To display, we use dict.values() by the key for the day of the week.
#
#     class Meta:
#         ordering = ['student']
#         indexes = [
#             models.Index(fields=['student']),
#         ]
#
#     def __str__(self):
#         return f"Расписание студента {self.student['first_name']}  {self.student['last_name']}."
#
#     def get_absolute_url(self):
#         return reverse('Schedule', kwargs={'slug': ('student',)})
