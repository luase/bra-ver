from django.db import models

# Answer


class Answer(models.Model):
    text = models.CharField(max_length=45)

    def __str__(self):
        return self.text

# Question


class Question(models.Model):
    text = models.CharField(max_length=45)

    def __str__(self):
        return self.text

# Respuestas correctas


class CorrectAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return self.question.text + ' ' + self.answer.text

# # User
#
#
# class Period(models.Model):
#     descr = models.CharField(max_length=20)
#     begin_date = models.DateTimeField('Begin date')
#     end_date = models.DateTimeField('End date')
#
#     def __str__(self):
#         return self.descr
#
# # Group of questions
#
#
# class Time_Block(models.Model):
#     descr = models.CharField(max_length=60)
#     begin_minute = models.IntegerField()
#     end_minute = models.IntegerField()
#     monday = models.BooleanField(default=False)
#     tuesday = models.BooleanField(default=False)
#     wednesday = models.BooleanField(default=False)
#     thursday = models.BooleanField(default=False)
#     friday = models.BooleanField(default=False)
#     saturday = models.BooleanField(default=False)
#     sunday = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.descr
#
# # Salon de clases
#
#
# class Classroom(models.Model):
#     descr = models.CharField(max_length=10, null=True)
#     seat_count = models.IntegerField()
#     has_projector = models.BooleanField(default=False)
#     building = models.CharField(max_length=1)
#
#     def __str__(self):
#         return 'Building ' + self.building + ', ' + self.descr
#
# # Profesores/Maestros
#
#
# class Professor(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     department = models.ForeignKey(
#         Department, on_delete=models.CASCADE, related_name='members')
#     username = models.CharField(max_length=20)
#     user_passw = models.CharField(max_length=25)
#     is_administrator = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.first_name + ' ' + self.last_name
#
# # Horario
#
#
