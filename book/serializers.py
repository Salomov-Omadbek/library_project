from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Books


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        if Books.objects.filter(title=title).exists():
            raise ValidationError({
                'status': 'Title',
                'message': 'Title already exists.'
            })

        if not title.isalpha() or not author.isalpha():
            raise ValidationError({
                'status': 'Invalid Data',
                'message': 'Title and Author must be alphanumeric.'
            })

        return data
