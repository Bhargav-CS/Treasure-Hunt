from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.CharField(max_length=255, default='')
    contact_email = models.EmailField()
    submission_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    
class Round2Submission(models.Model):
    team_name = models.CharField(max_length=100)
    participant_code = models.TextField()
    submission_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Team: {self.team_name}, Code: {self.participant_code}"