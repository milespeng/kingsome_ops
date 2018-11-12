from django.db import models


# Create your models here.
# run python manage.py  makemigrations  cmdb
# python manage.py migrate
# python manage.py createsuperuser

class Machine(models.Model):
    machine_id = models.IntegerField(auto_created=1)
    machine_name = models.CharField(max_length=200)
    public_ip = models.CharField(max_length=40)
    priv_ip = models.CharField(max_length=40)
    create_time = models.DateTimeField('创建时间', auto_now=True)

    def __str__(self):
        return self.machine_name

