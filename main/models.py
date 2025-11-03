from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError

def validate_umich_email(value):
        if not value.endswith('@umich.edu'):
            raise ValidationError('Email must be a @umich.edu address.')

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=now)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class LeadershipPosition(models.Model):
    title = models.CharField(max_length=100, unique=True)
    email = models.EmailField(blank=True, null=True, validators=[validate_umich_email])
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']  # Ensures positions are ordered by display_order

    def __str__(self):
        return self.title
    

class LeadershipMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.ForeignKey(LeadershipPosition, on_delete=models.CASCADE, related_name='leaders')
    bio = models.TextField()
    photo = models.ImageField(upload_to='leadership_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.position.title}"