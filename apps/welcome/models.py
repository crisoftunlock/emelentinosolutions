from django.db import models

# Create your models here.

class Welcome(models.Model):
    image = models.ImageField(verbose_name="Image", upload_to="welcome")
    title = models.TextField(verbose_name="Title")
    animated_text = models.TextField(verbose_name="Animated Title")
    paragraph = models.TextField(max_length=50, verbose_name="Paragraph")

    class Meta:
        verbose_name = "Welcome"

    def __str__(self):
        return str(self.title)