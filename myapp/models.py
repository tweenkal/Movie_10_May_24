from django.db import models

# Create your models here.

city_list=[
    ('1','ahmedabad'),
    ('2','gandhinagar'),
    ('3','memdabad'),
    ('4','rajkort'),
    ('5','surat'),
]
state_list=[
    ('1','Gujarat'),
    ('2','up'),
    ('3','Mp'),
    ('4','rajstan'),
    ('5','punjab'),
]

type_list=[
    ('1','2D'),
    ('2','3D'),
]

language_list=[
    ('1','Gujarati'),
    ('2','English'),
    ('3','Hindi'),
    ('4','tamil'),
    ('5','punjabi'),
]

class category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()

    def __str__(self):
        return self.name


class male_actor(models.Model):
    name=models.CharField(max_length=30)
    dob=models.DateField()
    description=models.TextField()

    def __str__(self):
        return self.name


class female_actor(models.Model):
    name=models.CharField(max_length=30)
    dob=models.DateField()
    description=models.TextField()

    def __str__(self):
        return self.name

class movie(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
    actor=models.ForeignKey(male_actor,on_delete=models.CASCADE)
    actress=models.ForeignKey(female_actor,on_delete=models.CASCADE)
    moviecategory=models.ForeignKey(category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class multiplex(models.Model):
     name=models.CharField(max_length=30)
     address=models.TextField()
     no_of_screens=models.IntegerField()
     city=models.CharField(max_length=50,choices=city_list)
     state=models.CharField(max_length=50,choices=state_list)
     website=models.URLField()

     def __str__(self):
         return self.name

class shows(models.Model):
    moviename=models.ForeignKey(movie,on_delete=models.CASCADE)
    multiplex=models.ForeignKey(multiplex,on_delete=models.CASCADE)
    showstime=models.DateTimeField()
    seats=models.IntegerField()
    ticket_price=models.IntegerField()
    type=models.CharField(max_length=30,choices=type_list)
    language=models.CharField(max_length=30,choices=language_list)