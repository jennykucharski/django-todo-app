from rest_framework import serializers
from todo_app.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'name', 'content', 'created_at', 'modified_at']


    def create(self, validated_data):
        """
        Create and return a new `Note` instance, given the validated data.
        """
        return Note.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Code` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.modified_at = validated_data.get('modified_at', instance.modified_at)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
        