from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=500)
    author = models.ForeignKey(User, related_name="ads", on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="django_media")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Comment(models.Model):
    text = models.CharField(max_length=100, null=False, blank=False)
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=False, auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
