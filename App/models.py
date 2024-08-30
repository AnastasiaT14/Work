from django.db import models


class Application(models.Model):
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
