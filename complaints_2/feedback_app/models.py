from django.db import models

class Feedback(models.Model):
    content = models.TextField()
    is_complaint = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{'Жалоба' if self.is_complaint else 'Предложение'}: {self.content}"
