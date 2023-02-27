from rest_framework import serializers
from blogs.models import Blog


class BlogsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255, allow_null=False)
    description = serializers.CharField(min_length=2, max_length=1000, allow_null=True)
    owner = serializers.CharField(min_length=2, max_length=1000, allow_null=True)

    def create(self, validated_data):
        Blogs = Blogs(**validated_data)
        Blogs.save()
        return Blogs

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance


class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255, allow_null=False)
    description = serializers.CharField(min_length=2, max_length=1000, allow_null=True)
    owner = serializers.CharField(min_length=2, max_length=1000, allow_null=True)
    

    def create(self, validated_data):
        blog = Blog(**validated_data)
        blog.save()
        return blog

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
