from django.db import models
from datetime import date
from django.contrib.auth.models import User
MEALS = (
      ('B', 'Breakfast'),
      ('L', 'Lunch'),
      ('D', 'Dinner')
)

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    
    def __str__(self):
        return f'A {self.color} {self.name}' 

# Create your models here.
class Cat(models.Model): 
    name = models.CharField(max_length=100)
    breed =  models.CharField(max_length=100)
    description =  models.TextField(max_length=250)
    age =  models.IntegerField()  
    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
    # first optional argument for field types is overridng,
    # default naming of field in GUI
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=MEALS,
        # set the default value for meal to be 'B'
        default=MEALS[0][0]
    )
    # create a cat id foreign key reference
    # this creates a 'one to many' relationship, one being the cat, 
    # this feeding being the many
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    # change the default sort
    class Meta:
        ordering = ['-date']

   
