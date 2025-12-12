from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # First logic
        super().save(*args, **kwargs)

        # Check if the image file exists
        if self.image and os.path.exists(self.image.path):
            img = Image.open(self.image.path)

            # First resizing logic
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

        # Second logic (your second block)
        super().save(*args, **kwargs)  # again included as you requested

        img = Image.open(self.image.path)

        # Second resizing logic
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
