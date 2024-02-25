from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

def user_directory_path(instance, filename):
    return 'blog/{0}/{1}'.format(instance.titulo, filename)

class Post(models.Model):
    class PostObjects(models.Model):
        def get_query_set(self):
            return super().get_query_set() .filter(status='publicado')
    options = (
        ['rascunho', 'Rascunho'],
        ['publicado', 'Publicado']
    )
    titulo = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    excerpt = models.TextField(null=True)
    conteudo = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='publicado', null=False, unique=True)
    publicado = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_blog')
    status = models.CharField(max_length=10, choices=options, default='rascunho')
    objetos = models.Manager()
    postobjects = PostObjects()

    #Ordenar Postagens

    class Meta:
        ordering = ('-publicado', )

    def __str__(self):
        return self.titulo
        
