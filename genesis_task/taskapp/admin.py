from django.contrib import admin
from.models import *


class AllUsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number', 'email', 'birth_date')
    list_display_links = ('id', 'first_name')


class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'reg_number')
    list_display_links = ('id', 'user')


class TeachersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id', 'user')


class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class StudentsSubjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'subject', 'mark')
    list_display_links = ('id', 'student')


class TeachersSubjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher', 'subject')
    list_display_links = ('id', 'teacher')


admin.site.register(AllUsers, AllUsersAdmin)
admin.site.register(Students, StudentsAdmin)
admin.site.register(Teachers, TeachersAdmin)
admin.site.register(Subjects, SubjectsAdmin)
admin.site.register(TeachersSubjects, TeachersSubjectsAdmin)
admin.site.register(StudentsSubjects, StudentsSubjectsAdmin)


