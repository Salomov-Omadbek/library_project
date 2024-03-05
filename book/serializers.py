from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Books


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'