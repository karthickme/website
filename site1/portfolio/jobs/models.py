from django.db import models

# Create your models here.
class Jobs(models.Model):
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None)
    summary = models.CharField(max_length=200)

    

    # class Meta:
    #     verbose_name = ("Jobs")
    #     verbose_name_plural = ("Jobss")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("Jobs_detail", kwargs={"pk": self.pk})