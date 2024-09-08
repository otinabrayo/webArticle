from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'slug', 'published')


    def create(self, validated_data):
        return Article.objects.create(**validated_data)

