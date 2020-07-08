from django.db import models


class AllUsers(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    birth_date = models.DateTimeField()

    def __str__(self):
        return self.first_name


class Students(models.Model):
    reg_number = models.CharField(max_length=50)
    user = models.ForeignKey(AllUsers, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name


class Teachers(models.Model):
    user = models.ForeignKey(AllUsers, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name


class Subjects(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class TeachersSubjects(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher.user.first_name


class StudentsSubjects(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    mark = models.IntegerField()

    def __str__(self):
        return self.student.user.first_name
