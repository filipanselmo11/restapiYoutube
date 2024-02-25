#Convertendo os campos da Modelo para um arquivo JSON

from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('id', 'titulo', 'image', 'conteudo', 'slug', 'publicado', 'autor', 'status')