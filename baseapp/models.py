from django.db import models
from ckeditor.fields import RichTextField

class Task(models.Model):
    title = models.CharField(max_length=300)
    description = RichTextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed']