from django.db import models
from django.utils.timezone import now


class Post(models.Model):
    is_boast = models.BooleanField(default=True)
    content = models.CharField(max_length=150)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    submit_time = models.DateTimeField(default=now)

    @property
    def count(self):
        return self.upvotes - self.downvotes