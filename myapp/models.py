from django.db import models

# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    date = models.DateField()
    time = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{self.name} — {self.date} at {self.time}"


class Feedback(models.Model):
    FEEDBACK_TYPES = [
        ("compliment", "Compliment"),
        ("suggestion", "Suggestion"),
        ("issue", "Report an issue"),
    ]

    feedback_type = models.CharField(max_length=20, choices=FEEDBACK_TYPES)
    rating = models.PositiveSmallIntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{self.get_feedback_type_display()} — {self.rating} stars"