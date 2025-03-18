from django.db import models

class CursorSkin(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='django/images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name