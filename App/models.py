from django.db import models

class Workout(models.Model):
    part_of_body = models.CharField(max_length=100)
    quantity_of_workouts = models.IntegerField()  # Remove max_length
    duration = models.IntegerField()  # Remove max_length

class Exercises(models.Model):
    workout = models.ForeignKey(Workout, related_name='exercises', on_delete=models.CASCADE)
    exercise = models.CharField(max_length=100)
    reps = models.IntegerField()
    sets = models.IntegerField()

    def __str__(self):
        return f"{self.exercise}: {self.reps} reps, {self.sets} sets"

class Measurements(models.Model):
    WEIGHT_GOAL_CHOICES = [
        ('gain', 'Gain Weight'),
        ('lose', 'Lose Weight'),
    ]

    weight = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    goal_weight = models.CharField(
        max_length=10,
        choices=WEIGHT_GOAL_CHOICES,
        default='lose'
    )

    def __str__(self):
        return f"{self.weight}, {self.height}, Goal: {self.get_goal_weight_display()}"
