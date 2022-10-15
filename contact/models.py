from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=300)
    message = models.TextField(max_length=2000)
    ip = models.CharField(max_length=200)
    create_date = models.DateField(auto_now=True)
    create_time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Aloqa'
        verbose_name_plural = 'Aloqa'
