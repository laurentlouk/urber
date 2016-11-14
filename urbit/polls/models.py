from django.db import models
from django.utils import timezone

#class Information(models.Model):
#    author = models.ForeignKey('auth.User')
#    name = models.CharField(max_length=100)
#    email = models.EmailField(max_length=200)
#    password = models.CharField(max_length=100)
#    house_no = models.CharField(max_length=100)
#    address_line = models.CharField(max_length=200)
#    telephone = models.CharField(max_length=100)
#    zip_code = models.CharField(max_length=20)
#    city = models.CharField(max_length=100)
#    country = models.CharField(max_length=100)
#    published_date = models.DateTimeField(
#            blank=True, null=True)

#    def __str__(self):
#        return self.name

#    def publish(self):
#        self.published_date = timezone.now()
#        self.save()
