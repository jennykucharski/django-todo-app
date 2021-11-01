from rest_framework import serializers
from todo_app.models import Note
from django.db import transaction
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'name', 'content', 'created_at', 'modified_at', 'created_by']
        
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


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=255, default='')
    last_name = serializers.CharField(max_length=255, default='')
    date_of_birth = serializers.DateField()

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'date_of_birth',
            'password1',
            'password2',
        )

    def save(self, request):
        user = super().save(request)
        user.first_name = self.data.get('first_name')
        user.last_name = self.data.get('last_name')
        user.date_of_birth = self.data.get('date_of_birth')
        user.save()
        return user


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'first_name',
            'last_name',
        )
        read_only_fields = ('pk', 'email', 'first_name', 'last_name')