# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Student(models.Model):
    enrollment_no = models.CharField(max_length=50, default=None, unique=True)
    first_name = models.CharField(max_length=200, default=None)
    last_name = models.CharField(max_length=200, default=None)
    email = models.EmailField(default=None)
    current_semester = models.IntegerField(default=1, null=True)
    graduation_year = models.IntegerField(null=True)
    is_active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.enrollment_no


class Course(models.Model):
    course_name = models.CharField(max_length=200, default=None)
    course_code = models.CharField(max_length=50, default=None)
    semester = models.IntegerField(default=0)
    total_lectures = models.IntegerField(default=0)

    def __str__(self):
        return self.course_code


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.IntegerField()
    section = models.CharField(max_length=50, default=None)
    lectures_attended = models.IntegerField(default=0)

    def __str__(self):
        return self.student.enrollment_no + " " + self.course.course_code


class Professor(models.Model):
    professor_id = models.CharField(max_length=200, default=None, unique=True)
    first_name = models.CharField(max_length=200, default=None)
    last_name = models.CharField(max_length=200, default=None)
    email = models.EmailField(default=None)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.professor_id


class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecture_date = models.DateTimeField()
    no_of_lectures = models.IntegerField(default=None)
    lecture_type = models.CharField(max_length=50, default=None)
    professor = models.ForeignKey(Professor)
    rating = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.course.course_code


class Attendance(models.Model):
    student_course = models.ForeignKey(StudentCourse, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)
    token = models.CharField(max_length=100, default=None, null=True)
    rating = models.DecimalField(max_digits=5, decimal_places=1)
    feedback = models.TextField()


class Session(models.Model):
    auth_token = models.CharField(max_length=200, default=None, unique=True)
    user_id = models.IntegerField(default=0)
    user_type = models.CharField(max_length=100, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()


class AttendanceToken(models.Model):
    token = models.CharField(max_length=100, default=None)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    token_issued = models.IntegerField(default=0)
    token_accepted = models.IntegerField(default=0)

    def __str__(self):
        return self.token
