from rest_framework.serializers import ModelSerializer
from new.models import Books

class BooksSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'