from django.db import models

class UsefulIdea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    submitted_by = models.CharField(max_length=100)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
