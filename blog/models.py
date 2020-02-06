from django.db import models
from django.utils import timezone

## Creo la clase POST que va a definir mis entradas
class Post(models.Model):
	## Los atributos de mi post: ForeignKey es un enlace con otro modelo
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    ## Texto con número limitado de caracteres
    title = models.CharField(max_length=200)
    ## Texto sin límite
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
# Create your models here.
