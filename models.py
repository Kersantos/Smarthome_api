from django.db import models
from django.contrib.auth.models import User

class Local(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.TextField()

class Ambiente(models.Model):
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    descricao = models.TextField()
    cor = models.CharField(max_length=50)

class Dispositivo(models.Model):
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    descricao = models.TextField()
    online = models.BooleanField(default=True)
    ligado = models.BooleanField(default=False)
    cor = models.CharField(max_length=50)
    last_communication = models.DateTimeField(null=True)
